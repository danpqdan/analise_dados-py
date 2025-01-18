# -*- coding: utf-8 -*-
import os

import platform
import conexao
import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter import messagebox
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from router_path import dir, imagemPadrao, imagemSecundaria
from ClienteTreeview import ClienteTreeview
from ProdutoTreeview import ProdutoTreeview

import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

if __name__ == '__main__': 
    tela_venda = tk.Tk()
else:
    tela_venda = tk.Toplevel()

larguraTela = tela_venda.winfo_screenwidth()
alturaTela = tela_venda.winfo_screenheight()

tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((tela_venda.winfo_screenwidth(), tela_venda.winfo_screenheight())))
tk.Label(tela_venda, image=tkimage_cli).pack()


def abrir_popup_busca_cliente():
    popup_busca = tk.Toplevel(tela_venda)
    popup_busca.title("Buscar Cliente")
    popup_busca.geometry("700x500")
    popup_busca.resizable(True, True)
    tree = ClienteTreeview(popup_busca)
    tree.tree.place(x=50, y=50, width=600, height=300)
    
    def handle_duplo_click(event):
        valores = tree.duplo_click(event)
        print(f"Dados selecionados: {valores}")
        if valores:
            txtcodcli.delete(0, tk.END)
            txtcodcli.insert(0, valores[0])
        popup_busca.destroy()
        event= 36
        txtcodcli.focus
        bus_cli()
    tree.tree.bind("<Double-1>", handle_duplo_click)

def abrir_popup_busca_prodserv():
    popup_busca = tk.Toplevel(tela_venda)
    popup_busca.title("Buscar Cliente")
    popup_busca.geometry("700x500")
    popup_busca.resizable(True, True)
    tree = ProdutoTreeview(popup_busca)
    tree.tree.place(x=50, y=50, width=600, height=300)
    
    def handle_duplo_click(event):
        valores = tree.duplo_click(event)
        print(f"Dados selecionados: {valores}")
        if valores:
            txtcodprod.delete(0, tk.END)
            txtcodprod.insert(0, valores[0])
            txtcodprod.focus
        popup_busca.destroy()
        event= 36
        txtcodcli.focus
        bus_prod()
    tree.tree.bind("<Double-1>", handle_duplo_click)


def numeracao():

    txtnumvenda.config(state= "normal")
    
    con=conexao.conexao()
    sql_txt = "select num_venda + 1 as num_venda from  auto_num"
    rs=con.consultar(sql_txt)

    if rs:
        txtnumvenda.delete(0,"end")
        txtnumvenda.insert(0, rs[0])

    txtnumvenda.config(state= "disabled")
    

def limpar(event=None):
    print("Limpar acionado!")
    txtdescricao.config(state= "normal")
    txtvlrunit.config(state= "normal")
    txtvalor.config(state= "normal")
    txtcodprod.delete(0,"end")
    txtdescricao.delete(0,"end")
    txtqtde.delete(0,"end")
    txtvlrunit.delete(0,"end")
    txtvalor.delete("0","end")
    txtcodprod.focus_set()

def limpar_cab():
    txtcodcli.config(state= "normal")
    txtnomecli.config(state= "normal") 
    txtnumvenda.delete(0,"end")
    txtnomecli.delete(0,"end")
    txtcodcli.delete(0,"end")
    txtcodcli.focus_set()


def gravar_lin():
    num_venda = txtnumvenda.get()
    var_codcli = txtcodcli.get()
    var_codprod = txtcodprod.get()
    var_qtde = txtqtde.get()
    var_vlrunit = txtvlrunit.get()
    var_valor = txtvalor.get()

    if var_codcli == "":
         messagebox.showwarning("Aviso", "Favor preencher o código do cliente",parent = tela_venda)
         txtcodcli.focus_set()
    else:
         if var_codprod == "":
             messagebox.showwarning("Aviso", "Favor preencher o código do produto" ,parent = tela_venda)
             txtcodprod.focus_set()
         else:
             if var_qtde == "":
                 messagebox.showwarning("Aviso", "Favor preencher a quantidade" ,parent = tela_venda)
                 txtqtde.focus_set()
             else:
                 con=conexao.conexao()
                 sql_txt = f"select IFNULL(max(lin_venda),0)+1 as lin_venda from vendas_lin where num_venda = {num_venda}"
                 rs=con.consultar(sql_txt)
                 var_lin_venda = rs[0]
                 sql_text = f"insert into vendas_lin (num_venda, lin_venda, codigo_prod, quantidade, valor_unit, valor) values ({num_venda},'{var_lin_venda}','{var_codprod}','{var_qtde}','{var_vlrunit}','{var_valor}')"
                 if con.gravar(sql_text):
                     limpar()
                 else:
                     print(sql_text)

    

