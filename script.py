import os
import subprocess

path_env = ':'.join([i for i in os.listdir('.') if os.path.isdir(i)]) 

with open("xpath-dump.txt", "wb") as fp:
  for dir in os.listdir('.'):
    if os.path.isdir(dir):
       if dir in ["plugins"]:
           continue
       cmd = "pyang --plugindir plugins --path {} -f xpath {}/openconfig-*".format(path_env, dir)
       op = subprocess.check_output(cmd, shell=True)
       fp.write(op)
