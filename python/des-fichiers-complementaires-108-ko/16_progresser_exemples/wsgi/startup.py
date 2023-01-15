import os
import sys
import bottle
from path import Path

import configparser as cp

## Les parametres
params = cp.ConfigParser()
params.read("params.ini")

## Quelques parametres
DATA_DIR = params.get("PARAMETRES",'DATA_DIR')

import page_html

sys.path.insert(0, os.path.dirname(__file__))

@bottle.route('/'+DATA_DIR+'/<filename:path>')
def autres_routes(filename):
    p = Path(DATA_DIR+'/'+filename)
    print(p)
    if p.isdir():
        env = { 'REQUEST_URI' :  '/'+DATA_DIR+'/'+filename }
        page = page_html.get_page( env )
        return page
    else:
        return bottle.static_file(filename, root=DATA_DIR, mimetype='application/octet-stream', download=True)

@bottle.route('/')
@bottle.route('/'+DATA_DIR)
def home():
    env = { 'REQUEST_URI' : '/' }
    page = page_html.get_page( env )
    return page

application = bottle.default_app()
