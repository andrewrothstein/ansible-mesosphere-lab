#!/usr/bin/env bash
ssh-add -l | fgrep vagrant | awk '{print $2}' | xargs ssh-add -d
vagrant destroy -f
