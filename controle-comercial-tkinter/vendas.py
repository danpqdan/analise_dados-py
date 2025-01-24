# -*- coding: utf-8 -*-
import locale
import os

import platform
from conexao import Conexao
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date

from ClienteTreeview import ClienteTreeview
from ProdutoTreeview import ProdutoTreeview
from conexao import Conexao
from router_path import imagemSecundaria


class Vendas(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        larguraTela = self.master.winfo_screenwidth()
        alturaTela = self.master.winfo_screenheight()
        self.master.geometry(f'{larguraTela}x{alturaTela}+0+0')

        self.tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((larguraTela, alturaTela)))
        tk.Label(self, image=self.tkimage_cli).grid()

        self.create_widgets()
        self.numeracao()
        self.excluir_inic()
        self.visualizar()
        self.total()
        self.txtnumvenda.config(state="disabled")
        self.txtcodcli.focus_set()

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

    def imprimir(self):
        # Cabeçalho do Relatório
        today = date.today()
        d3 = today.strftime("%d/%m/%y")
            
        cnv = canvas.Canvas("vendas.pdf")
        width, height = A4
        print("Largura= ", width, "  Altura= ", height)

        cnv.setFont('Times-Roman', 14)
        cnv.setFillColorRGB(0, 0, 255)

        cnv.drawString(1, 820, "Sistema Comercial 1.0")

        cnv.setFont('Times-Bold', 14)
        cnv.setFillColorRGB(255, 0, 0)

        cnv.drawString(250, 820, "Pedido de Vendas")

        cnv.setFont('Times-Roman', 14)
        cnv.setFillColorRGB(0, 0, 255)

        cnv.drawString(540, 820, d3)

        # Cabeçalho do Pedido
        cnv.setLineWidth(2)
        cnv.line(0, 810, 595, 810)

        cnv.setFont('Times-Roman', 12)
        cnv.setFillColorRGB(0, 0, 0)

        cnv.drawString(10, 780, "Número do Pedido: " + self.txtnumvenda.get())
        cnv.drawString(200, 780, "Data do Pedido:   " + d3)
        
        cnv.drawString(10, 750, "Código do Cliente: " + self.txtcodcli.get())
        cnv.drawString(200, 750, "Nome do Cliente:  " + self.txtnomecli.get())

        cnv.setLineWidth(1)
        cnv.line(0, 720, 595, 720)

        # Linhas do Pedido
        cnv.setFont('Times-Bold', 12)
        cnv.drawString(1, 700, "Lin")
        cnv.drawString(40, 700, "Cod. Prod")
        cnv.drawString(130, 700, "Descrição")
        cnv.drawString(320, 700, "Quantidade")
        cnv.drawString(430, 700, "Valor Unitário")
        cnv.drawString(530, 700, "Valor")
        cnv.setFont('Times-Roman', 12)
        
        linha = 680
        for child in self.tree.get_children():
            print(self.tree.item(child)["values"])
            
            cnv.drawString(1, linha, str(self.tree.item(child)["values"][0]))
            cnv.drawString(40, linha, str(self.tree.item(child)["values"][1]))
            cnv.drawString(130, linha, self.tree.item(child)["values"][2])
            cnv.drawString(320, linha, str(self.tree.item(child)["values"][3]))
            cnv.drawString(430, linha, locale.currency(float(self.tree.item(child)["values"][4])))
            cnv.drawString(530, linha, locale.currency(float(self.tree.item(child)["values"][5])))

            linha = linha - 20

        # Total do Pedido
        cnv.line(0, linha, 595, linha)
        linha = linha - 20

        cnv.setFont('Times-Bold', 12)
        cnv.drawString(420, linha, "Total do Pedido ->")
        cnv.drawString(530, linha, locale.currency(float(self.txt_total.get().strip())))
        
        cnv.save()

        if platform.system() == "Windows":
            os.startfile("vendas.pdf")
        else:
            os.system("xdg-open vendas.pdf")
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

    def create_widgets(self):
        lblnumvenda = tk.Label(self, text="Núm. Venda:", font=('Calibri', 12, 'bold'), bg='lightskyblue', fg='black', anchor='w')
        lblnumvenda.place(x=50, y=25, width=100, height=20)

        self.txtnumvenda = tk.Entry(self, justify='center', font=('Calibri', 12, 'bold'))
        self.txtnumvenda.place(x=160, y=25, width=100, height=20)

        lblcodcli = tk.Label(self, text="Cod. Cliente:", font=('Calibri', 12, 'bold'), bg='lightskyblue', fg='black', anchor='w')
        lblcodcli.place(x=50, y=60, width=100, height=20)

        self.txtcodcli = tk.Entry(self)
        self.txtcodcli.place(x=160, y=60, width=100, height=20)
        self.txtcodcli.bind('<Return>', self.bus_cli)

        btnbuscli = tk.Button(self, text="Buscar cliente", bg='gold', foreground='black', font=('Calibri', 12, 'bold'), command=self.abrir_popup_busca_cliente)
        btnbuscli.place(x=280, y=50, width=120, height=30)

        lblnomecli = tk.Label(self, text="Nome Cliente:", font=('Calibri', 12, 'bold'), bg='lightskyblue', fg='black', anchor='w')
        lblnomecli.place(x=50, y=100, width=100, height=20)

        self.txtnomecli = tk.Entry(self)
        self.txtnomecli.place(x=160, y=100, width=560, height=20)
        self.txtnomecli.config(state="disabled")

        lblcodprod = tk.Label(self, text="Cód. Prod:", font=('Calibri', 10, 'bold'), bg='lightskyblue', fg='black', anchor='w')
        lblcodprod.place(x=50, y=160, width=100, height=20)

        btnbusprod = tk.Button(self, text="Buscar produto", bg='gold', foreground='black', font=('Calibri', 12, 'bold'), command=self.abrir_popup_busca_prodserv)
        btnbusprod.place(x=280, y=160, width=120, height=30)

        self.txtcodprod = tk.Entry(self)
        self.txtcodprod.place(x=160, y=160, width=100, height=20)
        self.txtcodprod.bind('<Return>', self.bus_prod)

        lbldescricao = tk.Label(self, text="Descrição:", font=('Calibri', 10, 'bold'), bg='lightskyblue', fg='black', anchor='w')
        lbldescricao.place(x=50, y=200, width=100, height=20)

        self.txtdescricao = tk.Entry(self)
        self.txtdescricao.place(x=160, y=200, width=560, height=20)

        lblqtde = tk.Label(self, text="Quantidade:", font=('Calibri', 10, 'bold'), bg='lightskyblue', fg='black', anchor='w')
        lblqtde.place(x=50, y=240, width=100, height=20)

        self.txtqtde = tk.Entry(self)
        self.txtqtde.place(x=160, y=240, width=100, height=20)
        self.txtqtde.bind('<FocusOut>', self.entrar_qtde)
        self.txtqtde.bind('<Return>', self.entrar_qtde)

        self.btnincluir = tk.Button(self, text="Incluir - F1", bg='gold', foreground='black', font=('Calibri', 12, 'bold'), command=self.gravar_lin)
        self.btnincluir.place(x=160, y=290, width=100, height=30)
        self.master.bind('<F1>', self.finalizar_linha)
        self.btnincluir.bind('<Button-1>', self.finalizar_linha)
        self.btnincluir.bind('<Return>', self.finalizar_linha)

        self.lblvlrunit = tk.Label(self, text="Valor Unit:", font=('Calibri', 10, 'bold'), bg='lightskyblue', fg='black', anchor='w')
        self.lblvlrunit.place(x=280, y=240, width=100, height=20)
        self.lblvlrunit.config(state="disabled")

        self.txtvlrunit = tk.Entry(self)
        self.txtvlrunit.place(x=390, y=240, width=100, height=20)

        lblvalor = tk.Label(self, text="Valor:", font=('Calibri', 10, 'bold'), bg='lightskyblue', fg='black', anchor='w')
        lblvalor.place(x=510, y=240, width=100, height=20)

        self.txtvalor = tk.Entry(self)
        self.txtvalor.place(x=620, y=240, width=100, height=20)
        self.txtvalor.config(state="disabled")

        lbltotal = tk.Label(self, text="Total ->", font=('Calibri', 16, 'bold'), bg='lightskyblue', fg="black", anchor='c')
        lbltotal.place(x=548, y=520, width=100, height=40)

        self.txt_total = tk.Entry(self, justify='center', bg="silver", fg="blue", font=('Calibri', 16, 'bold'))
        self.txt_total.place(x=650, y=520, width=150, height=40)
        self.txt_total.config(state="readonly")

        btnlimpar = tk.Button(self, text="Limpar - F2", bg='gold', foreground='black', font=('Calibri', 12, 'bold'), command=self.limpar)
        btnlimpar.place(x=390, y=290, width=100, height=30)
        btnlimpar.bind('<Button-1>', self.limpar)
        self.master.bind('<F2>', self.limpar)

        btnexcluir = tk.Button(self, text="Excluir", bg='gold', foreground='black', font=('Calibri', 12, 'bold'), command=self.excluir)
        btnexcluir.place(x=620, y=290, width=100, height=30)

        self.btngravar = tk.Button(self, text="Gravar", bg='black', foreground='white', font=('Calibri', 12, 'bold'), command=self.gravar)
        self.btngravar.place(x=160, y=600, width=100, height=50)

        self.btnimprimir = tk.Button(self, text="Imprimir", bg='green', foreground='white', font=('Calibri', 12, 'bold'), command=self.imprimir)
        self.btnimprimir.place(x=280, y=600, width=100, height=50)

        self.btncancelar = tk.Button(self, text="Cancelar", bg='red', foreground='white', font=('Calibri', 12, 'bold'), command=self.cancelar)
        self.btncancelar.place(x=400, y=600, width=100, height=50)

        self.btnmenu = tk.Button(self, text="Menu", bg='yellow', foreground='black', font=('Calibri', 12, 'bold'), command=self.menu)
        self.btnmenu.place(x=520, y=600, width=100, height=50)

        style = ttk.Style()
        style.configure("mystyle.Treeview", font=("Calibri", 10))
        style.configure("mystyle.Treeview.Heading", font=("Calibri", 12, "bold"))

        self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', style="mystyle.Treeview", padding=0)
        self.tree.column("#1", width=50, anchor='c')
        self.tree.heading("#1", text="Linha")
        self.tree.column("#2", width=100, anchor='c')
        self.tree.heading("#2", text="Código")
        self.tree.column("#3", width=200, anchor='w')
        self.tree.heading("#3", text="Descrição")
        self.tree.column("#4", width=150, anchor='c')
        self.tree.heading("#4", text="Quantidade")
        self.tree.column("#5", width=100, anchor='c')
        self.tree.heading("#5", text="Valor Unit")
        self.tree.column("#6", width=150, anchor='c')
        self.tree.heading("#6", text="Valor")
        self.tree.place(x=50, y=350, height=180)

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=801, y=350, height=180)

        
