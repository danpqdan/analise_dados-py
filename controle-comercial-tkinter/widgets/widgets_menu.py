import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from assets.router_path import imagemPadrao


def create_widgets_menu(self):
    self.master.title("menu")

    self.frames = {}

    larguraTela = self.master.winfo_screenwidth()
    alturaTela = self.master.winfo_screenheight()
    self.master.geometry(f'{larguraTela}x{alturaTela}+0+0')

    self.tkimage_cli = ImageTk.PhotoImage(Image.open(imagemPadrao).resize((larguraTela, alturaTela)))
    tk.Label(self, image=self.tkimage_cli).grid(row=0, column=0)
    
    # Menu bar setup
    self.menu_bar = tk.Menu(self)
    self.master.config(menu=self.menu_bar)

    # Functionality menu
    menu_func = tk.Menu(self.menu_bar)
    self.menu_bar.add_cascade(label="Funcionalidades", menu=menu_func)
    menu_func.add_command(label="Clientes", command=self.show_clientes)
    menu_func.add_command(label="Produtos/Serviços", command=self.show_produtos)
    menu_func.add_command(label="Vendas", command=self.show_vendas)
    menu_func.add_command(label="Gestão de Acessos", command=self.show_cadlogin)
    menu_func.add_separator()
    menu_func.add_command(label="Sair", command=self.exit_app)

    # Help menu
    menu_ajuda = tk.Menu(self.menu_bar)
    self.menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)
    menu_ajuda.add_command(label="Sobre", command=self.show_about)