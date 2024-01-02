# -*- coding: utf-8 -*-

DOCUMENTATION = r'''
---
module: 'hwclock'
short_description: 'Manipulate the hardware clock.'
description:
  - 'Manipulate various functions of the hardware clock.'
version_added: '0.1'
options:
  mode:
    description:
      - 'The mode in which to execute.'
      - 'Current modes: systohc.'
    type: 'str'
    required: yes
requirements:
  - '/usr/bin/ansible'
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
- name: 'Sync hardware clock'
  hwclock:
    mode: 'systohc'
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

    # TODO: when more functions crop up, split into hwclock_hcfromsys and so on?
    # TODO: add 'required' knob

    hwclock_argv = [ '/usr/bin/hwclock', '--systohc' ]
    rc, out, err = self.module.run_command(hwclock_argv, environ_update=self.LANG_ENV)

    if rc != 0 or self._stderr_failed(err):
        self.module.fail_json(msg="Failed to synchronise system and hardware clocks: %s" % to_native(out) + to_native(err))

    res_args = dict(
        warnings=warnings,
        changed=changed
    )

    module.exit_json(**res_args)

if __name__ == '__main__':
    main()

