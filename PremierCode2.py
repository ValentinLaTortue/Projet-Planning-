import csv
import ast

class Matiere():
    def __init__(self,name,duree,listeSalles, aretes, couleur, degreSaturation):
        self.name=name
        self.duree=duree
        self.listeSalles=listeSalles
        self.aretes = aretes
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
        print(self.couleur,end=', ')
        print("[ ",end='')
        for salle in self.listeSalles:
            print(salle.name,end=' ')
        print("]",end=",")
        print("[ ",end='')
        for ar in self.aretes:
            print(ar.name,end=' ')
        print("]")

class Salle():
    def __init__(self, name, capacite, listeDisponibilite):
        self.name = name
        self.capacite = capacite
        self.listeDisponibilite = listeDisponibilite

    # Getter, setter et toString
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def capacite(self):
        return self._capacite

    @capacite.setter
    def capacite(self, value):
        self._capacite = int(value)

    @capacite.deleter
    def capacite(self):
        del self._capacite

    @property
    def listeDisponibilite(self):
        return self._listeDisponibilite

    @listeDisponibilite.setter
    def listeDisponibilite(self, value):
        self._listeDisponibilite = value

    @listeDisponibilite.deleter
    def listeDisponibilite(self):
        del self._listeDisponibilite

    def afficherSalle(self):
        print(self.name, end=', ')  # end='' sert à ne pas retourner à la ligne avec le print
        print(self.capacite, end=', ')
        for dispo in self.listeDisponibilite:
            print(dispo, end=' ')
        print("]")



class Promotion():
    def __init__(self,name,nbEleves,listeMatiere):
        self.name=name
        self.nbEleves=nbEleves
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
    def nbEleves(self):
        return self._nbEleves

    @nbPlaces.setter
    def nbEleves(self,value):
        self._nbEleves = int(value)

    @nbPlaces.deleter
    def nbEleves(self):
        del self._nbEleves

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
    def __init__(self,creneau,couleur,listeMatiere):
        self.creneau=creneau
        self.listeMatiere=listeMatiere
        self.couleur=couleur

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
    def couleur(self):
        return self._couleur

    @couleur.setter
    def couleur(self,value):
        self._couleur=int(value)

    @couleur.deleter
    def couleur(self):
        del self._couleur

    @property
    def listeMatiere(self):
        return self._listeMatiere

    @listeMatiere.setter
    def listeMatiere(self,value):
        self._listeMatiere = value

    @listeMatiere.deleter
    def listeMatiere(self):
        del self._listeMatiere

    def afficherSession(self):
        print(self.creneau,end=', ')# end='' sert à ne pas retourner à la ligne avec le print
        print(self.couleur)
        print("[ ",end='')
        for matiere in self.listeMatiere:
            print(matiere.name,end=' ')
        print("]")
#------------------------------------------#
    def returnSession(self):
        liste = []
        for matiere in self.listeMatiere:
            liste.append(matiere)
        return (self.couleur, liste)
#------------------------------------------#
matieres = []

