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

#- name: 'Kill async process'
#  register: 'rg_kill_async'
#  shell:
#    cmd: '/bin/kill $(/usr/bin/more {{ iptables_check_pidfile }})'
#
#  kill_pidfile:
#    path: '{{ iptables_check_pidfile }}'
#
#
#
#- name: 'Read pid file'
#  when: 'repository_file is exists'
#  register: 'server'
#  slurp:
#    path: '{{ repository_file }}'
#
#- name: 'Kill pid'
#  when: 'server is not skipped'
#  failed_when: False
#  command:
#    argv:
#      - '/bin/kill'
#      - '{{ server.content | b64decode }}'
#
#
#
#- name: 'Kill process from pidfile'
#  kill_pidfile:
#    path: '{{ iptables_check_pidfile }}'
#    delete: yes
#
#- name: 'Delete pid file'
#  file:
#    state: 'absent'
#    path: '{{ repository_file }}'
#
#
#
#- name: 'Kill process from pidfile'
#  when: 'repository_file is exists'
#  kill_pidfile:
#    path: '{{ repository_file }}'
#    delete_pidfile: yes

