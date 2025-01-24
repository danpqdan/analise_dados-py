# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import bcrypt
from conexao import Conexao
import platform
from router_path import imagemSecundaria


class CadLogin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        larguraTela = self.master.winfo_screenwidth()
        alturaTela = self.master.winfo_screenheight()
        self.master.geometry(f'{larguraTela}x{alturaTela}+0+0')

        self.tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((larguraTela, alturaTela)))
        tk.Label(self, image=self.tkimage_cli).grid(row=0, column=0)

        lblUsuario = tk.Label(self, text ="Usuario:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = "w")
        lblUsuario.place(x = 50, y = 60, width=80,height=25)
        entry = tk.Entry(self, width = 100)
        self.txtUsuario = tk.Entry(self, width = 35, font=('Calibri', 12))
        self.txtUsuario.place(x = 150, y = 60, width = 100, height=25)

        lblNome = tk.Label(self, text ="Nome:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = "w")
        lblNome.place(x = 50, y = 100, width=80, height=25)
        self.txtNome = tk.Entry(self, font=('Calibri', 12))
        self.txtNome.place(x = 150, y = 100, width = 360, height=25)

        lblSenha = tk.Label(self, text ="Senha:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = "w")
        lblSenha.place(x = 50, y = 140, width=80, height=25)
        self.txtsenha = tk.Entry(self, show = "*" , width = 35, font=('Calibri', 12))
        self.txtsenha.place(x = 150, y = 140, width = 100, height=25)

        submitbtn = tk.Button(self, text ="Gravar", 
                            bg ='black',foreground='white', font=('Calibri', 12, 'bold'), command = self.gravar)
        submitbtn.place(x = 150, y = 190, width = 65)

        submitbtn = tk.Button(self, text ="Excluir", 
                            bg ='red',foreground='white', font=('Calibri', 12, 'bold'), command = self.excluir)
        submitbtn.place(x = 230, y = 190, width = 65)

        submitbtn = tk.Button(self, text ="Limpar", 
                            bg ='green',foreground='white', font=('Calibri', 12, 'bold'), command = self.limpar)
        submitbtn.place(x = 310, y = 190, width = 65)

        submitbtn = tk.Button(self, text ="Menu", 
                            bg ='yellow',foreground='black', font=('Calibri', 12, 'bold'), command = self.master.switch_to_menu)
        submitbtn.place(x = 390, y = 190, width = 65)

        buscabtn = tk.Button(self, text ="Pesquisar", 
                            bg ='white',foreground='black', font=('Calibri', 12, 'bold'), command = self.buscar)
        buscabtn.place(x = 280, y = 60, width = 90, height=25)

        style = ttk.Style()

        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=("Calibri", 10))
        style.configure("mystyle.Treeview.Heading", font=("Calibri", 12, "bold"))


        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4"), show='headings', style="mystyle.Treeview", padding=0)

        self.tree.columnconfigure(0, weight=1)
        self.tree.rowconfigure(0, weight=1)

        self.tree.column("#1")
        self.tree.heading("#1", text="Código")
        self.tree.column("#1", width = 100, anchor ='c')

        self.tree.column("#2")
        self.tree.heading("#2", text="Usuario")
        self.tree.column("#2", width = 130, anchor ='c')

        self.tree.column("#3")
        self.tree.heading("#3", text="Nome")
        self.tree.column("#3", width = 250, anchor ='c')

        self.tree.column("#4")
        self.tree.heading("#4", text="Criado Em")
        self.tree.column("#4", width = 200, anchor ='c')


        self.tree.place(x=50, y=260, height=200)

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x = 731, y = 260 , height=200)

        self.visualizar()
        self.txtUsuario.focus_set()


    def limpar(self):
        self.txtUsuario.delete(0,"end")
        self.txtNome.delete(0,"end")
        self.txtsenha.delete(0,"end")
        self.txtUsuario.focus_set()

    def buscar(self):
        var_usuario = self.txtUsuario.get()
        con=Conexao()
        sql_txt = f"SELECT usuario, nome, senha FROM login WHERE usuario = '{var_usuario}'"
        rs=con.consultar(sql_txt)
        if rs:
            self.limpar()
            self.txtUsuario.insert(0, rs[0])
            self.txtNome.insert(0,rs[1])
            self.txtsenha.insert(0,rs[2])
        else:
            messagebox.showwarning("Aviso", "Usuario não Encontrado")
            self.limpar()
            self.txtUsuario.focus_set()
        con.fechar()

    def duplo_click(self, event):
        self.limpar()
        item = self.tree.item(self.tree.selection())
        self.txtUsuario.insert(0, item['values'][1])
        self.buscar()

    def visualizar(self):
        con=Conexao()
        sql_txt = "select Codigo_int,usuario,nome,criado_em  from login order by nome"
        rs=con.consultar_tree(sql_txt)
        self.tree.bind("<Double-1>", self.duplo_click)
        for linha in self.tree.get_children():
            self.tree.delete(linha)
        for linha in rs:
            self.tree.insert("", tk.END, values=linha)

    def gravar(self):
        var_usuario = self.txtUsuario.get()
        var_nome = self.txtNome.get()
        var_senha = self.txtsenha.get()
        con = Conexao()
        sql_txt = "SELECT usuario, nome, senha FROM login WHERE usuario = ?"
        rs = con.consultar(sql_txt, (var_usuario,))
        if rs:
            db_usuario, db_nome, db_hash_senha = rs
            if bcrypt.checkpw(var_senha.encode('utf-8'), db_hash_senha):
                messagebox.showinfo("Aviso", "Usuário já existe com a mesma senha.")
            else:
                salt = bcrypt.gensalt()
                senha_hash = bcrypt.hashpw(var_senha.encode('utf-8'), salt)
                sql_text = "UPDATE login SET nome = ?, senha = ? WHERE usuario = ?"
                parametros = (var_nome, senha_hash, var_usuario)
                if con.gravar(sql_text, parametros):
                    messagebox.showinfo("Aviso", "Senha atualizada com sucesso.")
                    self.limpar()
                else:
                    messagebox.showerror("Erro", "Houve um erro na atualização.")
        else:
            salt = bcrypt.gensalt()
            senha_hash = bcrypt.hashpw(var_senha.encode('utf-8'), salt)
            sql_text = "INSERT INTO login (usuario, nome, senha) VALUES (?, ?, ?)"
            parametros = (var_usuario, var_nome, senha_hash)
            if con.gravar(sql_text, parametros):
                messagebox.showinfo("Aviso", "Novo usuário gravado com sucesso.")
                self.limpar()
            else:
                messagebox.showerror("Erro", "Houve um erro na gravação.")
        con.fechar()
        self.visualizar()
    def excluir(self):
        var_del = messagebox.askyesno("Exclusívo", "Tem certeza que deseja excluir?")
        if var_del == True:
            var_usuario = self.txtUsuario.get()
            con=Conexao()
            sql_text = f"delete from login where usuario = '{var_usuario}'"
            if con.gravar(sql_text):
                  messagebox.showinfo("Aviso", "Item Excluídos com Sucesso")
                  self.limpar()
            else:
                messagebox.showerror("Erro", "Houve um Erro na Exclusão")
            con.fechar()
            self.visualizar()
        else:
            self.limpar()