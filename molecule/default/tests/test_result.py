import testinfra


def test_os_release(host):
    """test host release for good measure"""

    assert host.file("/etc/os-release").contains("Ubuntu")


def test_key_present(host):
    """test whether the key was created and has the correct comment"""

    assert host.file("/home/ansible/.ssh/testkey_ed25519.pub")

    assert host.file("/home/ansible/.ssh/testkey_ed25519.pub").contains("testkey")
