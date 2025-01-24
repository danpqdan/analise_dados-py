# -*- coding: utf-8 -*-
import platform
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from conexao import Conexao  
from router_path import dir, imagemPadrao, imagemSecundaria
from ClienteTreeview import ClienteTreeview

class Cliente(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

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

        self.create_widgets()
        self.novo()

    def create_widgets(self):
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

    def novo(self):
        con = Conexao()
        sql_txt = "select IFNULL(max(codigo)+1,1) as codigo from clientes"
        rs = con.consultar(sql_txt)

        if rs:
            self.txtcodigo.insert(0, rs[0])

        con.fechar()
        self.txtnome.focus_set()

    def limpar(self):
        self.txtcodigo.delete(0, "end")
        self.txtnome.delete(0, "end")
        self.txttelefone.delete(0, "end")
        self.txtemail.delete(0, "end")
        self.txtobservacao.delete("1.0", "end")
        self.novo()

    def buscar(self):
        var_codigo = self.txtcodigo.get()
        self.txtcodigo.delete(0, "end")

        con = Conexao()
        sql_txt = f"select codigo, nome, telefone, email, observacao from clientes where codigo = {var_codigo}"
        rs = con.consultar(sql_txt)

        if rs:
            self.txtcodigo.insert(0, rs[0])
            self.txtnome.insert(0, rs[1])
            self.txttelefone.insert(0, rs[2])
            self.txtemail.insert(0, rs[3])
            self.txtobservacao.insert("1.0", rs[4])
        else:
            messagebox.showwarning("Aviso", "Código não Encontrado", parent=self.master)
            self.limpar()
            self.txtcodigo.focus_set()

        con.fechar()

    def gravar(self):
        var_codigo = self.txtcodigo.get()
        var_nome = self.txtnome.get()
        var_telefone = self.txttelefone.get()
        var_email = self.txtemail.get()
        var_observacao = self.txtobservacao.get("1.0", "end")

        con = Conexao()
        sql_txt = f"select codigo, nome, telefone, email, observacao from clientes where codigo = {var_codigo}"
        rs = con.consultar(sql_txt)

        if rs:
            sql_text = f"update clientes set nome='{var_nome}', telefone='{var_telefone}', email='{var_email}', observacao='{var_observacao}' where codigo = '{var_codigo}'"
        else:
            sql_text = f"insert into clientes(codigo, nome, telefone, email, observacao) values ({var_codigo}, '{var_nome}', '{var_telefone}', '{var_email}', '{var_observacao}')"

        if con.gravar(sql_text):
            messagebox.showinfo("Aviso", "Item Gravado com Sucesso", parent=self.master)
            self.limpar()
        else:
            messagebox.showerror("Erro", "Houve um Erro na Gravação", parent=self.master)

        con.fechar()

    def excluir(self):
        var_del = messagebox.askyesno("Exclusão", "Tem certeza que deseja excluir?", parent=self.master)
        if var_del:
            var_codigo = self.txtcodigo.get()

            con = Conexao()
            sql_text = f"delete from clientes where codigo = '{var_codigo}'"
            if con.gravar(sql_text):
                messagebox.showinfo("Aviso", "Item Excluido com Sucesso", parent=self.master)
                self.limpar()
            else:
                messagebox.showerror("Erro", "Houve um Erro na Exclusão", parent=self.master)

            con.fechar()
            self.limpar()
        else:
            self.limpar()

    def menu(self): 
        self.master.switch_to_menu()

    def atualizar_filds(self, fields, valores):
        if len(valores) == len(fields):
            for field, valor in zip(fields, valores):
                if isinstance(field, tk.Entry):
                    field.delete(0, tk.END)
                    field.insert(0, valor)
                elif isinstance(field, tk.Text):
                    field.delete("1.0", tk.END)
                    field.insert("1.0", valor)

