import platform
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from assets.router_path import imagemSecundaria
from services.ClienteTreeview import ClienteTreeview


def create_widgets_cliente(self):

    larguraTela = self.master.winfo_screenwidth()
    alturaTela = self.master.winfo_screenheight()
    self.master.geometry(f'{larguraTela}x{alturaTela}+0+0')

    if platform.system() == "Windows":
        self.master.state('zoomed')
    else:
        self.master.attributes('-zoomed', True)
    self.master.title("Controle Comercial 1.0 - Cadastro de Clientes")
    self.master['bg'] = "gold"

    self.tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((larguraTela, alturaTela)))
    tk.Label(self, image=self.tkimage_cli).grid()

    lblcodigo = tk.Label(self, text="Codigo:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor="w")
    lblcodigo.place(x=50, y=60, width=85, height=25)

    self.txtcodigo = tk.Entry(self, width=35, font=('Calibri', 12))
    self.txtcodigo.place(x=150, y=60, width=100, height=25)

    buscabtn = tk.Button(self, text="Pesquisar", bg='white', foreground='black', font=('Calibri', 12, 'bold'), command=self.buscar)
    buscabtn.place(x=280, y=60, width=90, height=25)

    lblnome = tk.Label(self, text="Nome:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor="w")
    lblnome.place(x=50, y=100, width=85, height=25)

    self.txtnome = tk.Entry(self, width=35, font=('Calibri', 12))
    self.txtnome.place(x=150, y=100, width=360, height=25)

    lbltelefone = tk.Label(self, text="Telefone:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor="w")
    lbltelefone.place(x=50, y=140, width=85, height=25)

    self.txttelefone = tk.Entry(self, width=35, font=('Calibri', 12))
    self.txttelefone.place(x=150, y=140, width=360, height=25)

    lblemail = tk.Label(self, text="E-mail:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor="w")
    lblemail.place(x=50, y=180, width=85, height=25)

    self.txtemail = tk.Entry(self, width=35, font=('Calibri', 12))
    self.txtemail.place(x=150, y=180, width=360, height=25)

    lblobservacao = tk.Label(self, text="Observacao:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor="w")
    lblobservacao.place(x=50, y=220, width=85, height=25)

    self.txtobservacao = tk.Text(self, font=('Calibri', 12))
    self.txtobservacao.place(x=150, y=220, width=360, height=80)

    btngravar = tk.Button(self, text="Gravar", bg='black', foreground='white', font=('Calibri', 12, 'bold'), command=self.gravar)
    btngravar.place(x=150, y=320, width=65)

    btnexcluir = tk.Button(self, text="Excluir", bg='red', foreground='white', font=('Calibri', 12, 'bold'), command=self.excluir)
    btnexcluir.place(x=250, y=320, width=65)

    btnlimpar = tk.Button(self, text="Limpar", bg='green', foreground='white', font=('Calibri', 12, 'bold'), command=self.limpar)
    btnlimpar.place(x=350, y=320, width=65)

    btnmenu = tk.Button(self, text="Menu", bg='yellow', foreground='black', font=('Calibri', 12, 'bold'), command=self.menu)
    btnmenu.place(x=450, y=320, width=65)

    self.text_fields = [self.txtcodigo, self.txtnome, self.txttelefone, self.txtemail, self.txtobservacao]
    self.tree = ClienteTreeview(self)
    self.tree.tree.bind("<Double-1>", lambda event: self.atualizar_filds(self.text_fields, self.tree.duplo_click(event)))

