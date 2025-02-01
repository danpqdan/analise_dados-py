# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import bcrypt
from conexao import Conexao
from widgets.widgets_cadlogin import create_widgets_cadlogin

class CadLogin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()    

    def create_widgets(self):
        create_widgets_cadlogin(self=self)   


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