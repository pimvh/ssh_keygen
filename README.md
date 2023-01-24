# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

## Required variables

Review the variables as shown in defaults.

```
ssh_keygen_storagedir: "~/.ssh" # where to save generated key
ssh_keygen_keyname: "ed25519" # filename of key
ssh_keygen_cipher: "ed25519" # passed to -t, values are dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa
ssh_keygen_cipher_options: "" # cipher options addtional args to pass when generating keys
ssh_keygen_comment: "" # Comment to set in the key
```

# Example playbook

```
hosts:
  - foo
roles:
  - pimvh.ssh_keygen

```

# TLDR - What will happen if I run this

- Generate ssh key
- Add public key as fact

# Future Improvements

- Add variable assertions
- Use community library instead for key generation

# License

The GPLv3 License (GPLv3)

Copyright (c) 2022 Author

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
