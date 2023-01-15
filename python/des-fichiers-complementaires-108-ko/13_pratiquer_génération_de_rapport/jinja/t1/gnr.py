from jinja2 import Environment, FileSystemLoader
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

TMPL_DIR = "tmpl"

templateLoader = FileSystemLoader(searchpath=TMPL_DIR)
templateEnv = Environment(loader=templateLoader)

data={
        'time_stamp':datetime.datetime.now().strftime("%x %X")
    }


fichiers = [ "index", "about" ]

for fichier in fichiers:
    template = templateEnv.get_template(fichier+".jinja")
    page = template.render( data )
    with open( fichier+".html", "w") as f:
        print("Writing : %s " % fichier)
        f.write(page)