def finalizar_linha(event:None):
    gravar_lin()
    visualizar()
    total()


def excluir():
    num_venda = txtnumvenda.get()

    item = tree.item(tree.selection())
    try:
        lin_venda = item['values'][0]

        con=conexao.conexao()
        sql_text = f"delete from vendas_lin where num_venda = {num_venda} and lin_venda = {lin_venda}"
        print(sql_text)
        if con.gravar(sql_text):
            visualizar()
            total()
    except:
        messagebox.showwarning("Aviso", "Necessário Selecionar uma Linha antes de Clicar em Excluir",parent = tela_venda)

def excluir_inic():
    num_venda = txtnumvenda.get()

    item = tree.item(tree.selection())
    con=conexao.conexao()
    sql_text = f"delete from vendas_lin where num_venda = {num_venda}"
    con.gravar(sql_text)


        
def visualizar():
    
    num_venda = txtnumvenda.get()
    print("Num_venda", num_venda)
    
    con=conexao.conexao()
    sql_txt = (f"select A.lin_venda, A.codigo_prod, B.descricao, A.quantidade, A.valor_unit, A.valor " +
               f"from vendas_lin A, prodserv B where A.num_venda = {num_venda} and A.codigo_prod = B.codigo order by A.num_venda, A.lin_venda")
    rs=con.consultar_tree(sql_txt)


    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

    con.fechar()          

def total():
    num_venda = txtnumvenda.get()
    
    con=conexao.conexao()
    sql_txt = f"select IFNULL(sum(A.valor),0) as valor from vendas_lin A where A.num_venda = {num_venda}"
    rs=con.consultar(sql_txt)

    if rs:
        txt_total.config(state= "normal")
        # txt_total.config(state= "readonly")
        txt_total.delete("0","end")
        txt_total.insert(0, rs[0])
        

    var_total = float(txt_total.get())
    
    if var_total >0:
        txtcodcli.config(state= "disabled")
        btngravar.config(state= "normal")
        btnimprimir.config(state= "normal")
    else:
        txtcodcli.config(state= "normal")
        btngravar.config(state= "disabled")
        btnimprimir.config(state= "disabled")
        

    con.fechar()        
    
def gravar():

    num_venda = txtnumvenda.get()
    var_codcli = txtcodcli.get()

    var_total = float(txt_total.get())
    
    var_total = float(txt_total.get())
    if var_total >0:
        con=conexao.conexao()
        sql_text = "update auto_num set num_venda = num_venda + 1 where num_venda >=0;"
        con.gravar(sql_text)
             
        sql_text = f"insert into vendas_cab (num_venda, codigo_cli, data_hora, total_venda) values ({num_venda},{var_codcli}, now() , {var_total});"
        print(sql_text)
        con.gravar(sql_text)

        con.fechar()

        baixa_estoque()

        var_del = messagebox.askyesno("Imprimir", "Deseja Imprimir a Venda?",parent = tela_venda)
        if var_del==True:
            imprimir()
            
        limpar()
        limpar_cab()
        numeracao()
        visualizar()
        total()


def bus_cli(event=None):
      print('Você digitou enter')
      var_codcli = txtcodcli.get()
    
      con=conexao.conexao()
      sql_txt = f"select nome from clientes where codigo = {var_codcli}"
      rs=con.consultar(sql_txt)
      if rs:
          txtnomecli.config(state= "normal")
          
          txtnomecli.delete(0,"end")
          txtnomecli.insert(0, rs[0])
          
          txtnomecli.config(state= "disabled")
          
          txtcodprod.focus_set()
          
      else:
          messagebox.showwarning("Aviso", "Cliente Não Encontrado",parent = tela_venda)
          txtnomecli.config(state= "normal")
          
          txtcodcli.delete(0,"end")
          txtnomecli.delete(0,"end")
          txtnomecli.config(state= "disabled")
          
          txtcodcli.focus_set()
          
      con.fechar()

