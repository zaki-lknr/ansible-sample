from ansible.errors import AnsibleActionFail, AnsibleFileNotFound
from ansible.module_utils.common.text.converters import to_text
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):

    TRANSFERS_FILES = True


    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)

        src = self._task.args.get("src")
        dest = self._task.args.get("dest")
        decrypt = boolean(
            self._task.args.get("decrypt", True),
            strict=False,
        )

        # Check parameters.
        if not src:
            raise AnsibleActionFail(
                message="src is required",
                result=result,
            )

        if not dest:
            raise AnsibleActionFail(
                message="dest is required",
                result=result,
            )

        # Find source file on the controller.
        try:
            source = self._find_needle(
                "files",
                src,
            )
        except Exception as e:
            raise AnsibleActionFail(
                message=f"Could not find src={src}: {e}",
                result=result,
            ) from e

        # Resolve the real file.
        #
        # decrypt=True:
        #   If source is an Ansible Vault encrypted file,
        #   Ansible decrypts it on the controller.
        try:
            source = self._loader.get_real_file(
                source,
                decrypt=decrypt,
            )
        except AnsibleFileNotFound as e:
            raise AnsibleActionFail(
                message=(
                    f"Could not find src={src}: "
                    f"{to_text(e)}"
                ),
                result=result,
            ) from e

        # Create a temporary path on the managed node.
        tmp_src = self._connection._shell.join_path(
            self._connection._shell.tmpdir,
            ".zaki_lknr_sample_copy",
        )

        # Transfer the file from controller to managed node.
        try:
            remote_path = self._transfer_file(
                source,
                tmp_src,
            )
        except Exception as e:
            self._loader.cleanup_tmp_file(source)

            raise AnsibleActionFail(
                message=f"Failed to transfer {src}: {e}",
                result=result,
            ) from e

        # The decrypted temporary file on the controller
        # is no longer needed.
        self._loader.cleanup_tmp_file(source)

        # Pass the transferred file to our module.
        module_args = self._task.args.copy()
        module_args["src"] = remote_path

        # "decrypt" is an Action Plugin option and is not
        # an argument of our module.
        module_args.pop("decrypt", None)

        module_return = self._execute_module(
            module_name="zaki_lknr.sample.copy",
            module_args=module_args,
            task_vars=task_vars,
            tmp=tmp,
        )

        result.update(module_return)

        return result
