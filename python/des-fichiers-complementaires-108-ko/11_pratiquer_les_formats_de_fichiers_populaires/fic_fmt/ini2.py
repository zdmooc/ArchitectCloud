import configparser as cp

config = cp.ConfigParser()

data_default = {
            "default_user" : "demo",
            "default_password" : "demo",
            "server":"localhost",
            "port":27017
        }

config['DEFAULT'] = data_default

data_chap1 = {
        "multi lignes" : """
         On peut stocker de multiples lignes dans les fichiers .ini
         c'est quand même pratique
        """
        }

config['Chapitre 1'] = data_chap1

with open('test2.ini', 'w') as config_file:
    config.write(config_file)
