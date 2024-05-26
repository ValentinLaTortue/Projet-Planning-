import csv
import ast
from tkinter import *
from tkinter import messagebox

# Classe représentant une matière
class Matiere():
    def __init__(self,name,duree,listeSalles, aretes, couleur, degreSaturation):
        self.name=name
        self.duree=duree
        self.listeSalles=listeSalles
        self.aretes = aretes
        self.couleur = couleur
        self.degreSaturation = degreSaturation

    #getter setter et affichage pour chaque attribut
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

    # Méthode pour afficher les informations d'une matière
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

# Classe représentant une salle
class Salle():
    def __init__(self, name, capacite, listeDisponibilite):
        self.name = name
        self.capacite = capacite
        self.listeDisponibilite = listeDisponibilite

    # Getter, setter et toString pour chaque attribut
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

    # Méthode pour afficher les informations d'une salle
    def afficherSalle(self):
        print(self.name, end=', ')  # end='' sert à ne pas retourner à la ligne avec le print
        print(self.capacite, end=', ')
        for dispo in self.listeDisponibilite:
            print(dispo, end=' ')
        print("]")

# Classe représentant une promotion
class Promotion():
    def __init__(self,name,nb_eleves,listeMatiere):
        self.name=name
        self.nb_eleves=nb_eleves
        self.listeMatiere=listeMatiere

    #getter setter et toString pour chaque attribut
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
    def nb_eleves(self):
        return self._nb_eleves

    @nb_eleves.setter
    def nb_eleves(self,value):
        self._nb_eleves = int(value)

    @nb_eleves.deleter
    def nb_eleves(self):
        del self._nb_eleves

    @property
    def listeMatiere(self):
        return self._listeMatiere

    @listeMatiere.setter
    def listeMatiere(self,value):
        self._listeMatiere = value

    @listeMatiere.deleter
    def listeMatiere(self):
        del self._listeMatiere

    # Méthode pour afficher les informations d'une promotion
    def afficherPromotion(self):
        print(self.name,end=', ')# end='' sert à ne pas retrouner à la ligne avec le print
        print(self.nb_eleves,end=', ')
        print("[ ",end='')
        for matiere in self.listeMatiere:
            print(matiere.name,end=', ')
        print("]")

# Classe représentant une session d'examen
class Session():
    def __init__(self,couleur,listeMatiere):
        self.listeMatiere=listeMatiere
        self.couleur=couleur

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

    # Méthode pour afficher les informations d'une session
    def afficherSession(self):
        print(self.couleur) # end='' sert à ne pas retourner à la ligne avec le print
        print("[ ",end='')
        for matiere in self.listeMatiere:
            print(matiere.name,end=' ')
        print("]")