def bus_prod(event=None):
    var_codprod = txtcodprod.get()
 
    con=conexao.conexao()
    sql_txt = f"select descricao, preco from prodserv where codigo = {var_codprod}"
    rs=con.consultar(sql_txt)
    if rs:
        txtdescricao.config(state= "normal")
        txtdescricao.delete(0,"end")
        txtdescricao.insert(0, rs[0])
        txtdescricao.config(state= "disabled")
        lblvlrunit.config(state= "normal")
        txtvlrunit.delete(0,"end")
        txtvlrunit.insert(0, rs[1])
        txtvlrunit.config(state= "disabled")
        txtqtde.focus_set()
    else:
        txtcodprod.focus_set()
        messagebox.showwarning("Aviso", "Produto não Encontrado",parent = tela_venda)
        
    con.fechar()

def entrar_qtde(event=None):
    txtvalor.config(state="normal")
    qtde = float(txtqtde.get())
    vrl_unit = float(txtvlrunit.get())
    if qtde > 0 and vrl_unit > 0:
        valor = qtde * vrl_unit
        txtvalor.delete(0, tk.END)
        txtvalor.insert(0, valor)
        btnincluir.focus_set()
    else:
        txtvalor.delete(0, tk.END)


def cancelar():
    var_del = messagebox.askyesno("Cancelar", "Deseja Cancelar a Venda?",parent = tela_venda)
    if var_del==True:
        limpar()
        limpar_cab()
        numeracao()
        excluir_inic()
        visualizar()
        total()
    
def imprimir():
    # Cabeçalho do Relatório
    today = date.today()
    d3 = today.strftime("%d/%m/%y")
        
    cnv = canvas.Canvas("vendas.pdf")
    width, height = A4
    print("Largura= ",width,"  Altura= ", height)

    cnv.setFont('Times-Roman', 14)
    cnv.setFillColorRGB(0, 0, 255)

    cnv.drawString(1,820,"Sistema Comercial 1.0")

    cnv.setFont('Times-Bold', 14)
    cnv.setFillColorRGB(255, 0, 0)

    cnv.drawString(250,820,"Pedido de Vendas")

    cnv.setFont('Times-Roman', 14)
    cnv.setFillColorRGB(0, 0, 255)

    cnv.drawString(540,820,d3)

    # Cabeçalho do Pedido
    cnv.setLineWidth(2)
    cnv.line(0, 810, 595, 810)

    cnv.setFont('Times-Roman', 12)
    cnv.setFillColorRGB(0 ,0, 0)

    cnv.drawString(10,780, "Número do Pedido: " + txtnumvenda.get())
    cnv.drawString(200,780,"Data do Pedido:   " + d3)
    
    
    cnv.drawString(10,750 ,"Código do Cliente: " + txtcodcli.get())
    cnv.drawString(200,750,"Nome do Cliente:  " + txtnomecli.get())

    cnv.setLineWidth(1)
    cnv.line(0, 720, 595, 720)

    # Linhas do Pedido
    cnv.setFont('Times-Bold', 12)
    cnv.drawString(1,700,"Lin")
    cnv.drawString(40,700,"Cod. Prod")
    cnv.drawString(130,700,"Descrição")
    cnv.drawString(320,700,"Quantidade")
    cnv.drawString(430,700,"Valor Unítario")
    cnv.drawString(530,700,"Valor")
    cnv.setFont('Times-Roman', 12)
    
    linha = 680
    for child in tree.get_children():

        print(tree.item(child)["values"])
        
        cnv.drawString(1,linha, str(tree.item(child)["values"][0]))
        cnv.drawString(40,linha,str(tree.item(child)["values"][1]))
        cnv.drawString(130,linha,tree.item(child)["values"][2])
        cnv.drawString(320,linha,str(tree.item(child)["values"][3]))
        cnv.drawString(430,linha,locale.currency(float(tree.item(child)["values"][4])))
        cnv.drawString(530,linha,locale.currency(float(tree.item(child)["values"][5])))

        linha = linha - 20

    # Total do Pedido
    cnv.line(0, linha, 595, linha)
    linha = linha - 20

    cnv.setFont('Times-Bold', 12)
    cnv.drawString(420,linha,"Total do Pedido ->")
    cnv.drawString(530,linha, locale.currency(float(txt_total.get())))
    

    cnv.save()

    if platform.system() == "Windows":
        os.startfile("vendas.pdf")
    else:
        os.system("xdg-open vendas.pdf")
