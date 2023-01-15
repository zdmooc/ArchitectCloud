##
## FAKE PRODUITS
##
##  1 - Choix FAMILLE
##      => NOM
##      => Description Obligatoire
##      => Coef prix en fonction description
##  2 - Description Physique
##      Dimension / UNITE
##      DIAMETRE / UNITE
##      POIDS / UNITE
##  
##      COULEUR
##          %age
##      MATIERE
##          %age
##  
##  3 - Adjectif 
##      %age
##  4 - Autres 
##      %age
##  
##  5 - Catégorie de prix
##      A   5 - 100
##      B   100 - 500
##      C   100 - 900
##      D   1000 - 5000
##      E   2000 - 9000
##      F   10000   50000
##      
##  
##  Famille : 
##      DECORATION
##          SABRE       
##              DIM1 
##                  CM
##              POIDS
##                  KG
##          TABLEAU 
##              DIM2    
##                  M, CM
##          VASE 
##              POIDS
##                  KG
##          STATUE 
##              DIM3 
##                  CM METRE
##              POIDS
##                  KG
##                  TONNE
##          MINIATURE
##              DIM2
##                  CM MM
##          NAPPERON
##              DIM2
##                  CM
##      MOBILIER
##          TABLE   
##              MATIERE
##          CHAISE  
##              MATIERE
##          FAUTEUIL    
##              MATIERE
##          BUFFET  
##              MATIERE
##          TABOURET    
##              MATIERE
##      HIGH TECH
##          CLAVIER 
##              COULEUR
##          ECRAN   
##              COULEUR
##          CONSOLE 
##              COULEUR
##          TABLETTE    
##              COULEUR
##          SOURIS  
##              COULEUR
##          SMARTPHONE  
##              COULEUR
##          CHARGEUR    
##              COULEUR
##          CABLE CHARGE    
##              COULEUR
##      VAISSELLE
##          COUTEAU
##          ASSIETTE
##          FOURCHETTE
##          CUILLERE
##          CASSEROLE
##          POELE
##          FAITOUT
##          COCOTTE
##      SERVICES
##          MONTAGE
##          DEMONTAGE
##          INSTALLATION
##          LIVRAISON
##      LOGICIEL
##      DOCUMENTATION
##      OUTILLAGE
##          PINCE
##          CISEAU
##          TOURNEVIS
##          CUTTER
##          CLE PLATE
##          CLE A DOUILLE
##      CABLES
##          CABLE RESEAU
##          CABLE ELECTRIQUE
##          CABLE VIDEO
##          CABLE AUDIO
##  
##  Catégorie (INUTILE pour l'instant)
##      COMPOSANT
##      PRODUIT FINI
##      MATIERE PREMIERE
##      NEGOCE
##  
##  Description Physique
##      DIMENSION 1/2/3 UNITE
##      DIAMETRE UNITE
##      POIDS UNITE
##      COULEUR
##      MATIERE ( bois, papier, carton, metal, pierre, vegetal, plastique )
##  
##  UNITE
##      Metre
##      Centimetre
##      Millimetre
##      Kg
##      Tonne
##  
##  Adjectif 
##      LASER
##      SONIQUE
##      SILENCIEUX
##      MOU
##      DUR
##      SOUPLE
##      FLEXIBLE
##      MALEABLE
##      GAMER
##      ETIRABLE
##  
##  AUTRES
##      A FONDRE
##      A PEINDRE
##      BRUT
##      PEINTE
##  
##  

from pyexcel_ods import get_data
import random
from faker import Faker

import pudb
##      MATIERE ( bois, papier, carton, metal, pierre, vegetal, plastique )
MATIERE = [
        "BOIS",
        "PAPIER",
        "CARTON",
        "METAL",
        "PIERRE",
        "MATIERE VEGETALE",
        "PLASTIQUE",
        ]

ADJECTIF = [
    "LASER",
    "SONIQUE",
    "SILENCIEUX",
    "MOU",
    "DUR",
    "SOUPLE",
    "FLEXIBLE",
    "MALEABLE",
    "GAMER",
    "PRO",
    "ETIRABLE",
    "A COULISSE",
    "ELECTRIQUE",
]

AUTRES = [
    "A PEINDRE",
    "BRUT",
    "PEINTE",
    "VERNIS",
    "SATINE",
    "BRILLANT",
]

DECORATIONS = {}
MOBILIER = {}
HIGH_TECH = {}
VAISSELLE = {}
SERVICES = {}
#LOGICIELS = {}
#DOCUMENTATIONS = {}
OUTILLAGE = {}
CABLES = {}


PRODUITS = { 
    "DECORATIONS"       : DECORATIONS,
    "MOBILIER"          : MOBILIER,
    "HIGH_TECH"         : HIGH_TECH,
    "VAISSELLE"         : VAISSELLE,
    "SERVICES"          : SERVICES,
#    "LOGICIELS"         : LOGICIELS,
#    "DOCUMENTATIONS"    : DOCUMENTATIONS,
    "OUTILLAGE"         : OUTILLAGE,
    "CABLES"            : CABLES,
}

PC_ADJECTIF = 30
PC_COULEUR  = 70
PC_AUTRES   = 80

fake = Faker('fr_FR')

