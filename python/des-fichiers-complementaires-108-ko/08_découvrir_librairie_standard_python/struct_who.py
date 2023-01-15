import struct

wtmp_struct = {
        'type'          : 'i',
        'process_id'    : 'i',
        'DeviceName'    : '32s',
        'Inittab_id'    : '4s',
        'Username'      : '32s',
        'padding'       : '308x',
    }

## Construction de la structure pou unpack
st = ''.join(wtmp_struct.values())

## calcul de la longueur de l'enregistrement
len_record = struct.calcsize(st)

print("St=%s : %s " % (st, len_record))

fichier = '/var/log/wtmp'

with open(fichier, 'rb') as fic:
    EOF=False
    while not EOF:
        record = fic.read(len_record)
        if len(record) != len_record:
            EOF=True
        else:
            lig = struct.unpack(st, record)
            l_typ       = lig[0]
            l_pid       = lig[1]
            l_device    = lig[2].decode('ascii')
            l_init      = lig[3]
            l_user      = lig[4].decode('ascii')
            print(" %s %d %s " % (l_device, l_pid, l_user))

