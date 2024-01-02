# -*- coding: utf-8 -*-

DOCUMENTATION = r'''
---
module: 'sysctl_reload'
short_description: 'Reload sysctl from /etc/sysctl.conf'
description:
  - 'Use this module to reload sysctl config.'
version_added: '0.1'
options:
requirements:
  - 'installed Linux system'
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
- name: 'Reload sysctl configuration'
  sysctl_reload:
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

    sysctl_args = ['/usr/bin/sysctl', '-p']
    rc, out, err = self.module.run_command(sysctl_args, environ_update=self.LANG_ENV)

    if rc != 0 or self._stderr_failed(err):
        self.module.fail_json(msg="Failed to reload sysctl: %s" % to_native(out) + to_native(err))

    res_args = dict(
        warnings=warnings,
        changed=changed
    )

    module.exit_json(**res_args)

if __name__ == '__main__':
    main()
