import tkinter as tk

from model.Unit.Bigdaddy import Bigdaddy


class Console():

    def console(self, joueur,timer, board):
        root = tk.Tk()

        canvas1 = tk.Canvas(root, width=400, height=300)
        canvas1.pack()

        entry1 = tk.Entry(root)
        canvas1.create_window(200, 140, window=entry1)

        def print():
            x1 = entry1.get()
            if (x1 == "NINJALUI"):
                joueur.contenu["wood"] += 10000
                joueur.contenu["stone"] += 10000
                joueur.contenu["food"] += 10000
                joueur.contenu["gold"] += 10000
                label1 = tk.Label(root, text='NINJALUI done !', font=('helvetica', 10))
                canvas1.create_window(200, 210, window=label1)
            if (x1 == "TIMER10"):
                timer.minute = 10
                timer.seconde = 0
                label2 = tk.Label(root, text='TIMER10 done !', font=('helvetica', 10))
                canvas1.create_window(200, 210, window=label2)
            if (x1 == "TIMER25"):
                timer.minute = 25
                timer.seconde = 0
                label3 = tk.Label(root, text='TIMER25 done !', font=('helvetica', 10))
                canvas1.create_window(200, 210, window=label3)
            if (x1 == "BIGDADDY"):
                b = Bigdaddy((700, 4500), 'R', board)
                board.board.append(b)
                label3 = tk.Label(root, text='VROUUUUMMMMMMMMMMMMMMMMMMMMM !', font=('helvetica', 10))
                canvas1.create_window(200, 210, window=label3)



        button1 = tk.Button(text='Enter', command=print)
        canvas1.create_window(200, 180, window=button1)

        root.mainloop()