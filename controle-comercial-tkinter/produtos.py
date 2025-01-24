# -*- coding: utf-8 -*-
import platform
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from ProdutoTreeview import ProdutoTreeview
from conexao import Conexao
from router_path import imagemPadrao, imagemSecundaria
import locale

class Produto(tk.Frame):
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
        self.master.title("Controle Comercial - Cadastro de Produtos/Serviços")
        self.master['bg'] = "gold"

        self.tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((larguraTela, alturaTela)))
        tk.Label(self, image=self.tkimage_cli).pack()

        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        self.create_widgets()
        self.txtcodigo.focus_set()

    def create_widgets(self):
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
