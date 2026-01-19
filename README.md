# ansible-role-dnsmasq

Ansible role to install and configure dnsmasq as a DNS and DHCP server.

## Requirements

- Ubuntu (focal, jammy, noble)

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `dnsmasq_interface` | `eth0` | Interface to listen on |
| `dnsmasq_domain` | `lan` | Local domain name |
| `dhcp_range_start` | `192.168.1.100` | DHCP range start IP |
| `dhcp_range_end` | `192.168.1.200` | DHCP range end IP |
| `dhcp_lease_time` | `24h` | DHCP lease duration |
| `dhcp_option_router` | `192.168.1.1` | Default gateway |
| `dhcp_option_dns` | `192.168.1.1` | DNS server for clients |
| `upstream_dns` | `[8.8.8.8, 8.8.4.4]` | Upstream DNS servers |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: ansible-role-dnsmasq
      vars:
        dnsmasq_interface: eth0
        dnsmasq_domain: home.local
        dhcp_range_start: 192.168.1.50
        dhcp_range_end: 192.168.1.150
        dhcp_lease_time: 12h
        dhcp_option_router: 192.168.1.1
        dhcp_option_dns: 192.168.1.1
        upstream_dns:
          - 1.1.1.1
          - 9.9.9.9
```

## License

MIT

## Author

Michael MACHADO
