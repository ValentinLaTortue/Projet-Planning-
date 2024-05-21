
class Matiere():
    def __init__(self,name,duree,listeSalles):
        self.name=name
        self.duree=duree
        self.listeSalles=listeSalles

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
    def duree(self):
        return self._duree

    @duree.setter
    def duree(self,value):
        self._duree = int(value)

    @duree.deleter
    def duree(self):
        del self._duree

    @property
    def listeSalles(self):
        return self._listeSalles

    @listeSalles.setter
    def listeSalles(self,value):
        self._listeSalles = int(value)

    @listeSalles.deleter
    def listeSalles(self):
        del self._listeSalles

    def afficherMatiere(self):
        print(self.name,end=', ')# end='' sert à ne pas retrouner à la ligne avec le print
        print(self.duree,end=', ')
        print("[ ",end='')
        for salle in self.listeSalles:
            print(salle.name,end=' ')
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
        self._listeMatiere = int(value)

    @listeMatiere.deleter
    def listeMatiere(self):
        del self._listeMatiere

    def afficherMatiere(self):
        print(self.name,end=', ')# end='' sert à ne pas retrouner à la ligne avec le print
        print(self.nbPlaces,end=', ')
        print("[ ",end='')
        for matiere in self.listeMatiere:
            print(matiere.name,end=' ')
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

    def afficherMatiere(self):
        print(self.creneau,end=', ')# end='' sert à ne pas retrouner à la ligne avec le print
        print("[ ",end='')
        for matiere in self.listeMatiere:
            print(matiere.name,end=' ')
        print("]")



######## main ############

