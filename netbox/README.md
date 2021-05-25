# source

- create-device-resources.yml:
    - デバイスを登録するまでに必要なSite/DeviceRole/Manufacturer/DeviceTypeとDeviceを作成
    - からの、device bay情報登録

# コレクションのupdate

```
(a2.10) [zaki@cloud-dev netbox (master)]$ ansible-galaxy collection list | grep netbox
netbox.netbox             1.2.1  
# /home/zaki/src/ansible-sample/netbox/collections/ansible_collections
netbox.netbox     2.1.0  
netbox.netbox             1.2.1  
```

```
(a2.10) [zaki@cloud-dev netbox (master)]$ ansible-galaxy collection install netbox.netbox
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Skipping 'netbox.netbox' as it is already installed
```

```
(a2.10) [zaki@cloud-dev netbox (master)]$ ansible-galaxy collection install netbox.netbox:3.0.0
Starting galaxy collection install process
Process install dependency map
ERROR! Cannot meet requirement netbox.netbox:3.0.0 as it is already installed at version '2.1.0'. Use --force to overwrite
```

2.10では`upgrade`できない。

```
(a2.10) [zaki@cloud-dev netbox (master)]$ ansible-galaxy collection install netbox.netbox:3.0.0 --force
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Installing 'netbox.netbox:3.0.0' to '/home/zaki/src/ansible-sample/netbox/collections/ansible_collections/netbox/netbox'
Downloading https://galaxy.ansible.com/download/netbox-netbox-3.0.0.tar.gz to /home/zaki/.ansible/tmp/ansible-local-106921ypd8t2os/tmpqfdg6jbb
netbox.netbox (3.0.0) was installed successfully
```

```
(a2.10) [zaki@cloud-dev netbox (master)]$ ansible-galaxy collection list | grep netbox
netbox.netbox             1.2.1  
netbox.netbox             1.2.1  
# /home/zaki/src/ansible-sample/netbox/collections/ansible_collections
netbox.netbox     3.0.0  
```
