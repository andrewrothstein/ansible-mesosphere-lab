#!/usr/bin/python

import os
from subprocess import call

github_root = "/home/arothste/git/github/andrewrothstein"
ansible_playbooks_dir = github_root + "/ansible-mesosphere-lab"
ansible_playbooks_roles_dir = ansible_playbooks_dir + "/roles"

addl_files_path = github_root + "/ansible-julia"
addl_files_to_copy = ["LICENSE", "README.md", ".gitignore", "test.yml", "meta/main.yml"]

def create_git_repo(role) :
  print "creating repo for role " + role
  github_repos_dir = "/home/arothste/git/github-target"
  src_role_path = ansible_playbooks_roles_dir + "/" + role
  target_role_name = "ansible-mesosphere-" + role
  target_role_path = github_repos_dir + "/" + target_role_name
  if (not os.path.isdir(target_role_path)):
    print("copying role files from {0} to {1}...".format(src_role_path, target_role_path))
    call(['cp', '-R', src_role_path, target_role_path])
    call(['mkdir', '-p', target_role_path + "/meta"])
    for f in addl_files_to_copy :
      call(['cp', addl_files_path + '/' + f, target_role_path])

    target_role_path_git_dir = target_role_path + "/.git"
    if (not os.path.isdir(target_role_path_git_dir)):
      print("initializing git in {0}...".format(target_role_path))
      os.chdir(target_role_path)
      call(['git', 'init'])
      call(['git', 'add', '.'])
      call(['git', 'commit', '-m', 'initial commit'])
      call(['hub', 'create', target_role_name])
      call(['git', 'push', 'origin', 'master'])

roles = filter(lambda x : not os.path.isdir(x), os.listdir(ansible_playbooks_roles_dir))
map(create_git_repo, roles)
print("roles:", roles)
