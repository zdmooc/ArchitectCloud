
def gener():
    print(" Bonjour on commence  ...     : Avant le 1er yield")
    yield(" C'est parti on est au debut  : 1er yield")
    yield(" La c'est la fin du debut     : 2eme yield")
    yield(" La c'est le milieu           : 3eme yield")
    yield(" C'est le debut de la fin     : 4eme yield")
    yield(" On est presque a la fin      : 5eme yield")
    yield(" Encore une petit peu ...     : 6eme yield")
    print(" The End                      : plus de yield")

for i in gener():
    print(i)

