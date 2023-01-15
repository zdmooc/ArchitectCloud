import tarfile
from pathlib import Path

fichier='test.tgz'
a_sauver = 'test'

p = Path(a_sauver)

with tarfile.open(fichier, "w:gz") as tar:
    for name in p.iterdir():
        print(name)
        tar.add(name)
