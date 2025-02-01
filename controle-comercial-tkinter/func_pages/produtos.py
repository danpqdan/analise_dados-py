# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conexao import Conexao
import locale
from widgets.widgets_produtos import create_widgets_produto

class Produto(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()    
    
    def create_widgets(self):
        create_widgets_produto(self=self)   
        
    def limpar(self):
        self.txtcodigo.delete(0, "end")
        self.txtdescricao.delete(0, "end")
        self.cmbtipo.delete(0, "end")
        self.txtquantidade.delete(0, "end")
        self.txtcusto.delete(0, "end")
        self.txtpreco.delete(0, "end")
        self.txtcodigo.focus_set()

    def buscar(self):
        var_codigo = self.txtcodigo.get()
        con = Conexao()
        sql_txt = f"select codigo, descricao, tipo, quantidade, custo, preco from prodserv where codigo = {var_codigo}"
        rs = con.consultar(sql_txt)

        if rs:
            self.limpar()
            self.txtcodigo.insert(0, rs[0])
            self.txtdescricao.insert(0, rs[1])
            self.cmbtipo.insert(0, rs[2])
            self.txtquantidade.insert(0, rs[3])
            self.txtcusto.insert(0, locale.currency(rs[4]))
            self.txtpreco.insert(0, locale.currency(rs[5]))
        else:
            messagebox.showwarning("Aviso", "Código não Encontrado", parent=self.master)
            self.limpar()
            self.txtcodigo.focus_set()

        con.fechar()

    def gravar(self):
        var_codigo = self.txtcodigo.get()
        var_tipo = self.cmbtipo.get()
        var_descricao = str.upper(self.txtdescricao.get())
        var_quantidade = self.txtquantidade.get()
        var_custo = self.txtcusto.get()
        var_custo = float(var_custo.replace('R$', '').strip().replace('.', '').replace(',', '.'))
        var_preco = self.txtpreco.get()
        var_preco = float(var_preco.replace('R$', '').strip().replace('.', '').replace(',', '.'))

        con = Conexao()
        sql_txt = f"select codigo, descricao, tipo, quantidade, custo, preco from prodserv where codigo = '{var_codigo}'"
        rs = con.consultar(sql_txt)

        if rs:
            sql_text = f"update prodserv set tipo='{var_tipo}', descricao='{var_descricao}', quantidade={var_quantidade}, custo={var_custo}, preco={var_preco} where codigo = '{var_codigo}'"
        else:
            sql_text = f"insert into prodserv(codigo, tipo, descricao, quantidade, custo, preco) values ('{var_codigo}', '{var_tipo}', '{var_descricao}', {var_quantidade}, {var_custo}, {var_preco})"

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
            sql_text = f"delete from prodserv where codigo = '{var_codigo}'"
            if con.gravar(sql_text):
                messagebox.showinfo("Aviso", "Item Excluído com Sucesso", parent=self.master)
                self.limpar()
            else:
                messagebox.showerror("Erro", "Houve um Erro na Exclusão", parent=self.master)
            con.fechar()
        else:
            self.limpar()

    def menu(self):
        self.master.switch_to_menu()

    def limitar_tamanho(self, p, limite):
        return len(p) <= int(limite)

    def atualizar_filds(self, fields, valores):
        if len(valores) == len(fields):
            for field, valor in zip(fields, valores):
                if isinstance(field, tk.Entry):
                    field.delete(0, tk.END)
                    field.insert(0, valor)
                elif isinstance(field, tk.Text):
                    field.delete("1.0", tk.END)
                    field.insert("1.0", valor)
                elif isinstance(field, ttk.Combobox):
                    if valor in field['values']:
                        field.set(valor)
                    else:
                        print(f"Valor '{valor}' não encontrado na lista do Combobox.")
