from tkinter import *
from tkinter import messagebox

#definitions des fonctions
def login():
    nom_utilisateur = "a"
    mdp = "a"
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
    liste = [ 'dessin salle1', 'peinture salle7' ]
    lundi1.delete(0, END)
    lundi1.insert(0, liste[0])
    lundi2.delete(0, END)
    lundi2.insert(0, liste[1])

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

bouton = Button(frame, text="Générer le planning des examens", font = ('Arial bold', 20), fg='black',bg='#445964', command=remplir)
bouton.pack(side='bottom', fill='x')

label = Label(frame, text="Planning des examens de ArtSchool", font = ( "Arial Bold" , 30 ), fg='black',bg='#9ADBFF')
label.pack()

lundi = Label(frame, text="Lundi", font = ('Arial Bold', 15), fg='black',bg='#9ADBFF')
lundi.place(x=120, y=80)

mardi = Label(frame, text="Mardi", font = ('Arial Bold', 15), fg='black',bg='#9ADBFF')
mardi.place(x=420, y=80)

mercredi = Label(frame, text="Mercredi", font = ('Arial Bold', 15), fg='black',bg='#9ADBFF')
mercredi.place(x=720, y=80)

jeudi = Label(frame, text="Jeudi", font = ('Arial Bold', 15), fg='black',bg='#9ADBFF')
jeudi.place(x=1020, y=80)

vendredi = Label(frame, text="Vendredi", font = ('Arial Bold', 15), fg='black',bg='#9ADBFF')
vendredi.place(x=1320, y=80)

trait1 = Label(frame, text="________________________________________________________________________________________________________________________________________", font = ('Arial', 15), fg='black',bg='#9ADBFF')
trait1.place(x=0, y=105)

lundi_m = Label(frame, text="Matin", font = ('Arial', 15), fg='black',bg='#9ADBFF')
lundi_m.place(x=120, y=135)

lundi_a = Label(frame, text="Après-midi", font = ('Arial', 15), fg='black',bg='#9ADBFF')
lundi_a.place(x=95, y=390)

lundi1 = Entry(frame, font = ('Arial', 15), fg='black',bg='#9ADBFF')
lundi1.place(x=5, y=160, width=300, height=200)

lundi2 = Entry(frame, font = ('Arial', 15), fg='black',bg='#9ADBFF')
lundi2.place(x=5, y=420, width=300, height=200)

mardi_m = Label(frame, text="Matin", font = ('Arial', 15), fg='black',bg='#9ADBFF')
mardi_m.place(x=420, y=135)

mardi_a = Label(frame, text="Après-midi", font = ('Arial', 15), fg='black',bg='#9ADBFF')
mardi_a.place(x=395, y=390)

mardi1 = Entry(frame, font = ('Arial', 15), fg='black',bg='#9ADBFF')
mardi1.place(x=305, y=160, width=300, height=200)

mardi2 = Entry(frame, font = ('Arial', 15), fg='black',bg='#9ADBFF')
mardi2.place(x=305, y=420, width=300, height=200)

mercredi_m = Label(frame, text="Matin", font = ('Arial', 15), fg='black',bg='#9ADBFF')
mercredi_m.place(x=728, y=135)

mercredi_a = Label(frame, text="Après-midi", font = ('Arial', 15), fg='black',bg='#9ADBFF')
mercredi_a.place(x=698, y=390)

mercredi1 = Entry(frame, font = ('Arial', 15), fg='black',bg='#9ADBFF')
mercredi1.place(x=605, y=160, width=300, height=200)

mercredi2 = Entry(frame, font = ('Arial', 15), fg='black',bg='#9ADBFF')
mercredi2.place(x=605, y=420, width=300, height=200)

jeudi_m = Label(frame, text="Matin", font = ('Arial', 15), fg='black',bg='#9ADBFF')
jeudi_m.place(x=1020, y=135)

jeudi_a = Label(frame, text="Après-midi", font = ('Arial', 15), fg='black',bg='#9ADBFF')
jeudi_a.place(x=995, y=390)

jeudi1 = Entry(frame, font = ('Arial', 15), fg='black',bg='#9ADBFF')
jeudi1.place(x=905, y=160, width=300, height=200)

jeudi2 = Entry(frame, font = ('Arial', 15), fg='black',bg='#9ADBFF')
jeudi2.place(x=905, y=420, width=300, height=200)

vendredi_m = Label(frame, text="Matin", font = ('Arial', 15), fg='black',bg='#9ADBFF')
vendredi_m.place(x=1330, y=135)

vendredi_a = Label(frame, text="Après-midi", font = ('Arial', 15), fg='black',bg='#9ADBFF')
vendredi_a.place(x=1305, y=390)

vendredi1 = Entry(frame, font = ('Arial', 15), fg='black',bg='#9ADBFF')
vendredi1.place(x=1205, y=160, width=293, height=200)

vendredi2 = Entry(frame, font = ('Arial', 15), fg='black',bg='#9ADBFF')
vendredi2.place(x=1205, y=420, width=293, height=200)



window.mainloop()