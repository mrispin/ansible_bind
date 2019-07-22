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


def test_bind_resolve_master(host):
    servera = host.addr("servera.bind.test")
    serverb = host.addr("serverb.bind.test")
    mailservera = host.addr("mailservera.bind.test")
    mailserverb = host.addr("mailserverb.bind.test")
    assert servera.is_resolvable
    assert '127.2.2.5' in servera.ipv4_addresses
    assert serverb.is_resolvable
    assert '127.4.2.5' in serverb.ipv4_addresses
    assert mailservera.is_resolvable
    assert '127.4.52.5' in mailservera.ipv4_addresses
    assert mailserverb.is_resolvable
    assert '127.4.62.5' in mailserverb.ipv4_addresses