## --------------------------------------
## La classe description 
## permet de determiner les parametres 
## de generation aleatoire 
## --------------------------------------
class Description():
    def __init__( self, dim, du, poids, pu, dia, diu, couleur, matiere, prix, adj, autres ):
        self.dimension = dim
        self.du = du
        self.diametre = dia
        self.diu = diu
        self.poids = poids
        self.pu = pu
        self.couleur = couleur
        self.matiere = matiere
        self.catprix = prix
        self.adjectif = adj
        self.autres = autres

    def __str__(self):
        r = ""
        if self.dimension:
            r += self.dimension
        return r

##
## La classe Fake Produit contient 
## les données de base pour genere 
## un produit au hasard
## 
class FakeProduit():
    def __init__(self, famille, nom, description):
        self.nom = nom
        self.desc = description
        self.famille = famille

        self.desig = "<vide>"
        self.prix = 0
        self.poids = 0


    def __str__(self):
        return "{:20s} | {:70s} | {:>8.2f}€ ". format( self.nom, self.desig, self.prix )

    ## renvoi un valeur en fonction
    ## de l'unite
    def set_D(self, U):
        if U == "MM":
            return random.randint( 1, 50)
        elif U == "CM":
            return random.randint( 1, 99)
        elif U == "M":
            return random.randint( 1, 9)
        elif U == "KG":
            return random.randint( 1, 99)
        elif U == "T":
            return random.randint( 1, 5)

    ## generation des donnees aleatoires
    ## Dimension
    def set_dim(self, dim, du):
            if dim == "D1":
                return "Long =  %s %s" % ( self.set_D(du) , du)
            elif dim == "D2":
                return "( lo x la ) %s x %s %s" % ( self.set_D(du), self.set_D(du) , du)
            elif dim == "D3":
                return "( H x lo x la ) %s x %s x %s %s" % ( self.set_D(du), self.set_D(du), self.set_D(du) , du)
    ## Diametre
    def set_diam(self, d, u):
        return "Diametre =  %s %s" % ( self.set_D(u) , u)

    ## Poids
    def set_poids(self, p, u):
        return "Poids =  %s %s" % ( self.set_D(u) , u)

    ## Couleur
    def set_couleur(self):
        return fake.color_name()

    ## Matiere
    def set_matiere(self):
        return random.choice(MATIERE).capitalize()

    ## Adjectif
    def set_adjectif(self):
        return random.choice(ADJECTIF).capitalize()

    ## Autres
    def set_autres(self):
        return random.choice(AUTRES).capitalize()

    ## Prix
    ##  5 - Catégorie de prix
    ##      A   5 - 100
    ##      B   100 - 500
    ##      C   100 - 900
    ##      D   1000 - 5000
    ##      E   2000 - 9000
    ##      F   10000   50000
    def set_prix(self,c_prix):
        categ = c_prix.strip()
        if    categ == "A":
              return random.randint(5, 100)
        elif categ == "B":
              return random.randint(100, 500)
        elif categ == "C":
              return random.randint(100, 900)
        elif categ == "D":
              return random.randint(1000, 5000)
        elif categ == "E":
              return random.randint(2000, 9000)
        elif categ == "F":
              return random.randint(10000, 50000)

    def set_desig(self):
        self.desig = self.nom.capitalize()
        x = random.randint(0, 100)
        if self.desc.couleur != 'N':
            if x > PC_COULEUR:
                self.desig = "%s %s" % (self.desig, self.set_couleur() )
            else:
                if self.desc.adjectif != 'N':
                    x = random.randint(0, 100)
                    if x > PC_ADJECTIF:
                        self.desig = "%s %s" % (self.desig, self.set_adjectif() )

        x = random.randint(0, 100)
        if x > PC_AUTRES:
            self.desig = "%s %s" % (self.desig, self.set_autres() )

        if self.desc.matiere != 'N':
            self.desig = "%s en %s " % (self.desig, self.set_matiere() )

        if self.desc.dimension:
            self.desig = "%s %s" % (self.desig, self.set_dim( self.desc.dimension, self.desc.du) )

        #if self.desc.poids:
        #    self.desig = "%s %s" % (self.desig, self.set_dim( self.desc.poids, self.desc.pu) )

    def set_alea(self):
        self.prix = self.set_prix( self.desc.catprix )
        self.set_desig()

## ---------------------------------
## Construction d'un objet de base 
## ce qui est dans le .ods
## ---------------------------------
def set_data( data ):
        famille, nom, dim, du, poids, pu, dia, diu, couleur, matiere, prix, adj, autres = data
        d = PRODUITS[famille]
        desc = Description( dim, du, poids, pu, dia, diu, couleur, matiere, prix, adj, autres )
        d[nom] = FakeProduit( famille, nom, desc )


## ------------------------------------
## Constitution du catalogue de base
## ------------------------------------
def init():
    data = get_data("FAKE_PRODUITS.ods")

    F = data['Feuille1']

    #pudb.set_trace()
    for l in F[1:]:
        l = [ x.strip() for x in l ]
        if l:
            set_data( l )

    ## Liste des produits
    #for D in PRODUITS:
    #    for l in PRODUITS[D].values():
    #        print(D, "%s" % l)

def genere():
    F = random.choice(list(PRODUITS))
    P = random.choice(list(PRODUITS[F]))
    fp = PRODUITS[F][P]
    fp.set_alea()
    return fp

if __name__ == "__main__":
    #pudb.set_trace()
    init()
    for x in range(1,1000):
        fp = genere()
        print( "{:20s} | {:70s} | {:>8.2f}€ ". format( fp.nom, fp.desig, fp.prix ))
        ## TODO => gerer les uniques dans un dico 

