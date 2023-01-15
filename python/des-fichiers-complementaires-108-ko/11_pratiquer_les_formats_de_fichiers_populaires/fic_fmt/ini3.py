from configparser import ConfigParser, ExtendedInterpolation

config =ConfigParser(interpolation=ExtendedInterpolation())

config.read("test3.ini")

for titre, section in config.items():
    print("Section : ", titre )
    for cle, val in section.items():
        print("   cle/val  %s = %s" % (cle, val))
