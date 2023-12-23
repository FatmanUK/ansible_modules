# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Adam J. Richardson <fatman.uk@gmail.com>

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: 'ansible_vault'
short_description: 'Manipulate Ansible Vaults.'
description:
  - 'Manipulate various functions of the Ansible Vault.'
version_added: '0.1'
options:
  mode:
    description:
      - 'The mode in which to execute.'
      - 'Current modes: encrypt.'
    type: 'str'
    required: yes
requirements:
  - 'installed Linux system'
  - 'ansible'
author:
  - 'Adam J. Richardson (@FatmanUK)'
extends_documentation_fragment:
    - 'action_common_attributes'
attributes:
    check_mode:
        support: 'full'
    diff_mode:
        support: 'full'
    platform:
        support: 'full'
        platforms: 'posix'
'''

EXAMPLES = r'''
- name: 'Make a plain text file into an Ansible Vault with password
        from password_file.'
  ansible_vault:
    mode: 'encrypt'
    password_file: '../{{ ansible_vault_secret }}'
    src: '{{ ansible_vault_random_filename.path }}'
    dest: '../{{ ansible_vault_file }}'
'''

RETURN = r'''#'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native

def main():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    changed = True
    res_args = dict()
    warnings = list()

# TODO: when more functions crop up, split into ansible_encrypt and so on?

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

    res_args = dict(
        warnings=warnings,
        changed=changed
    )

    module.exit_json(**res_args)

if __name__ == '__main__':
    main()

