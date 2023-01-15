
import tempfile

data = [ 'ligne 1\n', 'ligne 2\n', 'ligne 3\n' ]

with tempfile.TemporaryFile(mode='w+') as fic:
    fic.writelines( data )
    fic.flush()
    fic.seek(0)
    print(fic.read())

