import pexpect
import os
import sys
from sparrow6lib import *

qemu_args = [
  '-nographic',
  '-m', '512M',
  '-smp', '4',
]

img = config()['iso-file']
disktype = "ide"
qemu_args.extend(['-drive', f'if={disktype},format=raw,file={img}'])

p = pexpect.spawn("qemu-system-x86_64", qemu_args)

p.logfile = sys.stdout.buffer

p.expect("login:", timeout=30)
p.sendline("root")

p.timeout = 2
p.expect("localhost:~#")
p.sendline("pwd")
p.sendline("apk update")
p.sendline("apk add openssh")
p.sendline("apk info openssh")
p.sendline("poweroff")
p.expect(pexpect.EOF, timeout=10)
