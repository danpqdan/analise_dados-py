# -*- coding: cp1252 -*-
import platform
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from router_path import dir, imagemPadrao, imagemSecundaria


tela = tk.Tk() 
tela.geometry('1960x800+0+0')
if platform.system() == "Windows":
    tela.state('zoomed')
else:
    tela.attributes('-zoomed', True)
tela.title("Controle Comercial 1.0 - Menu")
tela['bg'] = "gold"

tkimage = ImageTk.PhotoImage(Image.open(imagemPadrao).resize((tela.winfo_screenwidth(), tela.winfo_screenheight())))

tk.Label(tela, image=tkimage).pack()

def clientes():
    exec(open(r"/home/zenxbr/Downloads/Controle/clientes.py").read(),locals())

def produtos():
    exec(open(r"/home/zenxbr/Downloads/Controle/produtos.py").read(),locals())

def cadlogin():
    exec(open(r"/home/zenxbr/Downloads/Controle/cadlogin.py").read(),locals())

def vendas():
    exec(open(r"/home/zenxbr/Downloads/Controle/vendas.py").read(),locals())

def sobre():
      messagebox.showinfo("Sobre", "Sistema Comercial 1.0")

def sair():
    var_sair = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
    if var_sair == True:
         tela.destroy()
    else:
        messagebox.showinfo("�timo", "Que bom que voc� escolheu continuar")

barramenu = tk.Menu(tela)
menu_func = tk.Menu(barramenu)
menu_ajuda = tk.Menu(barramenu)

barramenu.add_cascade(label="Funcionalidades", menu=menu_func)
menu_func.add_command(label="Clientes", command=clientes)
menu_func.add_command(label="Produtos/Servi�os", command=produtos)
menu_func.add_command(label="Vendas", command=vendas)
menu_func.add_command(label="Gest�o de Acessos", command=cadlogin)
menu_func.add_separator()
menu_func.add_command(label="Sair",command=sair)

barramenu.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Sobre",command=sobre)
tela.config(menu=barramenu)


tela.mainloop()