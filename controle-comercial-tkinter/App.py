import threading
import tkinter as tk
from tkinter import messagebox
from cadlogin import CadLogin
from clientes import Cliente
from conexao import Conexao
from login import TelaLogin
from menu import TelaMenu
from produtos import Produto
from vendas import Vendas

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controle Comercial 1.0")
        self.config_window()

        self.frames = {}
        self.show_frame("login")

    def config_window(self):
        self['bg'] = "gold"

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.grid_forget()

        if frame_name not in self.frames:
            if frame_name == "login":
                frame = TelaLogin(self)
            elif frame_name == "menu":
                frame = TelaMenu(self)
            elif frame_name == "clientes":
                frame = Cliente(self)
            elif frame_name == "produtos":
                frame = Produto(self)
            elif frame_name == "vendas":
                frame = Vendas(self)
            elif frame_name == "cadlogin":
                frame = CadLogin(self)
            else:
                raise ValueError(f"Frame '{frame_name}' not found.")

            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        else:
            self.frames[frame_name].grid(row=0, column=0, sticky="nsew")

    def delete_frames(self, exclude=[]):
        for key, frame in list(self.frames.items()):
            if key not in exclude:
                frame.destroy()
                del self.frames[key] 

    def switch_to_menu(self):
        self.delete_frames(exclude=['menu'])
        self.show_frame("menu")

    def switch_to_clientes(self):
        self.delete_frames(exclude=['menu'])
        self.show_frame("clientes")

    def switch_to_produtos(self):
        self.show_frame("produtos")

    def switch_to_vendas(self):
        self.show_frame("vendas")
    
    def switch_to_cadlogin(self):
        self.show_frame("cadlogin")
    
    def switch_to_login(self):
        self.show_frame("login")

def start_conexao():
    con = Conexao()
    con.fechar()

def init_app():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    connection_thread = threading.Thread(target=start_conexao)
    connection_thread.start()
    connection_thread.join()
    init_app()
