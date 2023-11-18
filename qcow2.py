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

#- name: 'Create virt overlay image'
#  connection: 'local'
#  vars:
#    command: '/usr/bin/qemu-img create'
#    formats: '-fqcow2 -Fqcow2'
#    embed_cmd: 'readlink -f ../annex/{{ virts_base_image }}'
#    base_disk: '-obacking_file=$({{ embed_cmd }})'
#    new_disk: '/tmp/{{ inventory_hostname }}.qcow2'
#  shell: '{{ command }} {{ formats }} {{ base_disk }} {{ new_disk }}'
#
#- name: 'Create virt overlay image'
#  connection: 'local'
#  qemu_qcow2:
#    follow_symlinks: yes
#    base_disk: '../annex/{{ virts_base_image }}'
#    new_disk: '/tmp/{{ inventory_hostname }}.qcow2'

