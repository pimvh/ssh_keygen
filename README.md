![Molecule test](https://github.com/pimvh/ssh_keygen/actions/workflows/test.yaml/badge.svg)
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
ssh_keygen_passphrase: "" # Optionally pass a passphrase to generated key (to not prompt for one)
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
