import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_symlinks(host):
    link = host.file('/home/devuser1/httpd-logs')
    assert link.exists
    assert link.is_symlink
    assert link.linked_to == '/var/log/apache2'
