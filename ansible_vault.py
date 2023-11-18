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

#- name: 'Encrypt the lot'
#  ansible_vault:
#    mode: 'encrypt'
#    password_file: '../{{ ansible_vault_secret }}'
#    src: '{{ ansible_vault_random_filename.path }}'
#    dest: '../{{ ansible_vault_file }}'
#    
#  command:
#    argv:
#      - '/usr/bin/ansible-vault'
#      - 'encrypt'
#      - '--vault-password-file=../{{ ansible_vault_secret }}'
#      - '{{ ansible_vault_random_filename.path }}'
#      - '--output'
#      - '../{{ ansible_vault_file }}'

