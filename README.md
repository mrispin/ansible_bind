Ansible: bind
============

[![Build Status](https://travis-ci.org/mrispin/ansible_bind.svg?branch=master)](https://travis-ci.org/mrispin/ansible_bind)

This role installs bind9

Requirements
------------

None

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

    bind_enable_caching: true

Enable use as a caching server. 

    bind_forwarders:
      - 8.8.8.8
      - 8.8.4.4

The servers to resolve requests for domains that this server is not administrative for.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: mrispin.bind }

License
-------

GPLv3
