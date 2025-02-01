import platform
import locale
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from services.ProdutoTreeview import ProdutoTreeview
from assets.router_path import imagemSecundaria


def create_widgets_produto(self):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    larguraTela = self.master.winfo_screenwidth()
    alturaTela = self.master.winfo_screenheight()
    self.master.geometry(f'{larguraTela}x{alturaTela}+0+0')
    
    self.master.title("Controle Comercial - Cadastro de Produtos/Serviços")
    self.master['bg'] = "gold"

    self.tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((larguraTela, alturaTela)))
    tk.Label(self, image=self.tkimage_cli).pack()

    limite_campo = self.master.register(self.limitar_tamanho)

    lblcodigo = tk.Label(self, text="Codigo:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor='w')
    lblcodigo.place(x=50, y=20, width=90)
    self.txtcodigo = tk.Entry(self, validate='key', font=('Calibri', 12), validatecommand=(limite_campo, '%P', 13))
    self.txtcodigo.place(x=150, y=20, width=120)

    buscabtn = tk.Button(self, text="Pesquisar", bg='white', foreground='black', font=('Calibri', 12), command=self.buscar)
    buscabtn.place(x=290, y=20, width=80, height=25)

    lbltipo = tk.Label(self, text="Tipo:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor='w')
    lbltipo.place(x=50, y=60, width=90)
    tipos = ["PRODUTO", "SERVICO", "OUTROS"]
    self.cmbtipo = ttk.Combobox(self, values=tipos, font=('Calibri', 12))
    self.cmbtipo.place(x=150, y=60, width=120, height=25)

    lbldescricao = tk.Label(self, text="Descrição:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor='w')
    lbldescricao.place(x=50, y=100, width=90)
    self.txtdescricao = tk.Entry(self, font=('Calibri', 12), validate='key', validatecommand=(limite_campo, '%P', 60))
    self.txtdescricao.place(x=150, y=100, width=400)

    lblquantidade = tk.Label(self, text="Quantidade:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor='w')
    lblquantidade.place(x=50, y=140, width=90)
    self.txtquantidade = tk.Entry(self, font=('Calibri', 12), validate='key', validatecommand=(limite_campo, '%P', 6))
    self.txtquantidade.place(x=150, y=140, width=120)

    lblcusto = tk.Label(self, text="Custo:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor='w')
    lblcusto.place(x=50, y=180, width=90)
    self.txtcusto = tk.Entry(self, font=('Calibri', 12), validate='key', validatecommand=(limite_campo, '%P', 13))
    self.txtcusto.place(x=150, y=180, width=120)

    lblpreco = tk.Label(self, text="Preço:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor='w')
    lblpreco.place(x=50, y=220, width=90)
    self.txtpreco = tk.Entry(self, font=('Calibri', 12), validate='key', validatecommand=(limite_campo, '%P', 13))
    self.txtpreco.place(x=150, y=220, width=120)

    btngravar = tk.Button(self, text="Gravar", bg='black', foreground='white', font=('Calibri', 12), command=self.gravar)
    btngravar.place(x=150, y=280, width=65)

    btnexcluir = tk.Button(self, text="Excluir", bg='red', foreground='white', font=('Calibri', 12), command=self.excluir)
    btnexcluir.place(x=230, y=280, width=65)

    btnlimpar = tk.Button(self, text="Limpar", bg='green', foreground='white', font=('Calibri', 12), command=self.limpar)
    btnlimpar.place(x=310, y=280, width=65)

    btnmenu = tk.Button(self, text="Menu", bg='yellow', foreground='black', font=('Calibri', 12), command=self.menu)
    btnmenu.place(x=390, y=280, width=65)

    self.text_fields = [self.txtcodigo, self.cmbtipo, self.txtdescricao, self.txtquantidade, self.txtcusto, self.txtpreco]
    self.tree = ProdutoTreeview(self)
    self.tree.tree.bind("<Double-1>", lambda event: self.atualizar_filds(self.text_fields, self.tree.duplo_click(event)))

    self.txtcodigo.focus_set()
