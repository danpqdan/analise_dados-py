import tkinter as tk
from tkinter import ttk
import conexao

class ClienteTreeview:
    def __init__(self, parent):
        self.parent = parent
        self.selected_data = None
        self.tree = None
        self.criar_treeview_cliente()

    def criar_treeview_cliente(self):
        # Define o estilo da Treeview
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=("Calibri", 10))
        style.configure("mystyle.Treeview.Heading", font=("Calibri", 12, "bold"))

        # Criação da Treeview
        self.tree = ttk.Treeview(
            self.parent,
            column=("c1", "c2", "c3", "c4", "c5"),
            show='headings',
            style="mystyle.Treeview"
        )

        # Definir as colunas
        self.tree.heading("#1", text="Código")
        self.tree.column("#1", width=100, anchor='c')

        self.tree.heading("#2", text="Nome")
        self.tree.column("#2", width=200, anchor='c')

        self.tree.heading("#3", text="Telefone")
        self.tree.column("#3", width=100, anchor='w')

        self.tree.heading("#4", text="E-mail")
        self.tree.column("#4", width=150, anchor='c')

        self.tree.heading("#5", text="Observação")
        self.tree.column("#5", width=300, anchor='c')

        self.tree.place(x=50, y=50, width=700, height=300)

        # Label e campo de pesquisa
        lbl_pes_nome = tk.Label(
            self.parent,
            text="Pesquisar por Nome:",
            font=('Calibri', 12, 'bold'),
            anchor="w"
        )
        lbl_pes_nome.place(x=50, y=390, width=200, height=25)

        # Registro do comando de pesquisa
        validate_pes_nome = self.parent.register(lambda p: self.pesquisar_nome(p))

        self.txt_pes_nome = tk.Entry(
            self.parent,
            width=35,
            font=('Calibri', 12),
            validate='key',
            validatecommand=(validate_pes_nome, '%P')
        )
        self.txt_pes_nome.place(x=210, y=390, width=500, height=25)
        scrollbar = ttk.Scrollbar(self.parent, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.place(x=50, y=420, width=900, height=200)


        # Inicializa a exibição dos dados
        self.visualizar()

    def pesquisar_nome(self, p):
        con = conexao.conexao()
        try:
            sql_txt = f"select * from clientes where nome like '%{p}%'"
            rs = con.consultar_tree(sql_txt)

            for linha in self.tree.get_children():
                self.tree.delete(linha)

            for linha in rs:
                self.tree.insert("", tk.END, values=linha)

        finally:
            con.fechar()

        return True

    def duplo_click(self, event):
        item = self.tree.item(self.tree.selection())
        if item:
            self.selected_data = item['values']
            return self.selected_data

    def visualizar(self):
        con = conexao.conexao()
        sql_txt = f"select * from clientes"
        rs = con.consultar_tree(sql_txt)

        for linha in self.tree.get_children():
            self.tree.delete(linha)

        for linha in rs:
            self.tree.insert("", tk.END, values=linha)

        con.fechar()
