import configparser as cp

config = cp.ConfigParser()

config.read("test1.ini")

for titre, section in config.items():
    print("Section : ", titre )
    for cle, val in section.items():
        print("   cle/val  %s = %s" % (cle, val))
