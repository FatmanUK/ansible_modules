# -*- coding: utf-8 -*-

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

#- name: 'Update libguestfs appliance'
#  command:
#    argv:
#      - '/usr/bin/update-libguestfs-appliance'
#
#- name: 'Update libguestfs appliance'
##  command:
##    argv:
##      - '/usr/bin/update-libguestfs-appliance'
#  libguestfs:
#    mode: 'update_appliance'

