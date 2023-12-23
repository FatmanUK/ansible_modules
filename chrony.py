# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Adam J. Richardson <fatman.uk@gmail.com>

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: 'chrony'
short_description: 'Manipulate chronyd via the chronyc command.'
description:
  - 'Manipulate various functions of the chrony daemon via the chronyc
    command.'
version_added: '0.1'
options:
  mode:
    description:
      - 'The mode in which to execute.'
      - 'Current modes: make_step, tracking.'
    type: 'str'
    required: yes
requirements:
  - 'installed Linux system'
  - 'chronyd/chronyc'
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
- name: 'Step system clock'
  chrony:
    mode: 'make_step'

- name: 'Get tracking data'
  chrony:
    mode: 'tracking'
'''

# TODO: add to this value, especially mode: tracking
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

    # TODO: should this be split into chrony_makestep and chrony_tracking? Maybe.
    mode = module.params['mode']

    chronyc_argv = [ '/usr/bin/chronyc' ]
    failmsg = 'Failed to '

    if mode == 'make_step':
        chrony_argv.append([ 'make_step' ])
        failmsg += 'step chronyd'

    if mode == 'tracking':
        chrony_argv.append([ 'tracking' ])
        failmsg += 'obtain tracking data'

    rc, out, err = self.module.run_command(chronyc_argv, environ_update=self.LANG_ENV)
    if rc != 0 or self._stderr_failed(err):
        self.module.fail_json(msg="%s: %s" % (failmsg, to_native(out) + to_native(err)))

    if mode == 'tracking':
        x=1
        # TODO: process output

    res_args = dict(
        warnings=warnings,
        changed=changed
    )

    module.exit_json(**res_args)

if __name__ == '__main__':
    main()

