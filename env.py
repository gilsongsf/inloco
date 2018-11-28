#!/usr/bin/python
import sys
import yaml
#env=sys.argv[1]
f=open('envs.yml')
envs=yaml.load(f)

print(envs)
print(f)
#hosts=envs['envs'][env]['hosts']
#for host in hosts: print host