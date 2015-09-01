#!/usr/bin/env python

"""
Like sshpass for:
ssh -2 -o StrictHostKeyChecking=no -i omerovmkey -p 2222 -t omero@localhost
"""

with open("omerovmkey.pub") as f:
	txt = f.read().strip()

import pxssh
try:
    #s = pxssh.pxssh(options={"StrictHostKeyChecking": "no"})
    s = pxssh.pxssh()
    hostname = "localhost"
    username = "omero"
    password = "omero"
    s.login(hostname, username, password, port=2222)
    s.sendline('echo "%s" > ~/.ssh/authorized_keys' % txt)
    s.prompt()             # match the prompt
    print(s.before)        # print everything before the prompt.
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
