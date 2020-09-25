# my-module

Ansible 2.9ドキュメントベースでモジュール作成。

# local exec

```
(dev) [zaki@cloud-dev my-module]$ ls library/
my_test.py
(dev) [zaki@cloud-dev my-module]$ cat args.json 
{
    "ANSIBLE_MODULE_ARGS": {
        "name": "hello",
        "new": true
    }
}
(dev) [zaki@cloud-dev my-module]$ python -m library.my_test args.json 

{"changed": true, "original_message": "hello", "message": "goodbye", "invocation": {"module_args": {"name": "hello", "new": true}}}
```

# exec ansible-playbook

```
TASK [run the new module] *************************************
changed: [localhost]

TASK [dump test output] ***************************************
ok: [localhost] => {
    "msg": {
        "changed": true,
        "failed": false,
        "message": "goodbye",
        "original_message": "hello"
    }
}
```
