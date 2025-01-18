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

tela_log.geometry('450x300+483+250')
tela_log.title("Controle Comercial - Login")
tela_log['bg'] = "gold"

tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((tela_log.winfo_screenwidth(), tela_log.winfo_screenheight())))
tk.Label(tela_log, image=tkimage_cli).pack()

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
           lblresult = tk.Label(tela_log, text ="**** Acesso Permitido ***", foreground='blue')
           lblresult.place(x = 125, y = 110)
           con.fechar()
           tela_log.destroy()
           exec(open(pathMenu).read(),locals())
          
        else:
           lblresult = tk.Label(tela_log, text ="Usuario ou Senha Invalida", foreground='red')
           lblresult.place(x = 125, y = 130)              
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

lblusuario = tk.Label(tela_log, text ="Usuario:", bg="lightskyblue", font=('Calibri', 12, 'bold'))
lblusuario.place(x = 50, y = 50, width = 80, height=25)
txtusuario = tk.Entry(tela_log, font=('Calibri', 12), width = 35)
txtusuario.place(x = 150, y = 50, width = 100, height=25)

lblsenha = tk.Label(tela_log, text ="Senha:  ", bg="lightskyblue", font=('Calibri', 12, 'bold'))
lblsenha.place(x = 50, y = 100, width = 80, height=25)
 
txtsenha  = tk.Entry(tela_log, font=('Calibri', 12), width = 35, show = "*")
txtsenha.place(x = 150, y = 100, width = 100, height=25)

btnsubmeter = tk.Button(tela_log, text ="Login", 
                      bg ='black',foreground='white', font=('Calibri', 12, 'bold'), command=validasenha)
btnsubmeter.place(x = 170, y = 150, width = 55, height=25)

btnmostrar = tk.Button(tela_log, text ="Mostar Senha", 
                      bg ='white',foreground='black', font=('Calibri', 12, 'bold'), command=mostrarsenha)
btnmostrar.place(x = 270, y = 100, width = 120, height=25)

txtusuario.focus_set()

tela_log.mainloop()
