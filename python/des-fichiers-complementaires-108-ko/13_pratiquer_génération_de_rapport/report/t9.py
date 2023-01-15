from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

Page_Largeur, Page_Hauteur = A4

Titre = "Une table avec ReportLab"

from faker import Faker
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

ts = datetime.datetime.now().strftime("%x a %X")

def set_doc():
    doc = SimpleDocTemplate("t9.pdf", 
				pagesize=A4,
				rightMargin=2*cm,
				leftMargin=2*cm,
				topMargin=2*cm,bottomMargin=2*cm)
    return doc

def set_data():
    fake = Faker('fr_FR')
    data = []
    # Entete
    row = []
    row.append("No")
    row.append("Nom")
    row.append("Adresse")
    row.append("Tél + Email")
    data.append(row)

    for i in range(200):
        row = []
        row.append(i+1)
        row.append( fake.name() )
        row.append( fake.address() )
        row.append( fake.phone_number() +'\n'+ fake.ascii_email())
        data.append( row )

    return data

## Une fonction commune a toute les pages
def MesPages(canvas, doc):
    canvas.saveState()

    # Affichage du titre
    canvas.setFont('Times-Roman',14)
    canvas.drawCentredString(Page_Largeur/2, 
				Page_Hauteur-1*cm, Titre)
    canvas.drawCentredString(Page_Largeur/2, 
				Page_Hauteur-1*cm, "_"*len(Titre))

    # Affichage des numeros de pages
    canvas.setFont('Times-Roman',9)
    canvas.drawString(1*cm, 1*cm, "Page N° %d " % doc.page)
    canvas.drawString(15*cm, 1*cm, "Edite le %s" % ts)

    canvas.restoreState()
  
def run():
    doc = set_doc()

    elements = []
      
    data = set_data()
      




    style = TableStyle([ 
               ('BACKGROUND',(0,0),(-1,0),colors.grey),
               ('VALIGN',(0,0),(-1,-1),'TOP'),
               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ])

    t=Table(data)
    t.setStyle(style)
      
    #On ajoute la table dans les elements
    elements.append(t)

    # On construit le document 
    doc.build(elements, onFirstPage=MesPages,
				 onLaterPages=MesPages)

if __name__ == "__main__":
    run()
