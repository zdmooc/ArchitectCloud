

with open('/etc/passwd') as f:
    for l in f:
        user, pswd, id_u, id_g, comment, home, shell = l.split(':')
        print( "USER    = %s" % utilisateur )
        print( "UID     = %s" % id_util )
        print( "GID     = %s" % id_groupe )
        print( "COMMENT = %s" % commentaire )
        print( "HOME    = %s" % home )
        print( "SHELL   = %s" % shell )
