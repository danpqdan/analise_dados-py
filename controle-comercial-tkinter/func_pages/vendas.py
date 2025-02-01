# -*- coding: utf-8 -*-
from conexao import Conexao
import tkinter as tk
from tkinter import messagebox
from services.ClienteTreeview import ClienteTreeview
from services.ProdutoTreeview import ProdutoTreeview
from conexao import Conexao
from services.func_imprimir_vendas import imprimir
from widgets.widgets_vendas import create_widgets_vendas


class Vendas(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        

        self.create_widgets()
        self.numeracao()
        self.excluir_inic()
        self.visualizar()
        self.total()
        self.txtnumvenda.config(state="disabled")
        self.txtcodcli.focus_set()

    def create_widgets(self):
        create_widgets_vendas(self=self)
        

    def abrir_popup_busca_cliente(self):
        popup_busca = tk.Toplevel(self.master)
        popup_busca.title("Buscar Cliente")
        popup_busca.geometry(f"{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}")
        popup_busca.resizable(True, True)
        tree = ClienteTreeview(popup_busca)
        tree.tree.place(x=0, y=0, width=self.master.winfo_screenwidth(), height=self.master.winfo_screenheight())

        def handle_duplo_click(event):
            valores = tree.duplo_click(event)
            print(f"Dados selecionados: {valores}")
            if valores:
                self.txtcodcli.delete(0, tk.END)
                self.txtcodcli.insert(0, valores[0])
            popup_busca.destroy()
            self.txtcodcli.focus()
            self.bus_cli()
        tree.tree.bind("<Double-1>", handle_duplo_click)

    def abrir_popup_busca_prodserv(self):
        popup_busca = tk.Toplevel(self.master)
        popup_busca.title("Buscar Produto")
        popup_busca.geometry(f"{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}")
        popup_busca.resizable(True, True)
        tree = ProdutoTreeview(popup_busca)
        tree.tree.place(x=0, y=0, width=(self.master.winfo_screenwidth() - 50), height=(self.master.winfo_screenheight() - 50))

        def handle_duplo_click(event):
            valores = tree.duplo_click(event)
            print(f"Dados selecionados: {valores}")
            if valores:
                self.txtcodprod.delete(0, tk.END)
                self.txtcodprod.insert(0, valores[0])
                self.txtcodprod.focus()
            popup_busca.destroy()
            self.txtcodcli.focus()
            self.bus_prod()
        tree.tree.bind("<Double-1>", handle_duplo_click)

    def numeracao(self):
        con = Conexao()
        self.txtnumvenda.config(state="normal")
        sql_txt = "SELECT COALESCE(MAX(num_venda), 0) AS num_venda FROM vendas_cab"
        rs = con.consultar(sql_txt)
        if rs:
            num_venda = rs[0]
            if num_venda == 0:
                num_venda = 1
            else:
                num_venda += 1
            self.txtnumvenda.delete(0, "end")
            self.txtnumvenda.insert(0, num_venda)
        self.txtnumvenda.config(state="disabled")

    def limpar(self, event=None):
        print("Limpar acionado!")
        self.txtdescricao.config(state="normal")
        self.txtvlrunit.config(state="normal")
        self.txtvalor.config(state="normal")
        self.txtcodprod.delete(0, "end")
        self.txtdescricao.delete(0, "end")
        self.txtqtde.delete(0, "end")
        self.txtvlrunit.delete(0, "end")
        self.txtvalor.delete("0", "end")
        self.txtcodprod.focus_set()

    def limpar_cab(self):
        self.txtcodcli.config(state="normal")
        self.txtnomecli.config(state="normal")
        self.txtnumvenda.delete(0, "end")
        self.txtnomecli.delete(0, "end")
        self.txtcodcli.delete(0, "end")
        self.txtcodcli.focus_set()

    def gravar_lin(self):
        con = Conexao()
        num_venda = self.txtnumvenda.get()
        var_codcli = self.txtcodcli.get()
        var_codprod = self.txtcodprod.get()
        var_qtde = self.txtqtde.get()
        var_vlrunit = self.txtvlrunit.get()
        var_valor = self.txtvalor.get()

        if not var_codcli:
            messagebox.showwarning("Aviso", "Favor preencher o código do cliente", parent=self.master)
            self.txtcodcli.focus_set()
            return
        if not var_codprod:
            messagebox.showwarning("Aviso", "Favor preencher o código do produto", parent=self.master)
            self.txtcodprod.focus_set()
            return
        if not (var_qtde and var_valor and var_vlrunit):
            messagebox.showwarning("Aviso", "Favor preencher a quantidade", parent=self.master)
            self.txtqtde.focus_set()
            return
        
        if not (float(var_qtde) * float(var_vlrunit) == float(var_valor)):
            messagebox.showwarning("Aviso", "Favor alterar apenas a quantidade", parent=self.master)
            self.txtqtde.focus_set()
            return
        
        try:
            sql_txt = "SELECT COALESCE(MAX(lin_venda), 0) + 1 AS lin_venda FROM vendas_lin WHERE num_venda = ?"
            rs = con.consultar(sql_txt, params=(num_venda,))
            if rs:
                var_lin_venda = rs[0]
                sql_text = '''INSERT INTO vendas_lin (num_venda, lin_venda, codigo_prod, quantidade, valor_unit, valor) 
                              VALUES (?, ?, ?, ?, ?, ?)'''
                params = (num_venda, var_lin_venda, var_codprod, var_qtde, var_vlrunit, var_valor)
                if con.gravar(sql_text, params):
                    messagebox.showinfo("Sucesso", "Linha gravada com sucesso!", parent=self.master)
                    self.limpar()
                else:
                    messagebox.showerror("Erro", "Falha ao gravar a linha.", parent=self.master)
            else:
                messagebox.showerror("Erro", "Erro ao recuperar o próximo número de linha.", parent=self.master)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gravar linha: {e}", parent=self.master)
        finally:
            con.fechar()

    def finalizar_linha(self, event=None):
        self.gravar_lin()
        self.visualizar()
        self.total()

    def excluir(self):
        con = Conexao()
        num_venda = self.txtnumvenda.get()
        item = self.tree.item(self.tree.selection())
        try:
            lin_venda = item['values'][0]
            sql_text = f"DELETE FROM vendas_lin WHERE num_venda = {num_venda} AND lin_venda = {lin_venda}"
            print(sql_text)
            if con.gravar(sql_text):
                self.visualizar()
                self.total()
            else:
                messagebox.showerror("Erro", "Falha ao executar a exclusão.", parent=self.master)
        except Exception as e:
            messagebox.showwarning("Aviso", f"Erro ao excluir: {e}", parent=self.master)

    def excluir_inic(self):
        con = Conexao()
        num_venda = self.txtnumvenda.get()
        sql_text = f"delete from vendas_lin where num_venda = {num_venda}"
        con.gravar(sql_text)

    def visualizar(self):
        con = Conexao()
        num_venda = self.txtnumvenda.get()
        print("Num_venda", num_venda)
        sql_txt = '''SELECT A.lin_venda, A.codigo_prod, B.descricao, A.quantidade, A.valor_unit, A.valor
                     FROM vendas_lin A
                     JOIN prodserv B ON A.codigo_prod = B.codigo
                     WHERE A.num_venda = ? 
                     ORDER BY A.num_venda, A.lin_venda'''
        rs = con.consultar_tree(sql_txt, (num_venda,))
        if rs is None:
            messagebox.showerror("Erro", "Não foi possível consultar as vendas.")
            return
        for linha in self.tree.get_children():
            self.tree.delete(linha)
        for linha in rs:
            self.tree.insert("", tk.END, values=linha)
        con.fechar()

    def total(self):
        con = Conexao()
        num_venda = self.txtnumvenda.get()
        sql_txt = f"select IFNULL(sum(A.valor),0) as valor from vendas_lin A where A.num_venda = {num_venda}"
        rs = con.consultar(sql_txt)
        if rs:
            total_valor = rs[0]
            self.txt_total.config(state="normal")
            self.txt_total.delete("0", "end")
            self.txt_total.insert(0, f"{total_valor:.2f}")
        else:
            total_valor = 9999.999
        con.fechar()
        try:
            var_total = float(total_valor)
        except ValueError:
            var_total = 0.0
        if var_total > 0:
            self.btngravar.config(state="normal")
            self.btnimprimir.config(state="normal")
        else:
            self.txtcodcli.config(state="normal")
            self.btngravar.config(state="disabled")
            self.btnimprimir.config(state="disabled")
    def gravar(self):
        con = Conexao()
        num_venda = self.txtnumvenda.get()
        var_codcli = self.txtcodcli.get()
        var_total = float(self.txt_total.get())
        
        if var_total > 0:
            sql_check = "SELECT COUNT(*) FROM auto_num;"
            cursor = con.db.cursor()
            cursor.execute(sql_check)
            count = cursor.fetchone()[0]
            cursor.close()
            if count == 0:
                sql_insert_initial = "INSERT INTO auto_num (num_venda) VALUES (0);"
                con.gravar(sql_insert_initial)
                print("Valor inicial inserido na tabela auto_num.")
                
            sql_text = "UPDATE auto_num SET num_venda = num_venda + 1 WHERE num_venda >= 0;"
            con.gravar(sql_text)
            sql_text = f"insert into vendas_cab (num_venda, codigo_cli, data_hora, total_venda) values ({num_venda},{var_codcli}, CURRENT_TIMESTAMP, {var_total});"
            print(sql_text)
            con.gravar(sql_text)
            con.fechar()
            
            self.baixa_estoque()
            var_del = messagebox.askyesno("Imprimir", "Deseja Imprimir a Venda?", parent=self.master)
            if var_del:
                self.imprimir()

            # Limpa os campos após o registro
            self.limpar()
            self.limpar_cab()
            self.numeracao()
            self.visualizar()
            self.total()

    def bus_cli(self, event=None):
        con = Conexao()
        print('Você digitou enter')
        var_codcli = self.txtcodcli.get()
        sql_txt = f"select nome from clientes where codigo = {var_codcli}"
        rs = con.consultar(sql_txt)
        if rs:
            self.txtnomecli.config(state="normal")
            self.txtnomecli.delete(0, "end")
            self.txtnomecli.insert(0, rs[0])
            self.txtnomecli.config(state="disabled")
            self.txtcodprod.focus_set()
        else:
            messagebox.showwarning("Aviso", "Cliente Não Encontrado", parent=self.master)
            self.txtnomecli.config(state="normal")
            self.txtcodcli.delete(0, "end")
            self.txtnomecli.delete(0, "end")
            self.txtnomecli.config(state="disabled")
            self.txtcodcli.focus_set()

    def bus_prod(self, event=None):
        con = Conexao()
        var_codprod = self.txtcodprod.get()
        sql_txt = f"select descricao, preco from prodserv where codigo = {var_codprod}"
        rs = con.consultar(sql_txt)
        if rs:
            self.txtdescricao.config(state="normal")
            self.txtdescricao.delete(0, "end")
            self.txtdescricao.insert(0, rs[0])
            self.txtdescricao.config(state="disabled")
            self.lblvlrunit.config(state="normal")
            self.txtvlrunit.delete(0, "end")
            self.txtvlrunit.insert(0, rs[1])
            self.txtvlrunit.config(state="disabled")
            self.txtqtde.focus_set()
        else:
            self.txtcodprod.focus_set()
            messagebox.showwarning("Aviso", "Produto não Encontrado", parent=self.master)

    def entrar_qtde(self, event=None):
        try:
            self.txtvalor.config(state="normal")
            qtde = float(self.txtqtde.get())
            vlr_unit = float(self.txtvlrunit.get())
            if qtde > 0 and vlr_unit > 0:
                valor = qtde * vlr_unit
                self.txtvalor.delete(0, tk.END)
                self.txtvalor.insert(0, f"{valor:.2f}")
                self.btnincluir.focus_set()
            else:
                self.txtvalor.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para quantidade e valor unitário.", parent=self.master)
        finally:
            self.txtvalor.config(state="readonly")

    def cancelar(self):
        var_del = messagebox.askyesno("Cancelar", "Deseja Cancelar a Venda?", parent=self.master)
        if var_del:
            self.limpar()
            self.limpar_cab()
            self.numeracao()
            self.excluir_inic()
            self.visualizar()
            self.total()

    def baixa_estoque(self):
        con = Conexao()
        for child in self.tree.get_children():
            codigo = str(self.tree.item(child)["values"][1])
            quantidade = str(self.tree.item(child)["values"][3])
            sql_text = f"UPDATE prodserv SET quantidade = quantidade - {quantidade} WHERE codigo = '{codigo}';"
            print(sql_text)
            con.gravar(sql_text)
    
    def menu(self):
        self.master.switch_to_menu()

    def hook_imprimir(self):
        imprimir(self=self)