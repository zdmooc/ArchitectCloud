import pexpect
serveur = "speedtest.tele2.net"
username = "anonymous"
password = "root@exemple.com"

child = pexpect.spawn ('ftp %s' % serveur)
child.expect ('Name .*: ')
child.sendline (username)
child.expect ('Password:')
child.sendline (password)
child.expect ('ftp> ')
child.sendline ('ls -l')
child.expect ('ftp> ')
print(child.before)   # Print the result of the ls command.
#child.interact()     # Give control of the child to the user.
child.sendline ('quit')
