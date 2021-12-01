from tkinter import *

screen = Tk()
barre = Menu(screen)

menu_fichier = Menu(barre,tearoff=0)
barre.add_cascade(label="Fichier", menu=menu_fichier)

screen.config(menu=barre)
screen.mainloop()
