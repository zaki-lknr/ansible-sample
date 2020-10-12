#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule

def run_module():

    # パラメタ定義
    module_args = dict(
        opt=dict(type='str', required=True),
        state=dict(type='str', required=False, default='present'),
        changed=dict(type='bool', required=False, default=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=False,
        message=''
    )

    if module.check_mode:
        module.exit_json(**result)

    # ロジックここから
    result['message'] = module.params['opt']
    if module.params['changed']:
        result['changed'] = True

    if module.params['opt'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)
    # ロジックここまで

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
