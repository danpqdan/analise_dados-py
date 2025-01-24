import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
# from cadlogin import CadLogin
# from clientes import Cliente
# from produtos import Produto
from router_path import imagemPadrao
# from vendas import Vendas

class TelaMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
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

    def show_about(self):
        messagebox.showinfo("Sobre", "Sistema Comercial 1.0")

    def exit_app(self):
        var_sair = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
        if var_sair:
            self.switch_to_login()
        else:
            messagebox.showinfo("Ótimo", "Que bom que você escolheu continuar")

    def show_frame(self, frame_class):
        """Switch between frames in the menu."""
        for frame in self.frames.values():
            frame.grid_forget()

        if frame_class not in self.frames:
            frame = frame_class(self.master)
            self.frames[frame_class] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        else:
            self.frames[frame_class].grid(row=0, column=0, sticky="nsew")

    # Placeholder methods for other functionalities
    def show_clientes(self):
        self.master.switch_to_clientes()

    def show_produtos(self):
        self.master.switch_to_produtos()

    def show_vendas(self):
        self.master.switch_to_vendas()

    def show_cadlogin(self):
        self.master.switch_to_cadlogin()

    def switch_to_login(self):
        self.master.switch_to_login()
