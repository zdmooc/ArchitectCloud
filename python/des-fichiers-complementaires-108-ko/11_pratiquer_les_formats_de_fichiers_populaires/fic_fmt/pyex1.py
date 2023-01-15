from  pyexcel import get_records

records = get_records(file_name="contacts.ods")


fmt = "|{NOM:30s} | {DATE_NAI:10s} | {TEL:20s} |"

for record in records:
    print( fmt.format( **record ))
