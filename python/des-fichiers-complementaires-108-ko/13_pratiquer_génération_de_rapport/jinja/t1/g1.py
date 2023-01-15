from jinja2 import Environment, FileSystemLoader

## Necessaire pour les dates en français
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

TMPL_DIR = "tmpl"
fichier = "index.jinja"

templateLoader = FileSystemLoader(searchpath=TMPL_DIR)
templateEnv = Environment(loader=templateLoader)
template = templateEnv.get_template(fichier)

data={
        'time_stamp':datetime.datetime.now().strftime("%x %X")
    }

print( template.render( data ) )
