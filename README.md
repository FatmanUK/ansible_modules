# ansible_modules

## ansible_vault

Perform some Ansible Vault operations.

### mode: encrypt

Encrypt a file. Requires src, dest.

## chrony

Perform some chrony operations.

### mode: make_step

Do a chronyc make_step.

### mode: tracking

Do a chronyc tracking. Return the data in a useful form.

## sysctl_reload

Simply reload the sysctl settings from /etc/sysctl.conf.

## hwclock

Synchronise the hardware clock and (operating) system clock.

## localedef

Define missing locales.

### locale

The locale to generate. Must be specified.

### charmap

Character map to use. Default: 'UTF-8'

### path

Output path for the locale including filename. Default: '/usr/lib64/locale/<locale>.<charmap>'

  - '/usr/bin/localedef'

### Examples
- name: 'Create en-GB.UTF-8 locale'
  localedef:
    locale: 'en_GB'

- name: 'Create en-GB.ACSII locale in /tmp for no reason'
  localedef:
    locale: 'en_GB'
    charmap: 'ASCII'
    path: '/tmp/en_GB.ASCII'