def baixa_estoque():
   for child in tree.get_children():

        codigo = str(tree.item(child)["values"][1])
        quantidade = str(tree.item(child)["values"][3])

       
        con=conexao.conexao()
        sql_text = f"update prodserv set quantidade = quantidade - {quantidade} where codigo = '{codigo}';"
        print(sql_text)
        con.gravar(sql_text)
        con.fechar()

def menu():
    tela_venda.destroy()
    

tela_venda.geometry('1366x768+0+0')
if platform.system() == "Windows":
    tela_venda.state('zoomed')
else:
    tela_venda.attributes('-zoomed', True)
tela_venda['bg'] = "dimgray"
tela_venda.title("Controle Comercial - Vendas")


lblnumvenda = tk.Label(tela_venda, text="Núm. Venda:", font=('Calibri', 12, 'bold'), bg='lightskyblue', fg='black', anchor='w')
lblnumvenda.place(x = 50, y = 25, width = 100, height=20)

txtnumvenda = tk.Entry(tela_venda, justify='center', font=('Calibri', 12, 'bold'))
txtnumvenda.place(x = 160, y = 25, width = 100, height=20)

lblcodcli = tk.Label(tela_venda, text="Cod. Cliente:", font=('Calibri', 12, 'bold'), bg='lightskyblue', fg='black', anchor='w')
lblcodcli.place(x = 50, y = 60, width = 100, height=20)

txtcodcli = tk.Entry(tela_venda)
txtcodcli.place(x = 160, y = 60, width = 100, height=20)
txtcodcli.bind('<Return>', bus_cli)

btnbuscli = tk.Button(tela_venda, text ="Buscar cliente", 
                      bg ='gold',foreground='black', font=('Calibri', 12, 'bold'), command=abrir_popup_busca_cliente)
btnbuscli.place(x = 280, y = 50, width = 120, height=30)

lblnomecli = tk.Label(tela_venda, text ="Nome Cliente:", font=('Calibri', 12, 'bold'), bg = 'lightskyblue', fg = 'black', anchor = 'w')
lblnomecli.place(x = 50, y = 100, width = 100, height=20)

txtnomecli =  tk.Entry(tela_venda)
txtnomecli.place(x = 160, y = 100, width = 560, height=20)
txtnomecli.config(state= "disabled")

lblcodprod = tk.Label(tela_venda, text = "Cód. Prod:", font=('Calibri', 10, 'bold'), bg = 'lightskyblue', fg = 'black', anchor = 'w')
lblcodprod.place(x = 50, y = 160, width = 100, height=20)

btnbuscli = tk.Button(tela_venda, text ="Buscar cliente", 
                      bg ='gold',foreground='black', font=('Calibri', 12, 'bold'), command=abrir_popup_busca_prodserv)
btnbuscli.place(x = 280, y = 160, width = 120, height=30)

txtcodprod =  tk.Entry(tela_venda)
txtcodprod.place(x = 160, y = 160, width = 100, height=20)
txtcodprod.bind('<Return>', bus_prod)

lbldescricao = tk.Label(tela_venda, text = "Descrição:", font=('Calibri', 10, 'bold'), bg = 'lightskyblue', fg = 'black', anchor = 'w')
lbldescricao.place(x = 50, y = 200, width = 100, height=20)

txtdescricao =  tk.Entry(tela_venda)
txtdescricao.place(x = 160, y = 200, width = 560, height=20)

lblqtde = tk.Label(tela_venda, text = "Quantidade:", font=('Calibri', 10, 'bold'), bg = 'lightskyblue', fg = 'black', anchor = 'w')
lblqtde.place(x = 50, y = 240, width = 100, height=20)


txtqtde =  tk.Entry(tela_venda)
txtqtde.place(x = 160, y = 240, width = 100, height=20)
txtqtde.bind('<FocusOut>', entrar_qtde)
txtqtde.bind('<Return>', entrar_qtde)

btnincluir = tk.Button(tela_venda, text ="Incluir - F1", 
                      bg ='gold',foreground='black', font=('Calibri', 12, 'bold'), command = gravar_lin)
