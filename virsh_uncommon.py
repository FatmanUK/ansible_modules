# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Adam J. Richardson <fatman.uk@gmail.com>

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
'''

EXAMPLES = r'''
'''

RETURN = r'''#'''

#import os
#import platform
#import pwd
#import re
#import sys
#import tempfile

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
#from ansible.module_utils.six.moves import shlex_quote

def main():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    changed = True
    res_args = dict()
    warnings = list()



    res_args = dict(
        warnings=warnings,
        changed=changed
    )

    module.exit_json(**res_args)

if __name__ == '__main__':
    main()

#    virts_xml: '/tmp/{{ inventory_hostname }}.xml'
#  command:
#    argv:
#      - '/usr/bin/virsh'
#      - 'define'
#      - '{{ virts_xml }}'
#
#  virsh_uncommon:
#    mode: 'xml_define'
#    file: '{{ virts_xml }}'
#
#- name: 'Mark host autostarted (not on dev)'
#  vars:
#    autostart_command:
#      - '/usr/bin/virsh'
#      - '-c'
#      - 'qemu:///session'
#      - 'autostart'
#    autostart_state: '{{ [ "--disable" ] if env == "dev" else [] }}'
#  delegate_to: '{{ hypervisor_host }}'
#  command:
#    argv: '{{ autostart_command + autostart_state + [ fqdn ] }}'
#
#
#  command:
#    argv: '{{ autostart_cmd + autostart_state + [ fqdn ] }}'
#
#
#- name: 'Mark host autostarted (not on dev)'
#  vars:
#    autostart_cmd:
#      - '/usr/bin/virsh'
#      - '-c'
#      - 'qemu:///session'
#      - 'autostart'
#    autostart_state: '{{ [ "--disable" ] if env == "dev" else [] }}'
#  delegate_to: '{{ hypervisor_host }}'
#  virsh_uncommon:
#    mode: 'autostart'
#    disabled: '{{ env == "dev" }}'
#    domain: '{{ fqdn }}'
#
#  command:
#    argv: '{{ autostart_cmd + autostart_state + [ fqdn ] }}'
#
#- name: 'Mark host autostarted (not on dev)'
#  vars:
#    autostart_cmd:
#      - '/usr/bin/virsh'
#      - '-c'
#      - 'qemu:///session'
#      - 'autostart'
#    autostart_state: '{{ [ "--disable" ] if env == "dev" else [] }}'
#  delegate_to: '{{ hypervisor_host }}'
#  virsh_uncommon:
#    mode: 'autostart'
#    disabled: '{{ env == "dev" }}'
#    domain: '{{ fqdn }}'
#
#  command:
#    argv: '{{ autostart_cmd + autostart_state + [ fqdn ] }}'
#
#- name: 'Mark host autostarted (not on dev)'
#  delegate_to: '{{ hypervisor_host }}'
#  virsh_uncommon:
#    mode: 'autostart'
#    disabled: '{{ env == "dev" }}'
#    domain: '{{ fqdn }}'
#
#- name: 'Remove default virbr0 network interface'
#  notify: 'Restart iptables'
#  loop:
#    - 'destroy'
#    - 'undefine'
#  virsh_uncommon:
#    mode: 'net_destroy'
#    name: 'default'
#
#  virsh_uncommon:
#    mode: 'net_undefine'
#    name: 'default'
#
#  command:
#    argv:
#      - 'virsh'
#      - 'net-{{ item }}'
#      - 'default'
#
#- name: 'Modify default virbr0 network interface'
#  notify: 'Restart iptables'
#  virsh_uncommon:
#    mode: 'net_define'
#    path: '/tmp/network-default.xml'
#    validate: yes
##  command:
##    argv:
##      - 'virsh'
##      - 'net-define'
##      - '/tmp/network-default.xml'
##      - '--validate'
#
#- name: 'Set default virbr0 to autostart'
#  notify: 'Restart iptables'
#  loop:
#    - 'autostart'
#    - 'start'
#  virsh_uncommon:
#    mode: 'net_{{ item }}'
#    name: 'default'
##  command:
##    argv:
##      - 'virsh'
##      - 'net-{{ item }}'
##      - 'default'

