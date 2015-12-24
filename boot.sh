#!/usr/bin/env bash
vagrant up
vagrant ssh-config | fgrep IdentityFile | awk '{print $2}' | xargs ssh-add
