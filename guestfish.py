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

#- name: 'Inject SSH and network settings'
#  connection: 'local'
#  command:
#    argv:
#      - '/bin/guestfish'
#      - '-f'
#      - '/tmp/{{ inventory_hostname }}-guestfish.txt'
#
#- name: 'Inject SSH and network settings'
#  connection: 'local'
#  guestfish:
#    script: '/tmp/{{ inventory_hostname }}-guestfish.txt'

