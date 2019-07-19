import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bind_installed(host):
    bind = host.package("bind9")
    assert bind.is_installed


def test_bind_service_started(host):
    bindservice = host.service("bind9")
    assert bindservice.is_running
    assert bindservice.is_enabled


def test_bind_listening(host):
    bindtsocket = host.socket("tcp://0.0.0.0:53")
    bindusocket = host.socket("udp://0.0.0.0:53")
    assert bindtsocket.is_listening
    assert bindusocket.is_listening

def test_bind_forwarding_requests(host):
    google = host.addr("google.com")
    assert google.is_resolvable
