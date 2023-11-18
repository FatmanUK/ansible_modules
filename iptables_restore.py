# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Adam J. Richardson <fatman.uk@gmail.com>

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: iptables_restore
short_description: Load iptables ruleset via iptables-restore
description:
  - Use this module to load iptables rules.
version_added: "0.1"
options:
  path:
    description:
      - The ruleset file to load.
    type: str
    default: /etc/iptables/iptables.rules
requirements:
  - iptables and iptables-restore
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
- name: Reload iptables ruleset from /etc/iptables/iptables.rules
  iptables_restore:

- name: Reload iptables ruleset from /tmp/test_new_ruleset.rules
  iptables_restore:
    path: "/tmp/test_new_ruleset.rules"
'''

RETURN = r'''#'''

#import os
#import platform
#import pwd
#import re
#import sys
#import tempfile

from ansible.module_utils.basic import AnsibleModule
#from ansible.module_utils.common.text.converters import to_bytes, to_native
#from ansible.module_utils.six.moves import shlex_quote

def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', default='/etc/iptables/iptables.rules'),
        ),
        supports_check_mode=True,
    )
    path = module.params['path']

    changed = False
    failed = False
    res_args = dict()
    warnings = list()

    iptables_args = ['/usr/bin/iptables-restore', path]
    rc, out, err = self.module.run_command(sysctl_args, environ_update=self.LANG_ENV)

    if rc != 0 or self._stderr_failed(err):
        self.module.fail_json(msg="Failed to reload sysctl: %s" % to_native(out) + to_native(err))

    res_args = dict(
        warnings=warnings,
        changed=changed,
        failed=failed
    )

    res_args['path'] = path

    module.exit_json(**res_args)

if __name__ == '__main__':
    main()

#- name: 'Reload iptables'
#  iptables_restore:
#
##- name: 'Reload iptables'
##  register: 'iptables_reload_handler_result'
##  changed_when:
##    - 'iptables_reload_handler_result.rc is defined'
##    - 'iptables_reload_handler_result.rc == 0'
##  failed_when:
##    - 'iptables_reload_handler_result.rc is defined'
##    - 'iptables_reload_handler_result.rc > 0'
##  become: yes
##  command:
##    argv:
##      - '/sbin/iptables-restore'
##      - '/etc/iptables/iptables.rules'

