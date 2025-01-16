# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import conexao
import platform
from router_path import dir, imagemPadrao, imagemSecundaria

print(__name__)
if __name__ == '__main__': 
    tela_login = tk.Tk()
else:
    tela_login = tk.Toplevel()

def menu():
    tela_login.destroy()

def limpar():
    txtUsuario.delete(0,"end")
    txtNome.delete(0,"end")
    txtsenha.delete(0,"end")
    txtUsuario.focus_set()

def buscar():
    var_usuario = txtUsuario.get()
 
    con=conexao.conexao()
    sql_txt = f"select usuario,nome,CAST(aes_decrypt(senha,'chave') as char) as senha from login where usuario = '{var_usuario}'"
    rs=con.consultar(sql_txt)
    if rs:
        limpar()
        txtUsuario.insert(0, rs[0])
        txtNome.insert(0,rs[1])
        txtsenha.insert(0,rs[2])
    else:
        messagebox.showwarning("Aviso", "Usuario não Encontrado")
        limpar()
        txtUsuario.focus_set()

    con.fechar()

def duplo_click(event):
    limpar()
    item = tree.item(tree.selection())
    txtUsuario.insert(0, item['values'][1])
    buscar()

def visualizar():
    con=conexao.conexao()
    sql_txt = "select Codigo_int,usuario,nome,criado_em  from login order by nome"
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

def gravar():

    var_usuario = txtUsuario.get()
    var_nome = txtNome.get()
    var_senha = txtsenha.get()
 
    con=conexao.conexao()
    
    sql_txt = f"select usuario,nome,senha from login where usuario = '{var_usuario}'"

    rs=con.consultar(sql_txt)

    if rs:
        sql_text = f"update login set usuario='{var_usuario}',nome='{var_nome}',senha = aes_encrypt('{var_senha}','chave') where usuario = '{var_usuario}'"
    else:
        sql_text = f"insert into login(usuario,nome,senha) values ('{var_usuario}','{var_nome}',aes_encrypt('{var_senha}','chave'))"

    if con.gravar(sql_text):
        messagebox.showinfo("Aviso", "Item Gravado com Sucesso")
        limpar()
    else:
        messagebox.showerror("Erro", "Houve um Erro na Gravação")

    con.fechar()
    
    visualizar()

def excluir():
    var_del = messagebox.askyesno("Exclusívo", "Tem certeza que deseja excluir?")
    if var_del == True:
        var_usuario = txtUsuario.get()

        con=conexao.conexao()
        sql_text = f"delete from login where usuario = '{var_usuario}'"
        if con.gravar(sql_text):
              messagebox.showinfo("Aviso", "Item Excluídos com Sucesso")
              limpar()
        else:
            messagebox.showerror("Erro", "Houve um Erro na Exclusão")
            
        con.fechar()

        visualizar()
    else:
        limpar()

tela_login.geometry('1366x768+0+0')
if platform.system() == "Windows":
    tela_login.state('zoomed')
else:
    tela_login.attributes('-zoomed', True)
tela_login['bg'] = "gold"
tela_login.title("Controle Comercial - Gestão de Acessos")

tkimage_cli = ImageTk.PhotoImage(Image.open(imagemPadrao).resize((tela_login.winfo_screenwidth(), tela_login.winfo_screenheight())))
tk.Label(tela_login, image=tkimage_cli).pack()

lblUsuario = tk.Label(tela_login, text ="Usuario:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = "w")
lblUsuario.place(x = 50, y = 60, width=80,height=25)
entry = tk.Entry(tela_login, width = 100)
txtUsuario = tk.Entry(tela_login, width = 35, font=('Calibri', 12))
txtUsuario.place(x = 150, y = 60, width = 100, height=25)

lblNome = tk.Label(tela_login, text ="Nome:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = "w")
lblNome.place(x = 50, y = 100, width=80, height=25)
txtNome = tk.Entry(tela_login, font=('Calibri', 12))
txtNome.place(x = 150, y = 100, width = 360, height=25)

lblSenha = tk.Label(tela_login, text ="Senha:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = "w")
lblSenha.place(x = 50, y = 140, width=80, height=25)
txtsenha = tk.Entry(tela_login, show = "*" , width = 35, font=('Calibri', 12))
txtsenha.place(x = 150, y = 140, width = 100, height=25)

submitbtn = tk.Button(tela_login, text ="Gravar", 
                      bg ='black',foreground='white', font=('Calibri', 12, 'bold'), command = gravar)
submitbtn.place(x = 150, y = 190, width = 65)

submitbtn = tk.Button(tela_login, text ="Excluir", 
                      bg ='red',foreground='white', font=('Calibri', 12, 'bold'), command = excluir)
submitbtn.place(x = 230, y = 190, width = 65)

submitbtn = tk.Button(tela_login, text ="Limpar", 
                      bg ='green',foreground='white', font=('Calibri', 12, 'bold'), command = limpar)
submitbtn.place(x = 310, y = 190, width = 65)

submitbtn = tk.Button(tela_login, text ="Menu", 
                      bg ='yellow',foreground='black', font=('Calibri', 12, 'bold'), command = menu)
submitbtn.place(x = 390, y = 190, width = 65)

buscabtn = tk.Button(tela_login, text ="Pesquisar", 
                      bg ='white',foreground='black', font=('Calibri', 12, 'bold'), command = buscar)
buscabtn.place(x = 280, y = 60, width = 90, height=25)

style = ttk.Style()

style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=("Calibri", 10))
style.configure("mystyle.Treeview.Heading", font=("Calibri", 12, "bold"))


tree = ttk.Treeview(tela_login, column=("c1", "c2", "c3", "c4"), show='headings', style="mystyle.Treeview", padding=0)

tree.columnconfigure(0, weight=1)
tree.rowconfigure(0, weight=1)

tree.column("#1")
tree.heading("#1", text="Código")
tree.column("#1", width = 100, anchor ='c')

tree.column("#2")
tree.heading("#2", text="Usuario")
tree.column("#2", width = 130, anchor ='c')

tree.column("#3")
tree.heading("#3", text="Nome")
tree.column("#3", width = 250, anchor ='c')

tree.column("#4")
tree.heading("#4", text="Criado Em")
tree.column("#4", width = 200, anchor ='c')


tree.place(x=50, y=260, height=200)

scrollbar = ttk.Scrollbar(tela_login, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x = 731, y = 260 , height=200)

visualizar()
txtUsuario.focus_set()

tela_login.mainloop()
