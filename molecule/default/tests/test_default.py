import pytest


def test_dnsmasq_is_installed(host):
    dnsmasq = host.package("dnsmasq")
    assert dnsmasq.is_installed


def test_dnsmasq_service_running(host):
    dnsmasq = host.service("dnsmasq")
    assert dnsmasq.is_running
    assert dnsmasq.is_enabled


def test_dnsmasq_config_exists(host):
    config = host.file("/etc/dnsmasq.d/custom.conf")
    assert config.exists
    assert config.user == "root"
    assert config.group == "root"
