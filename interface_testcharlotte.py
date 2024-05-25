from tkinter import *

#pour finir il faudrait réussir à avoir une liste de 10 elements
#Ex: Liste = [8h-10h Mosaïque salle2, 13h-14h30 Peinture salle8, etc]
#Premier element: lundi matin, 2e element: lundi aprem etc

#test resulat
def liste_resultat_final():
    liste = [ 'dessin salle1, salle 8', 'peinture salle 7' ]
    lundi1.delete(0, END)
    lundi1.insert(0, liste[0])
    lundi2.delete(0, END)
    lundi2.insert(0, liste[1])

#parametres fenetre
window = Tk()
window.title("Interface admin planning")
window.geometry('1500x700') 
window.minsize(700,500)
window.config(background='#9ADBFF')

#afficher du texte à la fenetre 
label = Label(window, text="Planning des examens de ArtSchool", font = ( "Arial" , 30 ), fg='black',bg='#9ADBFF')
label.pack()

lundi = Label(window, text="Lundi", font = ('Arial Bold', 15), fg='black',bg='#9ADBFF')
lundi.place(x=120, y=80)

mardi = Label(window, text="Mardi", font = ('Arial Bold', 15), fg='black',bg='#9ADBFF')
mardi.place(x=420, y=80)

mercredi = Label(window, text="Mercredi", font = ('Arial Bold', 15), fg='black',bg='#9ADBFF')
mercredi.place(x=720, y=80)

jeudi = Label(window, text="Jeudi", font = ('Arial Bold', 15), fg='black',bg='#9ADBFF')
jeudi.place(x=1020, y=80)

vendredi = Label(window, text="Vendredi", font = ('Arial Bold', 15), fg='black',bg='#9ADBFF')
vendredi.place(x=1320, y=80)

trait1 = Label(window, text="________________________________________________________________________________________________________________________________________", font = ('Arial', 15), fg='black',bg='#9ADBFF')
trait1.place(x=0, y=105)

bouton = Button(window, text="Générer le planning des examens", font = ('Arial bold', 20), fg='black',bg='#445964', command=liste_resultat_final)
bouton.pack(side='bottom', fill='x')

lundi_m = Label(window, text="Matin", font = ('Arial', 15), fg='black',bg='#9ADBFF')
lundi_m.place(x=120, y=135)

lundi_a = Label(window, text="Après-midi", font = ('Arial', 15), fg='black',bg='#9ADBFF')
lundi_a.place(x=95, y=390)

lundi1 = Entry(window, font = ('Arial', 15), fg='black',bg='#9ADBFF')
lundi1.place(x=5, y=160, width=300, height=200)

lundi2 = Entry(window, font = ('Arial', 15), fg='black',bg='#9ADBFF')
lundi2.place(x=5, y=420, width=300, height=200)

mardi_m = Label(window, text="Matin", font = ('Arial', 15), fg='black',bg='#9ADBFF')
mardi_m.place(x=420, y=135)

mardi_a = Label(window, text="Après-midi", font = ('Arial', 15), fg='black',bg='#9ADBFF')
mardi_a.place(x=395, y=390)

mardi1 = Entry(window, font = ('Arial', 15), fg='black',bg='#9ADBFF')
mardi1.place(x=305, y=160, width=300, height=200)

mardi2 = Entry(window, font = ('Arial', 15), fg='black',bg='#9ADBFF')
mardi2.place(x=305, y=420, width=300, height=200)

mercredi_m = Label(window, text="Matin", font = ('Arial', 15), fg='black',bg='#9ADBFF')
mercredi_m.place(x=728, y=135)

mercredi_a = Label(window, text="Après-midi", font = ('Arial', 15), fg='black',bg='#9ADBFF')
mercredi_a.place(x=698, y=390)

mercredi1 = Entry(window, font = ('Arial', 15), fg='black',bg='#9ADBFF')
mercredi1.place(x=605, y=160, width=300, height=200)

mercredi2 = Entry(window, font = ('Arial', 15), fg='black',bg='#9ADBFF')
mercredi2.place(x=605, y=420, width=300, height=200)

jeudi_m = Label(window, text="Matin", font = ('Arial', 15), fg='black',bg='#9ADBFF')
jeudi_m.place(x=1020, y=135)

jeudi_a = Label(window, text="Après-midi", font = ('Arial', 15), fg='black',bg='#9ADBFF')
jeudi_a.place(x=995, y=390)

jeudi1 = Entry(window, font = ('Arial', 15), fg='black',bg='#9ADBFF')
jeudi1.place(x=905, y=160, width=300, height=200)

jeudi2 = Entry(window, font = ('Arial', 15), fg='black',bg='#9ADBFF')
jeudi2.place(x=905, y=420, width=300, height=200)

vendredi_m = Label(window, text="Matin", font = ('Arial', 15), fg='black',bg='#9ADBFF')
vendredi_m.place(x=1330, y=135)

vendredi_a = Label(window, text="Après-midi", font = ('Arial', 15), fg='black',bg='#9ADBFF')
vendredi_a.place(x=1305, y=390)

vendredi1 = Entry(window, font = ('Arial', 15), fg='black',bg='#9ADBFF')
vendredi1.place(x=1205, y=160, width=293, height=200)

vendredi2 = Entry(window, font = ('Arial', 15), fg='black',bg='#9ADBFF')
vendredi2.place(x=1205, y=420, width=293, height=200)

window.mainloop()

