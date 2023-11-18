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

## Can throw a wobbler if you don't do this first
#- name: 'Update xbps package'
#  register: 'rg_update_xbps'
#  vars:
#    e_already: "Package 'xbps' is up to date"
#  changed_when:
#    - 'rg_update_xbps.rc == 0'
#    - 'e_already not in rg_update_xbps.stdout'
#  become: yes
#  command:
#    argv:
#      - 'xbps-install'
#      - '-Suy'
#      - 'xbps'
#
#- name: 'Install packages'
#  register: 'rg_install'
#  vars:
#    e_already: 'already installed'
#    prefix:
#      - '/usr/bin/xbps-install'
#      - '-Sy'
#  notify: '{{ packages_notifies }}'
#  become: yes
#  changed_when:
#    - 'rg_install.rc == 0'
#    - 'e_already not in rg_install.stdout'
#  failed_when:
#    - 'rg_install.rc > 0'
#    - 'e_already not in rg_install.stdout'
#  command:  # for efficiency
#    argv: '{{ prefix + packages }}'
#
#
#- name: 'Install packages'
#  register: 'rg_install'
#  become: yes
#  vars:
#    e_already: 'already installed'
#  notify: '{{ packages_notifies }}'
#  changed_when:
#    - 'rg_install.rc == 0'
#    - 'e_already not in rg_install.stdout'
#  failed_when:
#    - 'rg_install.rc > 0'
#    - 'e_already not in rg_install.stdout'
#  xbps_uncommon:
#    packages: '{{ packages }}'
#
#
#- name: 'Download packages'
#  register: 'xbps_prepare_download'
#  when: 'download_enabled'
#  until: 'xbps_prepare_download is not failed'  # poor workaround, but why does this fail? standard wisdom is "flaky network", but I don't buy that for a second
#  retries: 300
#  environment:
#    XBPS_TARGET_ARCH: '{{ xbps_static_arch }}'
#    XBPS_ARCH: '{{ xbps_static_arch }}'
#  vars:
#    cmd_argv:
#      - '{{ xbps_static_binary_path }}/xbps-install.static'
#      - '-SyDR'
#      - '{{ xbps_static_repository }}'
#      - '-r'
#      - '{{ repository_root }}'
#  command:
#    argv: '{{ cmd_argv + xbps_package_download }}'
#
#
#- name: 'Download packages'
#  register: 'xbps_prepare_download'
#  when: 'download_enabled'
#  until: 'xbps_prepare_download is not failed'  # poor workaround, but why does this fail? standard wisdom is "flaky network", but I don't buy that for a second
#  retries: 300
#  xbps_uncommon:
#    binary_path: '{{ xbps_static_binary_path }}'
#    arch: '{{ xbps_static_arch }}'
#    packages: '{{ xbps_package_download }}'
#    download_only: yes
#    remote_repository:
#      - '{{ xbps_static_repository }}'
#    root_dir: '{{ repository_root }}'
#
#
#- name: 'Create new index'
#  when: 'downloads is defined'
#  vars:
#    cmd_argv:
#      - '{{ xbps_static_binary_path }}/xbps-rindex.static'
#      - '-a'
#  failed_when: '"index: failed to read props.plist metadata" in rindex.stderr'
#  register: 'rindex'
#  command:
#    argv: '{{ cmd_argv +  downloads }}'
#
#- name: 'Sign the index'
#  when: 'downloads is defined'
#  command:
#    argv:
#      - '{{ xbps_static_binary_path }}/xbps-rindex.static'
#      - '--sign'
#      - '--signedby'
#      - '{{ xbps_static_byline }}'
#      - '--privkey'
#      - '{{ xbps_static_pem_path }}/{{ xbps_static_pem_key }}'
#      - '{{ xbps_static_cache_path }}'
#
#- name: 'Sign the packages'
#  when: 'downloads is defined'
#  vars:
#    cmd_argv:
#      - '{{ xbps_static_binary_path }}/xbps-rindex.static'
#      - '--sign-pkg'
#      - '--privkey'
#      - '{{ xbps_static_pem_path }}/{{ xbps_static_pem_key }}'
#      # failed_when: '"index: failed to read props.plist metadata"
#      # in rindex-sign.stderr'
#      # register: 'rindex-sign'
#  command:
#    argv: '{{ cmd_argv +  downloads }}'
#
#
#- name: 'Build a new package index'
#  register: 'rindex'
#  when: 'downloads is defined'
#  vars:
#    e_read_metadata: 'index: failed to read props.plist metadata'
#  failed_when:
#    - 'e_read_metadata in rindex.stderr'
#  xbps_uncommon:
#    binary_path: '{{ xbps_static_binary_path }}'
#    arch: '{{ xbps_static_arch }}'
#    packages: '{{ downloads }}'
#    create_new_index: yes
#    #root_dir: '{{ repository_root }}'
#    cache_path: '{{ xbps_static_cache_path }}'
#    signed_by: '{{ xbps_static_byline }}'
#    privkey: '{{ xbps_static_pem_path }}/{{ xbps_static_pem_key }}'
#
#
#- name: 'Check hex key'
#  when: 'downloads is defined'
#  register: 'hexkey'
#  command:
#    argv:
#      - '{{ xbps_static_binary_path }}/xbps-query.static'
#      - '--repository={{ xbps_static_cache_path }}'
#      - '-vL'
#
#- name: 'Check hex key'
#  when: 'downloads is defined'
#  register: 'hexkey'
#  xbps_uncommon:
#    binary_path: '{{ xbps_static_binary_path }}'
#    cache_path: '{{ xbps_static_cache_path }}'
#    list_repos: yes