# Lecture des matières à partir d'un fichier CSV
matieres = []
with open('Matieres.csv', mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        matiere = Matiere (
            name=row['nom'],
            duree=int(row['duree']),
            listeSalles=[],
            aretes=[], # Initialisation des arêtes à une liste vide
            degreSaturation=0, # Initialisation du degré de saturation à 0
            couleur=0 # Initialisation de la couleur à 0
        )
        matieres.append(matiere)

# Lecture des promotions à partir d'un fichier CSV
promotions = []
with open('Promotions.csv', mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        liste_matieres_noms = row['liste_matieres'].split(';') #Fais une liste des matières de chaque promo
        liste_matieres = [matiere for matiere in matieres if matiere.name in liste_matieres_noms]
        promotion = Promotion(
            name=row['nom'],
            nb_eleves=int(row['nb_eleves']),
            listeMatiere=liste_matieres
        )
        promotions.append(promotion)

#for matiere in matieres:
#    matiere.afficherMatiere()

#for promotion in promotions:
#    promotion.afficherPromotion()

# Lecture des salles à partir d'un fichier CSV
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

#dans la partie du code qui va suivre, on va parcourir les promotions pour créer les arêtes des matières. Une arête représente le fait que les deux matières ne puissent pas se dérouler sur la même session


# Création des arêtes pour chaque matière
for promo in promotions :
   matpromo=promo.listeMatiere # Récupération de la liste des matières de la promo
   for i in range(len(matpromo)): # Parcours des matières de la promotion une par une
       for j in range (i+1, len(matpromo)):
           if matpromo[j] not in matpromo[i].aretes : #on vérifie que l'arête n'existe pas déjà
               matpromo[i].aretes.append(matpromo[j])
               matpromo[j].aretes.append(matpromo[i]) #ici on a les matières i et j qui sont enseignées dans une promo donc les examens ne peuvent pas se dérouler en même temps, donc on ajoute j dans les arêtes de i et i dans les arêtes de j
#complexité : nbPromo*nbMatPromo*nbmatpromo

# Fonction pour trouver la matière avec le degré de saturation maximal
def mat_deg_max():
    max=-1
    deg=-1
    for matiere in matieres :
        if matiere.couleur==0 and (max < matiere.degreSaturation or (max==matiere.degreSaturation and deg < len(matiere.aretes)))  : #on s'assure que le sommet n'a pas déjà été traité et que soit son degré de saturation est strictement supérieur à ceux des sommets d'avant, soit son degré de saturation est égale au maximum des degrés de saturation des sommets d'avant mais son degré est strictement supérieur.
            max = matiere.degreSaturation
            deg = len(matiere.aretes)
            mat = matiere
    return mat

sessions=[]
compteur=0

# Boucle pour colorier les matières en utilisant l'algorithme Dsatur
while compteur<len(matieres):
    compteur+=1
    encours=mat_deg_max() # Récupération de la matière avec le degré de saturation maximal
    coul=1
    ok=True
    couleurs=[0 for k in range (len(matieres))] # Initialisation des couleurs disponibles, len(matieres) est le nombre max de couleurs qu'on pourra utiliser, il n'est généralement jamais atteint

    for mat in encours.aretes : #on parcourt les voisons du sommet en cours
        if mat.couleur==1: #si la couleur 1 est déjà utilisée par les voisins, on ne peut pas utiliser la couleur 1
            ok=False
        if mat.couleur>0: #on remplit le tableau des couleurs des voisins
            couleurs[mat.couleur - 1]=1 #comme python utilise des indices débutant à 0 et que 0 représente un sommet non coloré pour nous, on décale les indices de 1. C'est à dire que si couleurs[i]=1, la couleur i+1 est utilisé par un des voisins du sommet

    if not ok : #si la couleur 1 est déjà utilisé par un voisin
        ind=0
        while couleurs[ind]==1: #on parcourt notre tableau des couleurs jusqu'à trouver un 0, c'est-à-dire une couleur non utilisée
            ind+=1
        coul=ind+1 #on décale l'indice de 1 car la couleur 0 ne nous intéresse pas
    encours.couleur=coul # Assigner la couleur à la matière courante

    trouve=False
    for ses in sessions : #on regarde si une session de cette couleur existe déjà
        if ses.couleur==coul:
            ses.listeMatiere.append(encours)
            trouve=True

    if not trouve: # Si aucune session de même couleur n'est trouvée, créer une nouvelle session
        ses=Session(couleur=coul, listeMatiere=[encours])
        sessions.append(ses)

    for mat in encours.aretes : # Augmenter le degré de saturation des matières voisines
            mat.degreSaturation += 1

"""
print("   ")
for ses in sessions:
    ses.afficherSession()
"""

# Conversion des sessions en dictionnaire
dic = {}
for ses in sessions:
    (a,b) = ses.couleur,ses.listeMatiere
    dic[a] = b

# Fonction qui réparti les sessions de matières sur plusieurs jours en fonction de leur nombre

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
    if reste_arrondi >= 4:
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

# Fonction pour afficher l'emploi du temps
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

# Fonction pour assigner les salles aux matières
def assignation_salle(emploidutemps, promotions, salles):
    resultat = {}
    jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi']

    for jour, sessions_jour in emploidutemps.items():
        resultat[jour] = {}
        max_heure_fin=510 # Réinitialiser l'heure de départ à 8h30 chaque jour

        for session in sessions_jour:
            salles_utilisees = []
            heuredepart=max_heure_fin # Réinitialiser l'heure de départ à la dernière heure de fin

            for matiere in session:
                duree_matiere = matiere.duree
                capacite_totale = 0

                # Calculer le nombre total d'élèves pour la matière actuelle
                for promotion in promotions:
                    for matiere_promo in promotion.listeMatiere:
                        if matiere_promo.name == matiere.name:
                            capacite_totale += promotion.nb_eleves

                nb_eleve_restants = capacite_totale
                liste_nb_eleve = []
                liste_salles = []

                for salle in salles :
                    if salle in salles_utilisees : # Ignorer les salles déjà utilisées
                        continue

                    liste_dispo = salle.listeDisponibilite[jours.index(jour)] # Récupère la disponibilité de la salle
                    debut_session = -1

                    ind_dep=(heuredepart-510)//30 # Calculer l'indice de départ pour la vérification des créneaux

                    # Parcourir la liste de disponibilité pour trouver un créneau libre
                    for i in range(ind_dep,len(liste_dispo)):
                        if liste_dispo[i] == 0:
                            if debut_session == -1:
                                debut_session = i # Marque le début d'un créneau libre
                        else:
                            debut_session = -1 # Le créneau disponible dans cette salle n'est pas assez long pour la matière, on teste à un nouvel horaire

                        if debut_session != -1 and (i - debut_session + 1) == duree_matiere : #le créneau est suffisamment long, on va utiliser cette salle
                            if nb_eleve_restants <= salle.capacite and (debut_session + duree_matiere)<=len(liste_dispo): # Si la salle peut contenir tous les élèves d'une promotion d'un coup et qu'il y a suffisamment de créneau dans la journée pour cette salle
                                if (debut_session + duree_matiere)==len(liste_dispo) or (debut_session + duree_matiere)==len(liste_dispo)-1: #si le créneau est en fin de journée, on ne rajoute pas de pause après l'épreuve
                                    fin=debut_session + duree_matiere
                                else :
                                    fin= debut_session + duree_matiere + 2 #sinon on rajoute 1h de pause
                                for k in range(debut_session,fin) :
                                    liste_dispo[k] = 1 # on rend la salle indisponible sur ce créneau
                                liste_salles.append(salle)
                                salles_utilisees.append(salle)
                                liste_nb_eleve.append(nb_eleve_restants)
                                heuredepart = 510 + debut_session * 30  # Calculer l'heure de début en fonction de la première disponibilité
                                nb_eleve_restants = 0 # Tous les élèves d'une même promotion ont été placés
                                break

                            # Si la salle ne peut pas contenir tous les élèves, en placer autant que possible
                            if nb_eleve_restants > salle.capacite and (debut_session + duree_matiere + 2)<=len(liste_dispo):
                                for k in range(debut_session, debut_session + duree_matiere + 2):
                                    liste_dispo[k] = 1
                                liste_salles.append(salle)
                                salles_utilisees.append(salle)
                                liste_nb_eleve.append(salle.capacite)
                                nb_eleve_restants -= salle.capacite # Déduire le nombre d'élèves restants
                                heuredepart = 510 + debut_session * 30
                                break

                        continue

                    if nb_eleve_restants == 0 : # Si tous les élèves ont été placés
                        break

                if nb_eleve_restants > 0 : # Si tous les élèves n'ont pas pu être placés
                    print(f"Il n'y a pas assez de salles ou les salles ne sont pas assez disponibles pour {matiere.name} le {jour}\n")

                if liste_salles and heuredepart is not None:
                    heurefin = (heuredepart + duree_matiere * 30) / 60
                    heurededepart = heuredepart / 60

                    #print(heurefin,max_heure_fin)

                    if heurefin>max_heure_fin*60:
                        max_heure_fin=heurefin*60

                    # Formatage des heures de début et de fin
                    if heurefin % 1 == 0.5:
                        heurefin = str(int(heurefin // 1)) + "h30"
                    else:
                        heurefin = str(int(heurefin // 1)) + "h"
                    if heurededepart % 1 == 0.5:
                        heurededepart = str(int(heurededepart // 1)) + "h30"
                    else:
                        heurededepart = str(int(heurededepart // 1)) + "h"

                    slot_key = f"{heurededepart} jusqu'à {heurefin}" # Création de la clé du créneau horaire
                    if slot_key not in resultat[jour] :
                        resultat[jour][slot_key] = []

                    """
                    promo=[]
                    for promotion in promotions:
                        for matiere_promo in promotion.listeMatiere:
                            if matiere_promo.name == matiere.name:
                                promo.append(promotion.name)
                    """

                    # Ajout des informations : nom de la matière, de la salle et du nombre d'élèves
                    for k in range(len(liste_salles)):
                        resultat[jour][slot_key].append(f"{matiere.name} - {liste_salles[k].name} : {liste_nb_eleve[k]}")

    # Supprimer les jours sans sessions
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
        horaire=horaire.replace("jusqu'à","-")
        print(f"  {horaire} : {matieres}")


tabLundi = []
tabMardi = []
tabMercredi = []
tabJeudi = []
tabVendredi = []

i = 0
for jour, sessions in resultat.items():
    for horaire, matieres in sessions.items():
        if(jour == "lundi"):
            tabLundi.append(horaire.replace("jusqu'à","-")+" :\n")
            tabLundi.append("".join(matieres)+"\n\n")
        if(jour == "mardi"):
            tabMardi.append(horaire.replace("jusqu'à","-")+" :\n")
            tabMardi.append("".join(matieres)+"\n\n")
        if(jour == "mercredi"):
           tabMercredi.append(horaire.replace("jusqu'à","-")+" :\n")
           tabMercredi.append("".join(matieres)+"\n\n")
        if(jour == "jeudi"):
            tabJeudi.append(horaire.replace("jusqu'à","-")+" :\n")
            tabJeudi.append("".join(matieres)+"\n\n")
        if(jour == "vendredi"):
            tabVendredi.append(horaire.replace("jusqu'à","-")+" :\n")
            tabVendredi.append("".join(matieres)+"\n\n")
    i +=1

global L,M,Me,J,V
L="".join(tabLundi)
M="".join(tabMardi)
Me="".join(tabMercredi)
J="".join(tabJeudi)
V="".join(tabVendredi)

###################################################################################################################################""
#Interface graphique

#definitions des fonctions
def login():
    nom_utilisateur = "admin"
    mdp = "team4"
    if nom_u.get()==nom_utilisateur and mdp_u.get()==mdp:
        frame.place(x=0, y=0, width=1500, height=700)
        bouton_c.destroy()
        login_l.destroy()
        nom_utilisateur_l.destroy()
        mdp_l.destroy()
        nom_u.destroy()
        mdp_u.destroy()
    else:
        messagebox.showerror(title="Erreur", message="Connexion invalide")
    
    return 0

def remplir():

    lundi1.delete(0.0, END)
    lundi1.insert(0.0, L)

    mardi1.delete(0.0, END)
    mardi1.insert(0.0, M)

    mercredi1.delete(0.0, END)
    mercredi1.insert(0.0, Me)

    jeudi1.delete(0.0, END)
    jeudi1.insert(0.0, J)

    vendredi1.delete(0.0, END)
    vendredi1.insert(0.0, V)

#fenetre principale
window = Tk()
window.title("Interface admin planning")
window.geometry('1500x700') 
window.minsize(700,500)
window.config(background='#9ADBFF')

######################################################################################################################

bouton_c = Button(window, text="Valider", font = ('Arial bold', 20), fg='black',bg='#445964', command=login)
bouton_c.place(x=700, y=380)

login_l = Label(window, text="Page de connexion", font = ( "Arial Bold" , 30 ), fg='black',bg='#9ADBFF')
login_l.place(x=600, y=50)

nom_utilisateur_l = Label(window, text="Nom d'utilisateur", font = ( "Arial Bold" , 20 ), fg='black',bg='#9ADBFF')
nom_utilisateur_l.place(x=520, y=200)

mdp_l = Label(window, text="Mot de passe", font = ( "Arial Bold" , 20 ), fg='black',bg='#9ADBFF')
mdp_l.place(x=520, y=250)

nom_u = Entry(window, font = ('Arial', 15), fg='black',bg='#445964')
nom_u.place(x=760, y=205)

mdp_u = Entry(window, show='*', font = ('Arial', 15), fg='black',bg='#445964')
mdp_u.place(x=760, y=255)

#######################################################################################################################

frame = Frame(window, background='#9ADBFF', width=1500, height=700)

bouton = Button(frame, text="Cliquez afin de générer le planning d'examens", font = ('Arial bold', 20), fg='black',bg='#445964', command=remplir)
bouton.pack(side='bottom', fill='x')

label = Label(frame, text="Planning des examens de ArtSchool", font = ( "Arial Bold" , 30 ), fg='black',bg='#9ADBFF')
label.pack()

lundi = Label(frame, text="Lundi", font = ('Arial Bold', 15, 'underline'), fg='black',bg='#9ADBFF')
lundi.place(x=120, y=80)

mardi = Label(frame, text="Mardi", font = ('Arial Bold', 15, 'underline'), fg='black',bg='#9ADBFF')
mardi.place(x=420, y=80)

mercredi = Label(frame, text="Mercredi", font = ('Arial Bold', 15, 'underline'), fg='black',bg='#9ADBFF')
mercredi.place(x=715, y=80)

jeudi = Label(frame, text="Jeudi", font = ('Arial Bold', 15, 'underline'), fg='black',bg='#9ADBFF')
jeudi.place(x=1020, y=80)

vendredi = Label(frame, text="Vendredi", font = ('Arial Bold', 15, 'underline'), fg='black',bg='#9ADBFF')
vendredi.place(x=1320, y=80)

trait1 = Label(frame, text="________________________________________________________________________________________________________________________________________", font = ('Arial', 15), fg='black',bg='#9ADBFF')
trait1.place(x=0, y=105)

lundi1 = Text(frame, fg='black',bg='#9ADBFF')
lundi1.config(font = ('Arial', 15)) 
lundi1.place(x=5, y=135, width=295, height=505)

mardi1 = Text(frame, fg='black',bg='#9ADBFF')
mardi1.config(font = ('Arial', 15))
mardi1.place(x=305, y=135, width=295, height=505)

mercredi1 = Text(frame, fg='black',bg='#9ADBFF')
mercredi1.config(font = ('Arial', 15))
mercredi1.place(x=605, y=135, width=295, height=505)

jeudi1 = Text(frame, fg='black',bg='#9ADBFF')
jeudi1.config(font = ('Arial', 15))
jeudi1.place(x=905, y=135, width=295, height=505)

vendredi1 = Text(frame, fg='black',bg='#9ADBFF')
vendredi1.config(font = ('Arial', 15))
vendredi1.place(x=1205, y=135, width=293, height=505)

window.mainloop()