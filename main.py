from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry


class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def cambiar(event):
        problema1 = " Crear un arreglo de numpy basado en una lista"
        problema2= "Comparar si el primer elemento de una lista es mayor que el segundo\n elemento(imprimir el elemento mayor)"
        problema3 = "Genere un arreglo de 9 elementos con números pares mayores a 10"
        problema4 = "  Dado el arreglo de numpy del ejercicio anterior utilice una función \nde numpy para hacer posible la multiplicación con su matriz identidad"
        problema5 = " Dado el arreglo de numpy con las notas de algunos alumnos de matemáticas\n, determine el promedio de las notas"
        listProblemas = [problema1,problema2,problema3,problema4,problema5]
        contProblemas = 0




    def initUI(self):
        problema1 = " Crear un arreglo de numpy basado en una lista"
        problema2= "Comparar si el primer elemento de una lista es mayor que el segundo\n elemento(imprimir el elemento mayor)"
        problema3 = "Genere un arreglo de 9 elementos con números pares mayores a 10"
        problema4 = "  Dado el arreglo de numpy del ejercicio anterior utilice una función \nde numpy para hacer posible la multiplicación con su matriz identidad"
        problema5 = " Dado el arreglo de numpy con las notas de algunos alumnos de matemáticas\n, determine el promedio de las notas"
        listProblemas = [problema2,problema3,problema4,problema5]
        global contProblemas
        contProblemas = 1
        self.parent.title("Numpy If-else problems")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global expr
        expr = StringVar()
        global res
        res = StringVar()
        randomIterator = iter(listProblemas)
        def cambio(event):

            label.configure(text=next(randomIterator))
            label.update()
            print("hola ")


        frame0 = Frame(self)
        frame0.pack(fill=X)
        label = Label(frame0, text=problema1, justify=CENTER)
        label.pack(side=TOP,padx=50, pady=20)
        frame1 = Frame(self)
        frame1.pack(fill=X)
        btn = Button(frame0,text="Siguiente problema")
        btn.bind("<Button-1>", cambio)
        btn.pack(pady=10)




        lbl1 = Label(frame1, text="Your code :", width=18)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Text(frame1,width=10, height=20)
        entry1.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btnplus = Button(frame3, text="Run", width=8, command=self.validate)
        btnplus.pack(side=LEFT, anchor=N, padx=5, pady=5)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl3 = Label(frame4, text="Result :", width=10)
        lbl3.pack(side=LEFT, padx=5, pady=5)

        result = Entry(frame4,textvariable=res)
        result.pack(fill=X, padx=5, expand=True)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Enter your expression')

    def validate(self):
        if expr.get() == '':
            self.errorMsg('error')
        else:
            result = validate(expr.get())
            file = open('res', 'r')
            last_line = file.read().splitlines()[-1]
            res.set(last_line)


def main():
    root = Tk()
    root.geometry("800x600")
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
