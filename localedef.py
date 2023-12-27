# -*- coding: utf-8 -*-

DOCUMENTATION = r'''
---
module: 'localedef'
short_description: 'Define missing locales.'
description:
  - 'Define missing locales.'
version_added: '0.1'
options:
  locale:
    description:
      - 'The locale to generate.'
    type: 'str'
    required: yes
  charmap:
    description:
      - 'Character map to use (default: UTF-8).'
    type: 'str'
    required: no
  path:
    description:
      - 'Output path for the locale including filename (default:'
        ' /usr/lib64/locale/<locale>.<charmap>).'
    type: 'str'
    required: no
requirements:
  - '/usr/bin/localedef'
  - '/usr/bin/ansible'
author:
  - 'Adam J. Richardson (@Fatman@twit.social)'
extends_documentation_fragment:
    - 'action_common_attributes'
attributes:
    check_mode:
        support: 'none'
    diff_mode:
        support: 'none'
    platform:
        support: 'full'
        platforms: 'posix'
'''

EXAMPLES = r'''
# Define a missing locale.
- name: 'Create en-GB.UTF-8 locale'
  localedef:
    locale: 'en_GB'

# Define a missing locale.
- name: 'Create en-GB.ACSII locale in /tmp for no reason'
  localedef:
    locale: 'en_GB'
    charmap: 'ASCII'
    path: '/tmp/en_GB.ASCII'
'''

RETURN = r'''#'''

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            locale = dict(
                required=True
            ),
            charmap = dict(
                required=False,
                default='UTF-8'
            ),
            path = dict(
                required=False
            )
        ),
        supports_check_mode=True,
    )

    changed = True
    res_args = dict()
    warnings = list()

    locale = module.params['locale']
    charmap = module.params['charmap']
    path = module.params['path']

    default_path = '/usr/lib64/locale'

    if path == None:
        path = f'{default_path}/{locale}.{charmap}'

    localedef_argv = [
        '/usr/bin/localedef',
        '-f',
        charmap,
        '-i',
        locale,
        path
    ]

    rc, out, err = self.module.run_command(localedef_argv, environ_update=self.LANG_ENV)
    if rc != 0 or self._stderr_failed(err):
        outerr = to_native(out) + to_native(err)
        self.module.fail_json(msg=f'{failmsg}: {outerr}')

    res_args = dict(
        warnings=warnings,
        changed=changed
    )

    module.exit_json(**res_args)

if __name__ == '__main__':
    main()

