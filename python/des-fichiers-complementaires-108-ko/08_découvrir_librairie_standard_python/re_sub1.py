import path
from path import Path 
import re

with path.TempDir() as dir_base:

    fichier = Path(dir_base) / 'fichier1'

    ## génération d'un fichier avec des numeros de lignes
    ligs = []
    for n in range(995,1005):
        ligs.append( '{0:03d} Ligne no {0:3d}\n'.format(n) )
    fichier.write_lines(ligs)

    print("AVANT MODIF")
    print(fichier.text())

    
    ## Modifions les numeros de lignes 
    p = Path(dir_base) / 'fichier1'
    assert p.isfile()
    with p.in_place() as (reader, writer):
        for n, lig in enumerate(reader, 995):
            num = '{0:05d}:'.format(n)
            lig = re.sub(r"^\d{3,4}", num, lig)
            writer.write(lig)

    print("APRES MODIF")
    print(p.text())
