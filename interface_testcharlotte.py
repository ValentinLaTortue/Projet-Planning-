print ("hello")

from tkinter import *

#test resulat
def liste_resultat_final():
    liste = [ 'dessin salle1, salle 8', 'peinture salle 7' ]
    lundi1.delete(0, END)
    lundi1.insert(0, liste[0])
    lundi2.delete(0, END)
    lundi2.insert(0, liste[1])
    #lundi1.insert(0, liste)

#parametres fenetre
window = Tk()
window.title("Interface admin planning")
window.geometry('1500x700') 
window.minsize(700,500)
window.config(background='#187DB4')

#afficher du texte à la fenetre 
label = Label(window, text="Planning des examens de ArtSchool", font = ( "Arial" , 30 ), fg='black',bg='#187DB4')
label.pack()

#creer un champ
#entree = Entry(window, font=("Helvetica", 20), bg='grey', fg='white')
#entree.pack()

#ajouter un bouton
#bouton = Button( window , text = "Cliquez ici", bg = "white" , fg = "black", command=liste_resultat_final )
#bouton.pack()

lundi = Label(window, text="Lundi", font = ('Arial', 15), fg='black',bg='#187DB4')
lundi.place(x=120, y=80)

mardi = Label(window, text="Mardi", font = ('Arial', 15), fg='black',bg='#187DB4')
mardi.place(x=420, y=80)

mercredi = Label(window, text="Mercredi", font = ('Arial', 15), fg='black',bg='#187DB4')
mercredi.place(x=720, y=80)

jeudi = Label(window, text="Jeudi", font = ('Arial', 15), fg='black',bg='#187DB4')
jeudi.place(x=1020, y=80)

vendredi = Label(window, text="Vendredi", font = ('Arial', 15), fg='black',bg='#187DB4')
vendredi.place(x=1320, y=80)

trait1 = Label(window, text="________________________________________________________________________________________________________________________________________", font = ('Arial', 15), fg='black',bg='#187DB4')
trait1.place(x=0, y=105)

bouton = Button(window, text="Générer le planning des examens", font = ('Arial bold', 20), fg='black',bg='#10435F', command=liste_resultat_final)
bouton.pack(side='bottom', fill='x')

lundi_m = Label(window, text="9h", font = ('Arial', 15), fg='black',bg='#187DB4')
lundi_m.place(x=130, y=135)

lundi_a = Label(window, text="14h", font = ('Arial', 15), fg='black',bg='#187DB4')
lundi_a.place(x=130, y=390)

lundi1 = Entry(window, font = ('Arial', 15), fg='black',bg='#187DB4')
lundi1.place(x=5, y=160, width=300, height=200)

lundi2 = Entry(window, font = ('Arial', 15), fg='black',bg='#187DB4')
lundi2.place(x=5, y=420, width=300, height=200)

window.mainloop()