btnincluir.place(x = 160, y = 290, width = 100, height=30)
tela_venda.bind('<F1>', finalizar_linha)
btnincluir.bind('<Button-1>', finalizar_linha)
btnincluir.bind('<Return>', finalizar_linha)

lblvlrunit = tk.Label(tela_venda, text = "Valor Unit:", font=('Calibri', 10, 'bold'), bg = 'lightskyblue', fg = 'black', anchor = 'w')
lblvlrunit.place(x = 280, y = 240, width = 100, height=20)
lblvlrunit.config(state= "disabled")

txtvlrunit =  tk.Entry(tela_venda)
txtvlrunit.place(x = 390, y = 240, width = 100, height=20)

lblvalor = tk.Label(tela_venda, text = "Valor:", font=('Calibri', 10, 'bold'), bg = 'lightskyblue', fg = 'black', anchor = 'w')
lblvalor.place(x = 510, y = 240, width = 100, height=20)

txtvalor =  tk.Entry(tela_venda)
txtvalor.place(x = 620, y = 240, width = 100, height=20)
txtvalor.config(state= "disabled")

lbltotal = tk.Label(tela_venda, text = "Total ->", font=('Calibri', 16, 'bold'), bg = 'lightskyblue', fg = "black", anchor = 'c')
lbltotal.place(x = 548, y = 520, width = 100, height=40)

txt_total =  tk.Entry(tela_venda, justify='center', bg="silver", fg="blue",  font=('Calibri', 16, 'bold'))
txt_total.place(x = 650, y = 520, width = 150, height=40)
txt_total.config(state= "readonly")

btnlimpar = tk.Button(tela_venda, text ="Limpar - F2", 
                      bg ='gold',foreground='black', font=('Calibri', 12, 'bold'), command=limpar)
btnlimpar.place(x = 390, y = 290, width = 100, height=30)
btnlimpar.bind('<Button-1>', limpar)
tela_venda.bind('<F2>', limpar)

btnexcluir = tk.Button(tela_venda, text ="Excluir", 
                      bg ='gold',foreground='black', font=('Calibri', 12, 'bold'), command = excluir)
btnexcluir.place(x = 620, y = 290, width = 100, height=30)


btngravar = tk.Button(tela_venda, text ="Gravar", 
                      bg ='black',foreground='white', font=('Calibri', 12, 'bold'), command = gravar)
btngravar.place(x = 160, y = 600, width = 100, height=50)

btnimprimir = tk.Button(tela_venda, text ="Imprimir", 
                       bg ='green',foreground='white', font=('Calibri', 12, 'bold'), command = imprimir)
btnimprimir.place(x = 280, y = 600, width = 100, height=50)

btncancelar = tk.Button(tela_venda, text ="Cancelar", 
                       bg ='red',foreground='white', font=('Calibri', 12, 'bold'), command = cancelar)
btncancelar.place(x = 400, y = 600, width = 100, height=50)

btnmenu = tk.Button(tela_venda, text ="Menu", 
                       bg ='yellow',foreground='black', font=('Calibri', 12, 'bold'), command = menu)
btnmenu.place(x = 520, y = 600, width = 100, height=50)



style = ttk.Style()

style.configure("mystye.Treeview", font=("Calibri", 10))
style.configure("mystyle.Treeview.Heading", font=("Calibri", 12, "bold"))

tree = ttk.Treeview(tela_venda, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', style="mystyle.Treeview", padding=0)

tree.column("#1")
tree.heading("#1", text="Linha")
tree.column("#1", width = 50, anchor ='c')

tree.column("#2")
tree.heading("#2", text="Código")
tree.column("#2", width = 100, anchor ='c')

tree.column("#3")
tree.heading("#3", text="Descrição")
tree.column("#3", width = 200, anchor ='w')

tree.column("#4")
tree.heading("#4", text="Quantidade")
tree.column("#4", width = 150, anchor ='c')

tree.column("#5")
tree.heading("#5", text="Valor Unit")
tree.column("#5", width = 100, anchor ='c')

tree.column("#6")
tree.heading("#6", text="Valor")
tree.column("#6", width = 150, anchor ='c')

tree.place(x=50,y=350,height=180)

scrollbar = ttk.Scrollbar(tela_venda, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x = 801, y = 350,height=180)


numeracao()
excluir_inic()

visualizar()

total()


txtnumvenda.config(state= "disabled")


txtcodcli.focus_set()
  

tela_venda.mainloop()
