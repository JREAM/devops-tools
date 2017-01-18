# Devops Ansible
Provisioning Servers with ease.

**Note**: I was unable to complete this once the company lost funding, so it would need some additions to
some of the roles. Additionally, the YML files (eg devops.yml, dockercloud.yml) could be re-arranged a better way or into a subfolder.

- [Update Hosts](#update-hosts)
- [Installation](#installation)
    - [Linux](#linux)
    - [OSX](#osx)
- [Run Playbooks](#run-playbooks)
- [Permissions](#permissions)

# Update Hosts
**Important**: To keep your `./hosts` the most up to date with the evolving
Docker Cloud, please always run this prior to running ansible.

For new hosts run the Python script which updates `./hosts`.
```
./update_hosts.py
```

# Installation
You first need the Ansible Client.

### Linux
I am using Xenail 16 for this:

```
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
```

```
sudo pip install 'dopy>=0.3.5,<=0.3.5'
sudo apt-get install ansible
```

### OSX
I do not run OSX, however it should be easy to install. To test, your best bet
is to run the `playbook-test.yml`.

```
brew install ansible
```

If you still have trouble please install PIP and try following this [link](https://valdhaus.co/writings/ansible-mac-osx/).

# Run Playbooks
Running a playbooks roles against a group of servers is quite easy by executing the following:
```
ansible-playbook playbook-name.yml
```

# Permissions
You will need SSH permissions on Docker Cloud. This would mean you need to edit the
`Stack File` entitled `auth_ssh` and append your key, then re-run the stack if you
do not have access.
