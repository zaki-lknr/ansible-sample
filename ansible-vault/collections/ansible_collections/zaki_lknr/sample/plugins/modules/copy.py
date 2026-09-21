#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os
import shutil


def main():
    module = AnsibleModule(
        argument_spec={
            "src": {
                "type": "path",
                "required": True,
            },
            "dest": {
                "type": "path",
                "required": True,
            },
        },
        supports_check_mode=True,
    )

    src = module.params["src"]
    dest = module.params["dest"]

    # コピー元が存在することを確認
    if not os.path.isfile(src):
        module.fail_json(
            msg=f"Source file does not exist: {src}"
        )

    # check mode
    if module.check_mode:
        module.exit_json(
            changed=(not os.path.exists(dest))
        )

    try:
        # コピー先ディレクトリが存在することを確認
        dest_dir = os.path.dirname(dest)

        if dest_dir and not os.path.isdir(dest_dir):
            module.fail_json(
                msg=f"Destination directory does not exist: {dest_dir}"
            )

        # コピー
        shutil.copy2(src, dest)

    except OSError as e:
        module.fail_json(
            msg=f"Failed to copy file: {e}"
        )

    module.exit_json(
        changed=True,
        src=src,
        dest=dest,
    )


if __name__ == "__main__":
    main()
