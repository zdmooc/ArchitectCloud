import psutil
from psutil._common import bytes2human


def fmt_ntuple( nt ):
    r = []
    for name in nt._fields:
        valeur = getattr(nt, name)
        if name != 'percent':
            valeur = bytes2human(valeur)
        else:
            valeur = "{:5.2f}%".format(valeur)
        r.append( "{:10s} : {:>7s}".format( name.capitalize(), valeur ))
    return r

def main():
    mem = fmt_ntuple( psutil.virtual_memory())
    swp = fmt_ntuple( psutil.swap_memory())
    mx = max( len(mem), len(swp) )
    mem += [ " " * 20  ] * mx
    swp += [ " " * 20  ] * mx
    print("Memory".center(20), ' | ', "Swap".center(20), ' |')
    for x in range(0, mx):
        print( mem[x] , ' | ', swp[x] , ' |')

if __name__ == '__main__':
    main()