with open('Matières.csv', mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        matiere = Matiere (
            name=row['nom'],
            duree=int(row['duree']),
            listeSalles=[],
            aretes=[],
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

#for matiere in matieres:
#    matiere.afficherMatiere()

#for promotion in promotions:
#    promotion.afficherPromotion()

salles = []
with open('Salles.csv', mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nom = row['nom']
        capacite = int(row['capacite'])
        # Convertir la chaîne de caractères représentant le tableau en une liste Python
        dispo = ast.literal_eval(row['dispo'])
        salle = Salle(nom, capacite, dispo)
        salles.append(salle)

#for salle in salles:
 #   print("Nom:", salle.name)
  #  print("Capacité:", salle.capacite)
   # print("Disponibilité:", salle.listeDisponibilite)
    #print()
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
#nbPromo*nbMatPromo*nbmatpromo

def mat_deg_max():
    max=-1
    deg=-1
    for matiere in matieres :
        if matiere.couleur==0 and (max < matiere.degreSaturation or (max==matiere.degreSaturation and deg < len(matiere.aretes)))  :
            max = matiere.degreSaturation
            deg = len(matiere.aretes)
            mat = matiere
    return mat

sessions=[]

compteur=0
while compteur<len(matieres):
    compteur+=1
    encours=mat_deg_max()
    coul=1
    ok=True
    couleurs=[0 for k in range (len(matieres))]
    for mat in encours.aretes :
        if mat.couleur==1:
            ok=False
        if mat.couleur>0:
            couleurs[mat.couleur - 1]=1
    if not ok:
        ind=0
        while couleurs[ind]==1:
            ind+=1
        coul=ind+1
    encours.couleur=coul
    trouve=False
    for ses in sessions :
        if ses.couleur==coul:
            ses.listeMatiere.append(encours)
            trouve=True
    if not trouve:
        ses=Session(creneau=[],couleur=coul, listeMatiere=[encours])
        sessions.append(ses)
    for mat in encours.aretes :
            mat.degreSaturation += 1

"""
print("   ")
for ses in sessions:
    ses.afficherSession()
"""

dic = {}
for ses in sessions:
    (a,b) = ses.returnSession()
    dic[a] = b

def emploiDuTemps(dico_matiere):
    jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]

    # Trouver la dernière clé du dictionnaire
    last_key = max(dico_matiere.keys())

    # Calculer le reste de la division par 5
    reste = last_key % 5

    # Arrondir à l'entier supérieur si le reste n'est pas 0
    if reste != 0:
        reste_arrondi = (last_key // 5) + 1
    else:
        reste_arrondi = last_key // 5

    # Si le reste est supérieur ou égal à 4, ajouter samedi
    if reste >= 4:
        jours.append("samedi")

    # Créer un nouveau dictionnaire pour l'emploi du temps
    emploi = {}

    for jour in jours:
        emploi[f"{jour}"] = []

    # Remplir le dictionnaire avec les "reste" sous-tableaux pour chaque jour
    index = 1
    for jour in jours:
        for _ in range(reste_arrondi): # o utilise _ car on n'a pas besoin de l'index d'itération
            if index in dico_matiere:
                emploi[jour].append(dico_matiere[index])
                index += 1
            else:
                break

    return emploi


emploidutemps = emploiDuTemps(dic)

def afficher_emploi_du_temps(emploidutemps):
    for jour, sessions_jour in emploidutemps.items():
        print(f"{jour.capitalize()} : ", end="")
        for session in sessions_jour:
            print("[", end="")
            for idx, matiere in enumerate(session):
                if idx != 0:
                    print(", ", end="")
                print(f"{matiere.name}", end="")
            print("]", end=" ")
    print()

# Appel de la fonction pour afficher l'emploi du temps
#afficher_emploi_du_temps(emploidutemps)

def assignation_salle(emploidutemps, promotions, salles):
    resultat = {}
    jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi']

    for jour, sessions_jour in emploidutemps.items():
        resultat[jour] = {}

        for session in sessions_jour:
            salles_utilisees = []
            heuredepart = 510  # Réinitialiser l'heure de départ à 8h30 chaque jour

            for matiere in session:
                duree_matiere = matiere.duree
                capacite_totale = 0

                # Calculer le nombre total d'élèves pour la matière actuelle
                for promotion in promotions:
                    for matiere_promo in promotion.listeMatiere:
                        if matiere_promo.name == matiere.name:
                            capacite_totale += promotion.nbPlaces

                nb_eleve_restants = capacite_totale
                liste_nb_eleve = []
                liste_salles = []

                for salle in salles:
                    if salle in salles_utilisees:
                        continue

                    liste_dispo = salle.listeDisponibilite[jours.index(jour)]
                    debut_session = -1

                    for i in range(len(liste_dispo)):
                        if liste_dispo[i] == 0:
                            if debut_session == -1:
                                debut_session = i
                        else:
                            debut_session = -1

                        if debut_session != -1 and (i - debut_session + 1) == duree_matiere :
                            if nb_eleve_restants <= salle.capacite:
                                for k in range(debut_session, debut_session + duree_matiere + 2) :
                                    liste_dispo[k] = 1
                                liste_salles.append(salle)
                                salles_utilisees.append(salle)
                                liste_nb_eleve.append(nb_eleve_restants)
                                heuredepart = 510 + debut_session * 30  # Calculer l'heure de début en fonction de la première disponibilité
                                nb_eleve_restants = 0
                                break

                            if nb_eleve_restants > salle.capacite:
                                for k in range(debut_session, debut_session + duree_matiere + 2):
                                    liste_dispo[k] = 1
                                liste_salles.append(salle)
                                salles_utilisees.append(salle)
                                liste_nb_eleve.append(salle.capacite)
                                nb_eleve_restants -= salle.capacite
                                heuredepart = 510 + debut_session * 30
                                break

                    if nb_eleve_restants == 0:
                        break

                if liste_salles and heuredepart is not None:
                    heurefin = (heuredepart + duree_matiere * 30) / 60
                    heuredepart = heuredepart / 60
                    if heurefin % 1 == 0.5:
                        heurefin = str(int(heurefin // 1)) + "h30"
                    else:
                        heurefin = str(int(heurefin // 1)) + "h"
                    if heuredepart % 1 == 0.5:
                        heuredepart = str(int(heuredepart // 1)) + "h30"
                    else:
                        heuredepart = str(int(heuredepart // 1)) + "h"

                    slot_key = f"{heuredepart} jusqu'à {heurefin}"
                    if slot_key not in resultat[jour]:
                        resultat[jour][slot_key] = []

                    """
                    promo=[]
                    for promotion in promotions:
                        for matiere_promo in promotion.listeMatiere:
                            if matiere_promo.name == matiere.name:
                                promo.append(promotion.name)
                    """

                    for k in range(len(liste_salles)):
                        resultat[jour][slot_key].append(f"{promo} - {matiere.name} - {liste_salles[k].name} : {liste_nb_eleve[k]}")
    for jour in jours :
        if resultat[jour]=={} :
            del resultat[jour]
            
    return resultat


print("\n")

# Exemple d'utilisation
resultat = assignation_salle(emploidutemps, promotions, salles)
for jour, sessions in resultat.items():
    print(f"{jour} :")
    for horaire, matieres in sessions.items():
        print(f"  {horaire} : {matieres}")
