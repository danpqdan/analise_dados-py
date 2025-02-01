import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
# from cadlogin import CadLogin
# from clientes import Cliente
# from produtos import Produto
from widgets.widgets_menu import create_widgets_menu

class TelaMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        
    def create_widgets(self):
        create_widgets_menu(self=self)

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
