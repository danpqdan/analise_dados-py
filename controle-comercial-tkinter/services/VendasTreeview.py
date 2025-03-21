import tkinter as tk
from tkinter import ttk
from conexao import Conexao

class VendasTreeview:
    def __init__(self, parent):
        self.parent = parent
        self.selected_data = None
        self.tree = None
        self.criar_treeview_vendas()

    def criar_treeview_vendas(self):
        # Define o estilo da Treeview
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=("Calibri", 10))
        style.configure("mystyle.Treeview.Heading", font=("Calibri", 12, "bold"))

        # Criação da Treeview
        self.tree = ttk.Treeview(
            self.parent,
            columns=("#1", "#2", "#3", "#4"), 
            show='headings',
            style="mystyle.Treeview"
        )
        

        # Definir as colunas
        self.tree.heading("#1", text="Num venda", command=lambda: self.ordenar_coluna("#1", False))
        self.tree.column("#1", width = 100, anchor ='c')

        self.tree.heading("#2", text="Cod cliente", command=lambda:self.ordenar_coluna("#2", False))
        self.tree.column("#2", width = 80, anchor ='c')

        self.tree.heading("#3", text="Data e hora", command=lambda:self.ordenar_coluna("#3", False))
        self.tree.column("#3", width = 200, anchor ='w')

        self.tree.heading("#4", text="Total da venda", command=lambda:self.ordenar_coluna("#4", False))
        self.tree.column("#4", width = 100, anchor ='c')

        lbl_pes_nome = tk.Label(
            self.parent,
            text="Pesquisar por Num venda:",
            font=('Calibri', 12, 'bold'),
            anchor="w"
        )
        lbl_pes_nome.place(x=50, y=330, width=200, height=25)

        # Registro do comando de pesquisa
        validate_pes_venda = self.parent.register(lambda p: self.pesquisar_num_venda(p))

        self.txt_pes_venda = tk.Entry(
            self.parent,
            width=35,
            font=('Calibri', 12),
            validate='key',
            validatecommand=(validate_pes_venda, '%P')
        )
        self.txt_pes_venda.place(x=210, y=330, width=500, height=25)

        scrollbar = ttk.Scrollbar(self.parent, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x = 731, y = 360,height=120)
        self.tree.place(x=50,y=360,height=120)

        self.visualizar()

    def visualizar(self):
        con=Conexao()
        sql_txt = "select * from vendas_cab order by num_venda"
        rs=con.consultar_tree(sql_txt)

        self.tree.bind("<Double-1>", self.duplo_click)

        for linha in self.tree.get_children():
            self.tree.delete(linha)

        for linha in rs:
            self.tree.insert("", tk.END, values=linha)

    def pesquisar_num_venda(self, p):
        con = Conexao()
        try:
            sql_txt = f"select * from vendas_cab where num_venda like '%{p}%'"
            rs = con.consultar_tree(sql_txt)

            for linha in self.tree.get_children():
                self.tree.delete(linha)

            for linha in rs:
                self.tree.insert("", tk.END, values=linha)

        finally:
            con.fechar()

        return True
    
    def ordenar_coluna(self, col_id: str, reverse: bool) -> None:
        """Função para ordenar a coluna selecionada."""
        def tratar_valor(valor):
            """Função para tratar o valor da célula antes da ordenação."""
            try:
                return float(valor) if '.' in valor or valor.isdigit() else int(valor)
            except ValueError:
                return valor.lower()

        itens = [(tratar_valor(self.tree.set(k, col_id)), k) for k in self.tree.get_children("")]
        itens.sort(reverse=reverse, key=lambda x: x[0])
        
        for index, (_, k) in enumerate(itens):
            self.tree.move(k, '', index)

        self.tree.heading(col_id, command=lambda: self.ordenar_coluna(col_id, not reverse))
    
    def duplo_click(self, event):
        item_selecionado = self.tree.selection()
        if item_selecionado:
            valores = self.tree.item(item_selecionado[0], "values")
            return valores 
        return []