#!/bin/env python3

# Test with: $ ./archived_checksum.py <test_inputs/_archived_checksum.json
# Believe it or not, it works great! :)
# Insanely, ansible will try to use the test data as a module if you remove the initial underscore from the filename. :|

DOCUMENTATION = r'''
---
module: 'archived_checksum'
short_description: 'Get checksum of an archived file'
description:
  - 'Get the checksum of an archived file.'
version_added: '0.1'
options:
  path:
    description:
      - 'The path of the tarball to inspect.'
    type: 'str'
    required: yes
  archived_file:
    description:
      - 'The file within the tarball.'
      - 'Looks for the file with the tar command.'
    type: 'str'
    required: yes
  checksum_type:
    description:
      - 'Type of checksum to generate.'
      - 'See man cksum.'
    type: 'str'
    choices: [ 'bsd', 'sysv', 'crc', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b', 'sm3' ]
    default: 'sha256'
  checksum_executable:
    description:
      - 'Checksum generation executable.'
      - 'Overrides type.'
    type: 'str'
    default: '/usr/bin/cksum'
  checksum_flags:
    description:
      - 'Checksum generation flags.'
    type: 'str'
    default: '-a sha256 -z --untagged'
requirements:
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
...
'''

EXAMPLES = r'''
---
- name: 'Get sha256 checksum from tarballed file'
  archived_checksum:
    path: 'the_tarball.tgz'
    archived_file: 'the_file.txt'
...
'''

# TODO: What should go in the RETURN string?
RETURN = r'''#'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
from os import unlink
from os.path import exists

def is_stderr_failed(err):
    # A command can fail to set a value even if it returns an exit
    # status 0. That's why we also have to check stderr for errors.
    #errors_regex = r'^sysctl: setting key "[^"]+": (Invalid argument|Read-only file system)$'
    #return search(errors_regex, err, re.MULTILINE) is not None
    return False  # TODO: this function

def has_ancient_cksum():
    # v<9.0
    #ver_argv = []
    # TODO: finish this
    #rc, out, err = module.run_command(untar_argv)
    return True

def delete_my_file(my_file):
    try:
        unlink(my_file)
    except:
        # Well, it's not there, so job done I guess. Just return.
        # Why is this not here? What deletes it?
        return

def main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True),
            archived_file=dict(type='str', required=True),
            checksum_type=dict(type='str', choices=[ 'bsd', 'sysv', 'crc', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b', 'sm3' ], default='sha256'),
            checksum_executable=dict(type='str', default='/usr/bin/cksum'),
            checksum_flags=dict(type='str', default='-a sha256 -z --untagged'),
        ),
        supports_check_mode=False,
    )

    _path = module.params['path']
    _file = module.params['archived_file']
    _type = module.params['checksum_type']
    _exe = module.params['checksum_executable']
    _flags = module.params['checksum_flags']

    _flags = _flags.replace('sha256', _type)

    temppath = '/dev/shm'
    tempfile = f'{temppath}/{_file}'

    changed = False  # doesn't change anything ever
    warnings = list()
    res_args = dict()

    untar_argv = [
        '/usr/bin/tar',
        'xzf',
        _path,
        '-C',
        temppath,
        _file,
    ]

    # print(untar_argv)
    rc, out, err = module.run_command(untar_argv)

    if rc != 0 or is_stderr_failed(err):
        module.fail_json(msg="Failed to untar: %s" % to_native(out) + to_native(err))
    else:
        # make sure we have cksum, otherwise this will fail spectacularly
        if (not exists('/usr/bin/cksum')) or has_ancient_cksum():
            _exe = '/bin/sha256sum'
            _flags = ''

        # do "env cksum" instead of specifying path?
        cksum_argv = [ _exe ]
        if _flags != '':
            cksum_argv.append(_flags.split(' '))
        cksum_argv.append(tempfile)

        rc, out, err = module.run_command(cksum_argv)

        if rc != 0 or is_stderr_failed(err):
            module.fail_json(msg="Failed to get checksum: %s" % to_native(out) + to_native(err))

        res_args['stdout'] = out
        res_args['rc'] = rc
        res_args['checksum'] = out.split(' ')[0]

    delete_my_file(tempfile)

    res_args['changed']=changed
    res_args['warnings']=warnings

    module.exit_json(**res_args)

if __name__ == '__main__':
    main()

