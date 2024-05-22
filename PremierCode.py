import csv 

class Matiere():
    def __init__(self,name,duree,listeSalles, aretes, couleur, degres, degreSaturation):
        self.name=name
        self.duree=duree
        self.listeSalles=listeSalles
        self.aretes = aretes
        self.degres = degres
        self.couleur = couleur
        self.degreSaturation = degreSaturation

    #getter setter et affichage
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def duree(self):
        return self._duree

    @duree.setter
    def duree(self,value):
        self._duree = int(value)

    @duree.deleter
    def duree(self):
        del self._duree
    @property
    def degres(self):
        return self._degres

    @degres.setter
    def degres(self,value):
        self._degres = int(value)
    
    @degres.deleter
    def degres(self):
        del self._degres
    
    @property
    def degreSaturation(self):
        return self._degreSaturation

    @degreSaturation.setter
    def degreSaturation(self,value):
        self._degreSaturation = int(value)

    @degreSaturation.deleter
    def degreSaturation(self):
        del self._degreSaturation

    @property
    def couleur(self):
        return self._couleur

    @couleur.setter
    def couleur(self,value):
        self._couleur = int(value)

    @couleur.deleter
    def couleur(self):
        del self._couleur
    
    @property
    def aretes(self):
        return self._aretes

    @aretes.setter
    def aretes(self,value):
        self._aretes = value

    @aretes.deleter
    def aretes(self):
        del self._aretes

    @property
    def listeSalles(self):
        return self._listeSalles

    @listeSalles.setter
    def listeSalles(self,value):
        self._listeSalles = value

    @listeSalles.deleter
    def listeSalles(self):
        del self._listeSalles

    def afficherMatiere(self):
        print(self.name,end=', ')# end='' sert à ne pas retrouner à la ligne avec le print
        print(self.duree,end=', ')
        print(self.degreSaturation,end=', ')
        print(self.degres,end=', ')
        print(self.couleur,end=', ')
        print("[ ",end='')
        for salle in self.listeSalles:
            print(salle.name,end=' ')
        print("]")
        print("[ ",end='')
        for ar in self.aretes:
            print(ar,end=' ')
        print("]")

class Salle():
    def __init__(self,name,capacite,listeDisponibilite):
        self.name=name
        self.capacite=capacite
        self.listeDisponibilite=listeDisponibilite

    #getter setter et toString
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def capacite(self):
        return self._capacite

    @capacite.setter
    def capacite(self,value):
        self._capacite = int(value)

    @capacite.deleter
    def capacite(self):
        del self._capacite

    @property
    def listeDisponibilite(self):
        return self._listeDisponibilite

    @listeDisponibilite.setter
    def listeDisponibilite(self,value):
        self._listeDisponibilite = int(value)

    @listeDisponibilite.deleter
    def listeDisponibilite(self):
        del self._listeDisponibilite

    def afficherSalle(self):
        print(self.name,end=', ')# end='' sert à ne pas retrouner à la ligne avec le print
        print(self.capacite,end=', ')
        for dispo in self.listeDisponibilite:
            print(dispo,end=' ')
        print("]")


class Promotion():
    def __init__(self,name,nbPlaces,listeMatiere):
        self.name=name
        self.nbPlaces=nbPlaces
        self.listeMatiere=listeMatiere

    #getter setter et toString
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def nbPlaces(self):
        return self._nbPlaces

    @nbPlaces.setter
    def nbPlaces(self,value):
        self._nbPlaces = int(value)

    @nbPlaces.deleter
    def nbPlaces(self):
        del self._nbPlaces

    @property
    def listeMatiere(self):
        return self._listeMatiere

    @listeMatiere.setter
    def listeMatiere(self,value):
        self._listeMatiere = value

    @listeMatiere.deleter
    def listeMatiere(self):
        del self._listeMatiere

    def afficherPromotion(self):
        print(self.name,end=', ')# end='' sert à ne pas retrouner à la ligne avec le print
        print(self.nbPlaces,end=', ')
        print("[ ",end='')
        for matiere in self.listeMatiere:
            print(matiere.name,end=', ')
        print("]")

class Session():
    def __init__(self,creneau,listeMatiere):
        self.creneau=creneau
        self.listeMatiere=listeMatiere

    #getter setter et toString
    @property
    def creneau(self):
        return self._creneau

    @creneau.setter
    def creneau(self,value):
        self._creneau = value

    @creneau.deleter
    def creneau(self):
        del self._creneau

    @property
    def listeMatiere(self):
        return self._listeMatiere

    @listeMatiere.setter
    def listeMatiere(self,value):
        self._listeMatiere = int(value)

    @listeMatiere.deleter
    def listeMatiere(self):
        del self._listeMatiere

    def afficherSession(self):
        print(self.creneau,end=', ')# end='' sert à ne pas retrouner à la ligne avec le print
        print("[ ",end='')
        for matiere in self.listeMatiere:
            print(matiere.name,end=' ')
        print("]")


matieres = []

with open('Matières.csv', mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        matiere = Matiere (
            name=row['nom'],
            duree=int(row['duree']),
            listeSalles=[],
            aretes=[],
            degres=0,
            degreSaturation=0,
            couleur=0
        )
        matieres.append(matiere)

promotions = []

with open('Promotions.csv', mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        liste_matieres_noms = row['liste_matieres'].split(';') #Fais une liste des matières de chaque promo
        liste_matieres = [matiere for matiere in matieres if matiere.name in liste_matieres_noms]
        promotion = Promotion(
            name=row['nom'],
            nbPlaces=int(row['nb_eleves']),
            listeMatiere=liste_matieres
        )
        promotions.append(promotion)

for matiere in matieres:
    matiere.afficherMatiere()

for promotion in promotions:
    promotion.afficherPromotion()

######## main ############

#ici on introduira le code de Sarah et Charlotte qui liront le csv et fourniront une liste de salles, une liste de matières et une liste de promotions. 
#Tous les attributs des promotions seront remplis et on n'y touchera plus. 
#Tous les attributs des salles seront remplis et seuls les disponibilités seront modifés par la partie de Bertrand. 
#Le nom et la duree des matières seront remplis et on n'y touchera plus, la liste des salles sera rempli dans la partie de Bertrand et intialisé à une liste vide, les arêtes et le degré de saturation seront respectivement initialisés à une liste vide et 0.


#on suppose
#matieres #liste de matières
#promotions #liste de promotions
#salles #liste de salles

#dans la partie du code qui va suivre, on va parcourir les promotions pour créer les arêtes des matières. Une arête représente le fait que les deux matières ne puissent pas se dérouler sur la même session

for promo in promotions :
    matpromo=promo.listeMatiere #on récupère la liste des matières de la promo
    for i in range(len(matpromo)): #on traite les matières une par une
        for j in range (i+1, len(matpromo)): 
            if matpromo[j] not in matpromo[i].aretes : #on vérifie que l'arête n'existe pas déjà
                matpromo[i].aretes.append(matpromo[j])
                matpromo[j].aretes.append(matpromo[i]) #ici on a les matières i et j qui sont enseignées dans une promo donc les examens ne peuvent pas se dérouler en même temps, donc on ajoute j dans les arêtes de i et i dans les arêtes de j

def mat_deg_max():
    max=0
    deg=0
    for matiere in matieres :
        if max <= matiere.degreSaturation and matiere.couleur==0 :
            if max==matiere.degreSaturation and deg < len(matiere.aretes) :
                max = matiere.degreSaturation
                deg = len(matiere.aretes)
                mat = matiere
    return mat
