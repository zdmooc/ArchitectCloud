import pexpect
import datetime

serveur = "X.X.X.X"
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
for fic in [ 'help', 'info', 'install' ]:
    child.sendline ('get %s' % fic)
    child.expect ('ftp> ')
for fic in [ 'prnlog', 'stat', 'syslog' ]:
    fic_ts = fic+"_"+datetime.datetime.now().strftime('%Y%m%d_%H%M%S') 
    child.sendline ('get %s %s' % (fic, fic_ts))
    child.expect ('ftp> ')

child.sendline ('quit')


#-r--r--r-- root root 200 Jan  1 01:08 help
#-r--r--r-- root root 200 Jan  1 01:08 info
#-r--r--r-- root root 200 Jan  1 01:08 install
#-r--r--r-- root root 200 Jan  1 01:08 prnlog
#-r--r--r-- root root 200 Jan  1 01:08 stat
#-r--r--r-- root root 200 Jan  1 01:08 syslog

