from odf.opendocument import OpenDocumentText
from odf.style import PageLayout, PageLayoutProperties, MasterPage, Header, Footer
from odf.style import Style, TextProperties
from odf.text import H, P, Span
from odf.table import Table, TableRow, TableCell, TableColumn

from fake_contact import fake_contact

from faker import Faker 
fake = Faker('fr_FR')


textdoc = OpenDocumentText()

pl = PageLayout(name="pagelayout")
pl.addElement(
            PageLayoutProperties(
                pagewidth="21cm", 
                pageheight="29.7cm", 
                margin="1cm",
                marginbottom='1cm',
                marginleft='1cm',
                marginright='1cm',
                margintop='1cm',
                papertrayname='A4',
                printorientation="portrait"
                )
            )
textdoc.automaticstyles.addElement(pl)

mp = MasterPage(name="Standard", pagelayoutname=pl)
textdoc.masterstyles.addElement(mp)

## Création de Style 
s = textdoc.styles

## Style d'entete
h1style = Style(name="Heading 1", family="paragraph")
h1style.addElement(TextProperties(attributes={'fontfamily':'Arial', 'fontsize':"24pt",'fontweight':"bold" }))
s.addElement(h1style)

# Style de Texte
boldstyle = Style(name="Bold", family="text")
boldprop = TextProperties(fontweight="bold")
boldstyle.addElement(boldprop)
textdoc.automaticstyles.addElement(boldstyle)

ItalicStyle = Style(name="Italic", family="text")
ItalicProp = TextProperties(fontstyle="italic")
ItalicStyle.addElement(ItalicProp)
textdoc.automaticstyles.addElement(ItalicStyle)

# Ajout de texte :
h=H(outlinelevel=1, stylename=h1style, text="Mon Test document ODT ")
textdoc.text.addElement(h)

p = P(text="Le texte peut être : ")
boldpart = Span(stylename=boldstyle, text="en GRAS")
p.addElement(boldpart)
p.addText(" Mais ce n'est pas obligatoire ")
textdoc.text.addElement(p)

p = P(text="Sinon il y a aussi le texte ")
part = Span(stylename=ItalicStyle, text = "en Italique")
p.addElement(part)
textdoc.text.addElement(p)

## Génération de données
data = [ ]
for x in range(0,10):
    data.append( fake_contact() )

# Table 
table = Table()

## Ajout des colonnes
for x in range(0, 4):
    table.addElement(TableColumn())

for n,d,a,t,c in data:
    tr = TableRow()
    ## Nom
    tc = TableCell(valuetype='string')
    tc.addElement(P(text = n ))
    tr.addElement(tc)
    ## Date de naissance
    tc = TableCell(valuetype='string')
    tc.addElement(P(text = d ))
    tr.addElement(tc)
    ## adresse
    tc = TableCell(valuetype='string')
    tc.addElement(P(text = a ))
    tr.addElement(tc)
    ## Telephone
    tc = TableCell(valuetype='string')
    tc.addElement(P(text = t ))
    tr.addElement(tc)
    ## adresse
    tc = TableCell(valuetype='string')
    tc.addElement(P(text = c ))
    tr.addElement(tc)
    table.addElement(tr)

textdoc.text.addElement(table)

textdoc.save("test_document.odt")
