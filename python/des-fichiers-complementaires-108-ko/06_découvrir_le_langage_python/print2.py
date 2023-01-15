bases = [ "Dec", "Hex", "Oct", "Bin" ]
fmt_titre = "|{d[0]:^5s}|{d[1]:^5s}|{d[2]:^5s}|{d[3]:^5s}|"
titre = fmt_titre.format( d=bases )
print('-' * len(titre))
print(titre)
print('-' * len(titre))
for num in range(0,16): 
    print("|", end='')
    for base in 'dXob':
        print('{0:5{base}}'.format(num, base=base), end='|')
    print()
print('-' * len(titre))
