from tkinter import *

ventana = Tk()
ventana.geometry("200x300")
ventana.iconbitmap(r"D:\Users\Quetzal\Documents\Monero\Practica-Python\calcu\calculator.ico.ico")
ventana.config(bg="gray")
ventana.title("Calculadora")
ventana.resizable( width=False , height= False )
campo=Entry(ventana, bd=5, bg="LightBlue3", font=("Consolas",20))
campo.place(x=20,y=10,width=160,height=50)


ventana.mainloop()
