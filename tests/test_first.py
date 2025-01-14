from jacob_os_version_check.osver import get_os_pretty_name

def test_first():
    v = get_os_pretty_name()
    assert v == "Ubuntu 24.04.1 LTS"

