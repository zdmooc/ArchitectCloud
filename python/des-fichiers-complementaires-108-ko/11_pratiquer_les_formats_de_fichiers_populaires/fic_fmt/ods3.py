from odf.opendocument import OpenDocumentSpreadsheet
from odf.style import ParagraphProperties, Style, TableColumnProperties, TextProperties
from odf.style import TableCellProperties
from odf.table import Table, TableCell, TableColumn, TableRow
from odf.text import P

from fake_contact import fake_contact

doc= OpenDocumentSpreadsheet()
table= Table(parent=doc.spreadsheet, name="Contacts")

# Colonne Nom
Col5 = Style(parent=doc.automaticstyles, name='Col5', family='table-column')
TableColumnProperties(parent=Col5, columnwidth='5cm')
TableColumn(parent=table, numbercolumnsrepeated=1, stylename=Col5)

# Colonne Date Naissance
Col3 = Style(parent=doc.automaticstyles, name='Col3', family='table-column')
TableColumnProperties(parent=Col3, columnwidth='3cm')
TableColumn(parent=table, numbercolumnsrepeated=1, stylename=Col3)

# Colonne adresse
Col12 = Style(parent=doc.automaticstyles, name='Col12', family='table-column')
TableColumnProperties(parent=Col12, columnwidth='12cm')
TableColumn(parent=table, numbercolumnsrepeated=1, stylename=Col12)

# Colonne telephone
TableColumn(parent=table, numbercolumnsrepeated=1, stylename=Col5)

# Colonne Comment
TableColumn(parent=table, numbercolumnsrepeated=1, stylename=Col12)

# Definition d'un style pour le titre
TitreBleu= Style(name="TitreBleu", family="table-cell")
TitreBleu.addElement(TextProperties(fontweight="bold", fontsize="13", color="#0000ff"))
doc.automaticstyles.addElement(TitreBleu)

## Definition entete de colonne
EntCol= Style(name="EntCol", family="table-cell")
EntCol.addElement(TextProperties(fontweight="bold"))
EntCol.addElement(TableCellProperties(backgroundcolor="#AEAEAE"))
doc.automaticstyles.addElement(EntCol)

# Ajout du titre

tr= TableRow()
table.addElement(tr)
tc= TableCell(stylename="TitreBleu")
tc.addElement(P(text="Liste des contacts"))
tr.addElement(tc)

table.addElement(TableRow())

# Ajout des entetes
tr= TableRow()
table.addElement(tr)
for entete in ["Nom", "Date de naissance", "Adresse", "Telephone", "Comment"]:
    tc= TableCell(stylename="EntCol")
    tc.addElement(P(text=entete))
    tr.addElement(tc)

for x in range(0,10):
    tr = TableRow(parent=table)
    c = []
    c = fake_contact()
    for champ in c:
        tc = TableCell(parent=tr)
        p = P(parent=tc, stylename='table-column', text=champ)


doc.save("contacts.ods")

