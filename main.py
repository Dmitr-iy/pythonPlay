from tkinter import *
import random as rdm


class Main(Frame):
    def __init__(self, field):
        super(Main, self).__init__(field)
        self.lbl4 = None
        self.lbl3 = None
        self.lose = None
        self.drow = None
        self.lbl2 = None
        self.win = None
        self.lbl = None
        self.start()

    def start(self):
        btn = Button(root, text="Камень", font=("Times New Roman", 15), fg="gray99", bg="gold4",
                     command=lambda x=1: self.btn_click(x))
        btn2 = Button(root, text="Ножницы", font=("Times New Roman", 15), fg="gray9", bg="purple",
                      command=lambda x=2: self.btn_click(x))
        btn3 = Button(root, text="Бумага", font=("Times New Roman", 15), fg="lightCyan2", bg="dim gray",
                      command=lambda x=3: self.btn_click(x))

        btn.place(x=10, y=100, width=120, height=50)
        btn2.place(x=155, y=100, width=120, height=50)
        btn3.place(x=300, y=100, width=120, height=50)

        self.lbl = Label(root, text="Начало игры!", bg="#FFF", fg="green4", font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=150, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(root, justify="left", font=("Times New Roman", 13),
                         text=f"Побед: {self.win}\nПроигрышей:"
                              f" {self.lose}\nНичей: {self.drow}",
                         bg="#FFF")
        self.lbl2.place(x=5, y=5)

        self.lbl4 = Label(root, text="Компьютер  выбрал:", font=("Times New Roman", 23, "bold"), bg="white")
        self.lbl4.place(x=30, y=200)


    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 3)

        if comp_choise == 1:
            self.lbl3 = Label(root, text="  Камень  !", font=("Times New Roman", 23, "bold"), fg="gray99", bg="gold4")
            self.lbl3.place(x=350, y=200)

        elif comp_choise == 2:
            self.lbl3 = Label(root, text="Ножницы!", font=("Times New Roman", 23, "bold"), fg="gray9", bg="purple")
            self.lbl3.place(x=350, y=200)

        else:
            self.lbl3 = Label(root, text="   Бумагу  !", font=("Times New Roman", 23, "bold"), fg="lightCyan2", bg="dim gray")
            self.lbl3.place(x=350, y=200)


        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Ничья", fg="blue")
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text="Победа", fg="green")
        else:
            self.lose += 1
            self.lbl.configure(text="Проигрыш", fg="red")

        self.lbl2.configure(text=f"Побед: {self.win}\nПроигрышей:"
                              f" {self.lose}\nНичей: {self.drow}")



if __name__ == '__main__':
    root = Tk()
    root.geometry("530x360+400+400")
    root.title("Камень, ножницы, бумага")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    app = Main(root)
    app.pack()
    root.mainloop()