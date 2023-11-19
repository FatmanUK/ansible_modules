# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Adam J. Richardson <fatman.uk@gmail.com>

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: move
short_description: Move a file
description:
  - Use this module to move a file.
version_added: "0.1"
options:
  src:
    description:
      - The file to move.
    type: str
    required: yes
  dest:
    description:
      - The new path for the file.
    type: str
    required: yes
  overwrite:
    alias:
      - force
      - insist
    description:
      - Insist that the file is moved.
    type: bool
    default: no
requirements:
  - an installed Linux system
author:
  - Adam J. Richardson (@FatmanUK)
extends_documentation_fragment:
    - action_common_attributes
attributes:
    check_mode:
        support: full
    diff_mode:
        support: full
    platform:
        support: full
        platforms: posix
'''

EXAMPLES = r'''
- name: 'Restore backup file'
  move:
    src: '/etc/my-service-config.bak'
    dest: '/etc/my-service-config'
    force: yes
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

    # fail if already present
    # change if copied

    res_args = dict(
        warnings=warnings,
        changed=changed
    )

    module.exit_json(**res_args)

if __name__ == '__main__':
    main()

## Technique only works when source and dest are on the same partition.
## Guaranteed to be the case here.
#- name: 'Restore original resolv.conf file'
#  when: 'rg_add_resolver.changed'
#  become: yes
#  file:
#    src: '{{ rg_add_resolver.backup }}'
#    dest: '/etc/resolv.conf'
#    force: yes
#
#- name: 'Remove modified resolv.conf file'
#  when: 'rg_add_resolver.changed'
#  become: yes
#  file:
#    path: '{{ rg_add_resolver.backup }}'
#    state: 'absent'
#
#
#- name: 'Restore backup resolv.conf file'
#  when: 'rg_add_resolver.changed'
#  become: yes
#  move:
#    src: '{{ rg_add_resolver.backup }}'
#    dest: '/etc/resolv.conf'
#    insist: yes

