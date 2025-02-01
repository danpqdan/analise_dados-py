# -*- coding: utf-8 -*-
import platform
import tkinter as tk
from tkinter import messagebox
from conexao import Conexao  
from widgets.widgets_cliente import create_widgets_cliente

class Cliente(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.novo()

    def create_widgets(self):
        create_widgets_cliente(self=self)

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

