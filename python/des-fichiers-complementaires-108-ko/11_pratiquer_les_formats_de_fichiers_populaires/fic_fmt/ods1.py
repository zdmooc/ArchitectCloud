from odf.opendocument import OpenDocumentSpreadsheet
from odf.style import ParagraphProperties, Style, TableColumnProperties, TextProperties
from odf.table import Table, TableCell, TableColumn, TableRow
from odf.text import P

from fake_contact import fake_contact

textdoc = OpenDocumentSpreadsheet()

table = Table(parent=textdoc.spreadsheet, name="Contacts")

#TableColumn(parent=table, numbercolumnsrepeated=5)

for x in range(0,10):
    tr = TableRow(parent=table)
    c = []
    c = fake_contact()
    for champ in c:
        tc = TableCell(parent=tr)
        p = P(parent=tc, text=champ)

textdoc.save("contacts.ods")
