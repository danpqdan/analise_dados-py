# -*- coding: utf-8 -*-
import platform
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
from PIL import Image, ImageTk
import conexao
from router_path import dir, imagemPadrao, imagemSecundaria


import locale

print(__name__)
if __name__ == '__main__': 
    tela_prod = tk.Tk()
else:
    tela_prod = tk.Toplevel()

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

tela_prod.geometry('1366x768+0+0')
if platform.system() == "Windows":
    tela_prod.state('zoomed')
else:
    tela_prod.attributes('-zoomed', True)
tela_prod['bg'] = "gold"
tela_prod.title("Controle Comercial - Cadastro de Produtos/Serviços")

tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((tela_prod.winfo_screenwidth(), tela_prod.winfo_screenheight())))
tk.Label(tela_prod, image=tkimage_cli).pack()

def limpar():
    txtcodigo.delete(0,"end")
    txtdescricao.delete(0,"end")
    cmbtipo.delete(0,"end")
    txtquantidade.delete(0,"end")
    txtcusto.delete(0,"end")
    txtpreco.delete(0,"end")
    txtcodigo.focus_set()

def buscar():
    var_codigo = txtcodigo.get()
 
    con=conexao.conexao()
    sql_txt = f"select codigo,descricao,tipo,quantidade,custo,preco from prodserv where codigo = {var_codigo}"
    rs=con.consultar(sql_txt)

    if rs:
    
        limpar()

        txtcodigo.insert(0, rs[0])
        txtdescricao.insert(0, rs[1])
        cmbtipo.insert(0,rs[2])
        txtquantidade.insert(0,rs[3])
        txtcusto.insert(0,locale.currency(rs[4]))
        txtpreco.insert(0,locale.currency(rs[5]))
    else:
        messagebox.showwarning("Aviso", "Código não Encontrado",parent = tela_prod)
        limpar()
        txtcodigo.focus_set()

    con.fechar()

def duplo_click(event):
    limpar()
    item = tree.selection()
    if item:
        values = tree.item(item, "values")
        txtcodigo.delete(0, tk.END)
        txtcodigo.insert(0, values[0])
        buscar()

def visualizar():
    con=conexao.conexao()
    #sql_txt = "select codigo,descricao,tipo,quantidade,custo,preco from prodserv order by descricao"
    sql_txt = "select * from prodserv order by descricao"
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

def gravar():
    var_codigo = txtcodigo.get()
    var_tipo = cmbtipo.get()
    var_descricao = txtdescricao.get()
    var_quantidade = txtquantidade.get()
    var_custo = txtcusto.get()
    var_custo = float(var_custo.replace('R$', '').strip().replace('.', '').replace(',', '.'))
    var_preco = txtpreco.get()
    var_preco = float(var_preco.replace('R$', '').strip().replace('.', '').replace(',', '.'))

    con=conexao.conexao()
    sql_txt = f"select codigo,descricao,tipo,quantidade,custo,preco from prodserv where codigo = '{var_codigo}'"

    rs=con.consultar(sql_txt)

    if rs:
        sql_text = f"update prodserv set tipo='{var_tipo}',descricao='{var_descricao}',quantidade={var_quantidade},custo={var_custo},preco={var_preco} where codigo = '{var_codigo}'"
    else:
        sql_text = f"insert into prodserv(codigo,tipo,descricao,quantidade,custo,preco) values ('{var_codigo}','{var_tipo}','{var_descricao}',{var_quantidade},{var_custo},{var_preco})"

    if con.gravar(sql_text):
        messagebox.showinfo("Aviso", "Item Gravado com Sucesso",parent = tela_prod)
        limpar()
    else:
        messagebox.showerror("Erro", "Houve um Erro na Gravação",parent = tela_prod)

    con.fechar()

    visualizar()

def excluir():
    var_del = messagebox.askyesno("Exclusão", "Tem certeza que deseja excluir?",parent = tela_prod)
    if var_del == True:
        var_codigo = txtcodigo.get()

        con=conexao.conexao()
        sql_text = f"delete from prodserv where codigo = '{var_codigo}'"
        if con.gravar(sql_text):
              messagebox.showinfo("Aviso", "Item Excluído com Sucesso",parent = tela_prod)
              limpar()
        else:
            messagebox.showerror("Erro", "Houve um Erro na Exclusão",parent = tela_prod)

        con.fechar()

        visualizar()
    else:
        limpar()

def menu():
    tela_prod.destroy()

def limitar_tamanho(p,limite):
    if len(p) > int(limite):
        return False
    return True

tela_prod.geometry('1366x768+0+0')
if platform.system() == "Windows":
    tela_prod.state('zoomed')
else:
    tela_prod.attributes('-zoomed', True)
tela_prod['bg'] = "gold"
tela_prod.title("Controle Comercial - Cadastro de Produtos/Serviço")

limite_campo = tela_prod.register(func=limitar_tamanho)

