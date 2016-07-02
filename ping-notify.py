#!/usr/bin/env python
import subprocess
import shlex
import time
import sys
import os

__author__ = 'Blayne Campbell'
__date__ = '2016-07-01'

audio_file = '/usr/share/sounds/freedesktop/stereo/complete.oga'

if len(sys.argv) <= 1:
    print("Please provide one or more hosts (hostname or ip)")
    print("Usage: %s <ip1> <ip2> <ip3> ..." % sys.argv[0])
    sys.exit()

hostlist = sys.argv[1:]

while len(hostlist):
    for ip in hostlist:
        command = "ping -c1 %s" % ip
        check = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        check.wait()
        if check.returncode == 0:
            print('%s: success' % ip)
            subprocess.call(shlex.split('notify-send "%s: Ping Success"' % ip))
            subprocess.call(shlex.split('paplay %s' % audio_file))
            hostlist.remove(ip)
    if len(hostlist):
        time.sleep(10)

print('Complete. All hosts have responded')
