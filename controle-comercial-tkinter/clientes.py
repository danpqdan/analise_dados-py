# -*- coding: utf-8 -*-
import platform
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import conexao  
from router_path import dir, imagemPadrao, imagemSecundaria
from ClienteTreeview import ClienteTreeview

def novo():
    con=conexao.conexao()
    sql_txt = f"select IFNULL(max(codigo)+1,1) as codigo from clientes"
    rs=con.consultar(sql_txt)

    if rs:
        txtcodigo.insert(0, rs[0])

    con.fechar()
    txtnome.focus_set()

def limpar():
    txtcodigo.delete(0,"end")
    txtnome.delete(0,"end")
    txttelefone.delete(0,"end")
    txtemail.delete(0,"end")
    txtobservacao.delete("1.0","end")
    novo()

def buscar():
    var_codigo = txtcodigo.get()
    txtcodigo.delete(0,"end")
 
    con=conexao.conexao()
    sql_txt = f"select codigo,nome,telefone,email,observacao from clientes where codigo = {var_codigo}"
    rs=con.consultar(sql_txt)

    if rs:
    
        txtcodigo.insert(0, rs[0])
        txtnome.insert(0, rs[1])
        txttelefone.insert(0,rs[2])
        txtemail.insert(0,rs[3])
        txtobservacao.insert("1.0",(rs[4]))
    
    else:
        messagebox.showwarning("Aviso", "Código não Encontrado",parent = tela_cli)
        limpar()
        txtcodigo.focus_set()

    con.fechar()

def gravar():
    var_codigo = txtcodigo.get()
    var_nome = txtnome.get()
    var_telefone = txttelefone.get()
    var_email = txtemail.get()
    var_observacao = txtobservacao.get("1.0","end")


    con=conexao.conexao()
    sql_txt = f"select codigo,nome,telefone,email,observacao from clientes where codigo = {var_codigo}"

    rs=con.consultar(sql_txt)

    if rs:
        sql_text = f"update clientes set nome='{var_nome}',telefone='{var_telefone}',email='{var_email}',observacao='{var_observacao}' where codigo = '{var_codigo}'"
    else:
        sql_text = f"insert into clientes(codigo,nome,telefone,email,observacao) values ({var_codigo},'{var_nome}','{var_telefone}','{var_email}','{var_observacao}')"

    print(sql_text)
    if con.gravar(sql_text):
        messagebox.showinfo("Aviso", "Item Gravado com Sucesso", parent = tela_cli)
        limpar()
    else:
        messagebox.showerror("Erro", "Houve um Erro na Gravação", parent = tela_cli)

    con.fechar()

def excluir():
    var_del = messagebox.askyesno("Exclusão", "Tem certeza que deseja excluir?", parent = tela_cli)
    if var_del == True:
        var_codigo = txtcodigo.get()

        con=conexao.conexao()
        sql_text = f"delete from clientes where codigo = '{var_codigo}'"
        if con.gravar(sql_text):
              messagebox.showinfo("Aviso", "Item Excluido com Sucesso",parent = tela_cli)
              limpar()
        else:
            messagebox.showerror("Erro", "Houve um Erro na Exclusão",parent = tela_cli)

            
        con.fechar()

        limpar()
    else:
        limpar()




def menu():
    tela_cli.destroy()

print(__name__)
if __name__ == '__main__': 
    tela_cli = tk.Tk()
else:
    tela_cli = tk.Toplevel()
    
tela_cli.geometry('1920x1080+0+0')
if platform.system() == "Windows":
    tela_cli.state('zoomed')
else:
    tela_cli.attributes('-zoomed', True)
tela_cli.title("Controle Comercial 1.0 - Cadastro de Clientes")
tela_cli['bg'] = "gold"


tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((tela_cli.winfo_screenwidth(), tela_cli.winfo_screenheight())))
tk.Label(tela_cli, image=tkimage_cli).pack()


lblcodigo = tk.Label(tela_cli, text ="Codigo:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor = "w")
lblcodigo.place(x = 50, y = 60, width=85, height = 25)

txtcodigo = tk.Entry(tela_cli, width = 35, font=('Calibri', 12))
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)

buscabtn = tk.Button(tela_cli, text ="Pesquisar", 
                      bg ='white',foreground='black', font=('Calibri', 12, 'bold'), command = buscar)
buscabtn.place(x = 280, y = 60, width = 90, height = 25)

lblnome = tk.Label(tela_cli, text ="Nome:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor = "w")
lblnome.place(x = 50, y = 100, width=85, height = 25)

txtnome = tk.Entry(tela_cli, width = 35, font=('Calibri', 12))
txtnome.place(x = 150, y = 100, width = 360, height = 25)

lbltelefone = tk.Label(tela_cli, text ="Telefone:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor = "w")
lbltelefone.place(x = 50, y = 140, width=85, height = 25)

txttelefone = tk.Entry(tela_cli, width = 35, font=('Calibri', 12))
txttelefone.place(x = 150, y = 140, width = 360, height = 25)

lblemail = tk.Label(tela_cli, text ="E-mail:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor = "w")
lblemail.place(x = 50, y = 180, width=85, height = 25)

txtemail = tk.Entry(tela_cli, width = 35, font=('Calibri', 12))
txtemail.place(x = 150, y = 180, width = 360, height = 25)

lblobservacao = tk.Label(tela_cli, text ="Observacao:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor = "w")
lblobservacao.place(x = 50, y = 220, width=85, height = 25)

txtobservacao= tk.Text(tela_cli, font=('Calibri', 12))
txtobservacao.place(x=150, y=220, width=360, height=80)

btngravar = tk.Button(tela_cli, text ="Gravar", 
                       bg ='black',foreground='white', font=('Calibri', 12, 'bold'), command = gravar)
btngravar.place(x = 150, y = 320, width = 65)

btnexcluir = tk.Button(tela_cli, text ="Excluir", 
                       bg ='red',foreground='white', font=('Calibri', 12, 'bold'), command = excluir)
btnexcluir.place(x = 250, y = 320, width = 65)

btnlimpar = tk.Button(tela_cli, text ="Limpar", 
                       bg ='green',foreground='white', font=('Calibri', 12, 'bold'), command = limpar)
btnlimpar.place(x = 350, y = 320, width = 65)

btnmenu = tk.Button(tela_cli, text ="Menu", 
                       bg ='yellow',foreground='black', font=('Calibri', 12, 'bold'), command = menu)
btnmenu.place(x = 450, y = 320, width = 65)

text_fields = [txtcodigo, txtnome, txttelefone, txtemail, txtobservacao]
tree = ClienteTreeview(tela_cli)
tree.tree.bind("<Double-1>", lambda event: atualizar_filds(text_fields, tree.duplo_click(event, tkview=None)))
valores = tree.duplo_click() 
print(valores)

def atualizar_filds(fields, valores):
    if len(valores) == len(fields):
        for field, valor in zip(fields, valores):
            if isinstance(field, tk.Entry):
                field.delete(0, tk.END)
                field.insert(0, valor)
            elif isinstance(field, tk.Text):
                field.delete("1.0", tk.END)
                field.insert("1.0", valor)
            
novo()

tela_cli.mainloop()
