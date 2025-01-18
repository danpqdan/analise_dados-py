# -*- coding: utf-8 -*-
import sys
import tkinter as tk
from tkinter import * 
from PIL import Image, ImageTk
import conexao 
from router_path import imagemSecundaria, pathMenu

if __name__ == '__main__': 
    tela_log = tk.Tk()
else:
    tela_log = tk.Toplevel()


larguraTela = tela_log.winfo_screenwidth()
alturaTela = tela_log.winfo_screenheight()
tela_log.geometry(f'{larguraTela}x{alturaTela}+0+0')

tela_log.title("Controle Comercial - Login")
tela_log['bg'] = "gold"

tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((tela_log.winfo_screenwidth(), tela_log.winfo_screenheight())))
tk.Label(tela_log, image=tkimage_cli).grid()

def validasenha():

    var_login = txtusuario.get()
    var_senha = txtsenha.get()

    try:
        con=conexao.conexao()
        if not con.db:
            raise ConnectionError("Não foi possível conectar ao banco de dados.")
        
        sql_txt=(f"select usuario, nome from login where usuario = '{var_login}'"
                 + f"and CAST(aes_decrypt(senha,'chave') as char) = '{var_senha}'")
                 
        rs=con.consultar(sql_txt)
       
        if rs:
           lblresult = tk.Label(container, text ="**** Acesso Permitido ***", foreground='blue')
           lblresult.grid(column=1, row=3)
           con.fechar()
           tela_log.destroy()
           exec(open(pathMenu).read(),locals())
          
        else:
           lblresult = tk.Label(container, text ="Usuario ou Senha Invalida", foreground='red')
           lblresult.grid(column=1, row=3)
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        if 'con' in locals() and con.db:
            con.fechar()

def mostrarsenha():
    if txtsenha.cget('show') == '':
        txtsenha.config(show='*')
        btnmostrar.config(text='Mostrar Senha')
    else:
        txtsenha.config(show='')
        btnmostrar.config(text='Enconder Senha')

'''
    Configurações de tela
'''
container = tk.Frame(tela_log)
container.place(bordermode='inside', relx=0.5, rely=0.5, anchor="center")
form = tk.Frame(container)
form.grid(row=1, column=1, padx=30, pady=10)
frame_botao = tk.Frame(container)
frame_botao.grid(row=2, column=1, pady=5) 

lblusuario = tk.Label(form, text ="Usuario:", bg="lightskyblue", font=('Calibri', 12, 'bold'))
lblusuario.grid(row=0, column=0, padx=5, pady=5)
txtusuario = tk.Entry(form, font=('Calibri', 12), width = 35)
txtusuario.grid(row=0, column=1, padx=5, pady=5)

lblsenha = tk.Label(form, text ="Senha:  ", bg="lightskyblue", font=('Calibri', 12, 'bold'))
lblsenha.grid(row=1, column=0)
txtsenha  = tk.Entry(form, font=('Calibri', 12), width = 35, show = "*")
txtsenha.grid(row=1, column=1)

btnsubmeter = tk.Button(frame_botao, text ="Login", 
                      bg ='black',foreground='white', font=('Calibri', 12, 'bold'), command=validasenha)
btnsubmeter.grid(row=2, column=0, pady=5, padx=10)


btnmostrar = tk.Button(frame_botao, text ="Mostar Senha", 
                      bg ='white',foreground='black', font=('Calibri', 12, 'bold'), command=mostrarsenha)
btnmostrar.grid(row=2, column=1, pady=5, padx=10)

txtusuario.focus_set()

tela_log.mainloop()
