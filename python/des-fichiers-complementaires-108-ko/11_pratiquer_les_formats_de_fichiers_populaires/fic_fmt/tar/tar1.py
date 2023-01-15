import tarfile
fichier = "test.tgz"
fmt = "|{name:30s}|{size:10s}|{typ:20s}|"
tar = tarfile.open(fichier, "r:gz")
total = 0

## Entete
info = { 'name': 'Fichier ', 'size': 'Taille', 'typ' : 'Type' }
t = len(fmt.format(**info))
print("-" * t)
print(fmt.format(**info))
print("-" * t)

## pour toutes les entrées de l'archive
fmt = "|{name:30s}|{size:10d}|{typ:20s}|"
for tarinfo in tar:
    info = tarinfo.get_info()
    total += info['size']
    #print(info)
    if tarinfo.isreg():
        info['typ'] = "Fichier"
    elif tarinfo.isdir():
        info['typ'] = "Repertoire"
    else:
        info['typ'] = "Autre"
    print(fmt.format(**info))
tar.close()

info = {
        'name': 'Total ',
        'size': total,
        'typ' : ''
        }
print("-" * t)
print(fmt.format(**info))
print("-" * t)
