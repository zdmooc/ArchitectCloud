import subprocess

commande = [ "ls", "-l" ]

cmd = subprocess.run(commande, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("=" * 30 )
print("Commande : %s " % commande )
print("=" * 30 )
print(" return code : %s " % cmd.returncode)
print("=" * 30 )
print(" STDOUT : ")
print(" %s " % cmd.stdout )
print("=" * 30 )
print(" STDERR : ")
print(" %s " % cmd.stderr )
print("=" * 30 )