lblcodigo = tk.Label(tela_prod, text ="Codigo:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = 'w')
lblcodigo.place(x = 50, y = 20, width = 90)
txtcodigo =  tk.Entry(tela_prod, validate='key', font=('Calibri', 12), validatecommand=(limite_campo,'%P',13))
txtcodigo.place(x = 150, y = 20, width = 120)


buscabtn = tk.Button(tela_prod, text ="Pesquisar", 
                      bg ='white',foreground='black', font=('Calibri', 12), command = buscar)
buscabtn.place(x = 290, y = 20, width = 80, height = 25)
  
lbltipo = tk.Label(tela_prod, text ="Tipo:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = 'w')
lbltipo.place(x = 50, y = 60, width = 90)
tipos = ["PRODUTO", "SERVICO", "OUTROS"]
cmbtipo = ttk.Combobox(tela_prod, values=tipos, font=('Calibri', 12))
cmbtipo.place(x=150, y=60, width=120, height = 25)
#cmbtipo.current(0)

lbldescricao = tk.Label(tela_prod, text ="Descrição:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = 'w')
lbldescricao.place(x = 50, y = 100, width = 90)
entry = tk.Entry(tela_prod, font=('Calibri', 12))
txtdescricao =  tk.Entry(tela_prod, font=('Calibri', 12), validate='key', validatecommand=(limite_campo,'%P',60))
txtdescricao.place(x = 150, y = 100, width = 400)

lblquantidade = tk.Label(tela_prod, text ="Quantidade:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = 'w')
lblquantidade.place(x = 50, y = 140, width = 90)
txtquantidade = tk.Entry(tela_prod, font=('Calibri', 12),  validate='key', validatecommand=(limite_campo,'%P',6))
txtquantidade.place(x = 150, y = 140, width = 120)

lblcusto = tk.Label(tela_prod, text ="Custo:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = 'w')
lblcusto.place(x = 50, y = 180, width = 90)
txtcusto = tk.Entry(tela_prod, font=('Calibri', 12), validate='key', validatecommand=(limite_campo,'%P',13))
txtcusto.place(x = 150, y = 180, width = 120)

lblpreco = tk.Label(tela_prod, text ="Preço:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = 'w')
lblpreco.place(x = 50, y = 220, width = 90)
txtpreco = tk.Entry(tela_prod, font=('Calibri', 12), validate='key', validatecommand=(limite_campo,'%P',13))
txtpreco.place(x = 150, y = 220, width = 120)


btngravar = tk.Button(tela_prod, text ="Gravar", 
                      bg ='black',foreground='white', font=('Calibri', 12), command = gravar)
btngravar.place(x = 150, y = 280, width = 65)

btnexcluir = tk.Button(tela_prod, text ="Excluir", 
                      bg ='red',foreground='white', font=('Calibri', 12), command = excluir)
btnexcluir.place(x = 230, y = 280, width = 65)

bntlimpar = tk.Button(tela_prod, text ="Limpar", 
                      bg ='green',foreground='white', font=('Calibri', 12), command = limpar)
bntlimpar.place(x = 310, y = 280, width = 65)

btnmneu = tk.Button(tela_prod, text ="Menu", 
                      bg ='yellow',foreground='black', font=('Calibri', 12), command = menu)
btnmneu.place(x = 390, y = 280, width = 65)

style = ttk.Style()

style.configure("mystye.Treeview", font=("Calibri", 10))
style.configure("mystyle.Treeview.Heading", font=("Calibri", 12, "bold"))
 


'''
    Colunas de produtos
'''
def ordenar_coluna(tree: Treeview, col_id: str, reverse: bool) -> None:
    def tratar_valor(valor):
            """Função para tratar o valor da célula antes da ordenação."""
            try:
                float(valor) 
                if '.' in valor or valor.isdigit():
                    return float(valor)    
                else: 
                    return int(valor)
            except ValueError: 
                return valor.lower()
        
    itens = [(tratar_valor(tree.set(k, col_id)), k) for k in tree.get_children("")]    
    itens.sort(reverse=reverse, key=lambda x: x[0])
    for index, (_, k) in enumerate(itens):
        tree.move(k, '', index)
    
    tree.heading(col_id, command=lambda:ordenar_coluna(tree, col_id, not reverse))

# 
tree = ttk.Treeview(tela_prod, column=("Código", "Tipo", "Descrição", "Quantidade", "Custo", "Preço"), show='headings', style="mystyle.Treeview", padding=0)

tree.columnconfigure(0, weight=1)
tree.rowconfigure(0, weight=1)

tree.heading("#1", text="Código", command=lambda:ordenar_coluna(tree, "#1", False) )
tree.column("#1", width = 100, anchor ='c')

tree.heading("#2", text="Tipo", command=lambda:ordenar_coluna(tree, "#2", False))
tree.column("#2", width = 80, anchor ='c')

tree.heading("#3", text="Descrição", command=lambda:ordenar_coluna(tree, "#3", False))
tree.column("#3", width = 200, anchor ='w')

tree.heading("#4", text="Quantidade", command=lambda:ordenar_coluna(tree, "#4", False))
tree.column("#4", width = 100, anchor ='c')

tree.heading("#5", text="Custo", command=lambda:ordenar_coluna(tree, "#5", False))
tree.column("#5", width = 100, anchor ='c')

tree.heading("#6", text="Preço", command=lambda:ordenar_coluna(tree, "#6", False))
tree.column("#6", width = 100, anchor ='c')

 
tree.place(x=50,y=360,height=120)

scrollbar = ttk.Scrollbar(tela_prod, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x = 731, y = 360,height=120)

visualizar()

txtcodigo.focus_set()

tela_prod.mainloop()

