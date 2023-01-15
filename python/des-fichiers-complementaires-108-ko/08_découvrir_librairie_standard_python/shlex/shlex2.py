import shlex

def interprete(ligne):
    s = shlex.shlex(ligne, posix=False, punctuation_chars=False)
    s.whitespace_split = False
    cmd = arg = temps = ""
    cmd = s.get_token()
    if cmd == "create":
        arg = s.get_token()
        temps = s.get_token()
    elif cmd == "list":
        pass
    elif cmd == "kill":
        arg = s.get_token()
    else:
        cmd = "Error ..."
    print("cmd=%s arg=%s temps=%s" % (cmd, arg, temps))


while True:
    ligne = input("Tapez une chaine a interpreter :")
    interprete(ligne)
