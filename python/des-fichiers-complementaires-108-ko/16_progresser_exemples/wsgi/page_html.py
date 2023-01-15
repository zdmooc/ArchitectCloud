from jinja2 import Environment, FileSystemLoader
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

from path import Path
from humanfriendly import format_size

import configparser as cp

## Les parametres
params = cp.ConfigParser()
params.read("params.ini")

## Quelques parametres
TMPL_DIR = params.get("PARAMETRES",'TMPL_DIR')
DATA_DIR = params.get("PARAMETRES",'DATA_DIR')
FIC_DESC = params.get("PARAMETRES",'FIC_DESC')
BASE_DOWNLOAD = params.get("PARAMETRES", 'BASE_DOWNLOAD')
HOME = params.get("PARAMETRES",'HOME')

if BASE_DOWNLOAD == '':
    BASE_DOWNLOAD = '/'+DATA_DIR

desc_fichiers = cp.ConfigParser()
desc_fichiers.read(FIC_DESC)

templateLoader = FileSystemLoader(searchpath=TMPL_DIR)
templateEnv = Environment(loader=templateLoader)

DOWNLOAD = chr(8659)
DOWNLOAD = "Télécharger"

## Récupération des informations sur les fichiers 
def get_info(fichier):
    try:
        desc = desc_fichiers.get(str(fichier.relpath(start=DATA_DIR)), 'description')
    except:
        desc = ''
    return desc

## Construction de la breadcrum
def make_breadcrum( chemin ):
    breadcrum = '''<nav aria-label="breadcrumb">
                  <ol class="breadcrumb">
                  '''
    p = Path(chemin)
    bc = ''
    for n in p.splitall()[1:]:
        if n == DATA_DIR:
            bc += '/'+n
            n = HOME
            nav = '<li class="breadcrumb-item"><a href="%s">%s</a></li>' % ( bc, n )
        else:
            bc += '/'+n
            nav = '<li class="breadcrumb-item"><a href="%s">%s</a></li>' % ( bc, n )
        #print(n, bc)
        breadcrum += nav +'\n'
    breadcrum += ''' </ol> </nav> '''
    return breadcrum


## on recupere les répertoires
def get_dirs(rep):
    p = Path(rep)
    return sorted(list(p.dirs()))

def get_files(rep):
    p = Path(rep)
    l = [ f for f in p.files() if not f.name.startswith('.') ]
    return sorted(l)

def get_page( env ):
    URI = env['REQUEST_URI']
    if URI == '/':
        URI = '/'+DATA_DIR
    URI = URI[1:]
    ## Ici tester si on pointe sur un fichier et dans ce cas renvoyer le fichier
    ## Les répertoires
    repertoires = []
    for r in get_dirs(URI):
        mod_date = datetime.datetime.fromtimestamp(r.getmtime())
        r1 = {  'nom':'<a href="%s">%s</a>' % ( '/'+str(r.relpath()), str(r.name)), 
                'date' :  mod_date.strftime("%d %B %Y à %X"),
                'info' : get_info( r ) 
            }
        repertoires.append(r1)

    ## Les fichiers
    fichiers = []
    for f in get_files(URI):
        f_name = f.name
        f_dir  = f.parent.split('/')[1:]
        f_dir.append(str(f.name))
        f_lnk  = "/".join(f_dir)
        dl_lnk = BASE_DOWNLOAD+'/'+f_lnk
        mod_date = datetime.datetime.fromtimestamp(f.getmtime())
        f1 = {  'nom' : str(f.name), 
                'download':'<a href="%s" class="badge badge-pill badge-primary">%s</a>' % (dl_lnk, DOWNLOAD), 
                'size' : format_size(f.size),
                'date' :  mod_date.strftime("%d %B %Y à %X"),
                'info': get_info( f )
               }
        fichiers.append(f1)

    ## Somme des infos
    page_data = { 
            'time_stamp':datetime.datetime.now().strftime("%x %X"),
            'fichiers' : fichiers,
            'rep' : repertoires,
            'breadcrum' : make_breadcrum(URI)
            }
    fichier = "index"
    template = templateEnv.get_template(fichier+".jinja")
    page = template.render( data=page_data )
    return page

## Pour test
def get_page_t( env ):
    page = "Hello World" + '\n'
    page += '<br/>'
    page += ' Répertoire = %s ' % env['REQUEST_URI'] + '\n'
    page += '<br/>'
    return page

if __name__ == '__main__':
    p = get_page( { 'REQUEST_URI' : '/' })
    #p = make_breadcrum( '/data/dolores' )
    print(p)
