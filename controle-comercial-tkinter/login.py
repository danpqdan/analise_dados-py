import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import bcrypt
from conexao import Conexao
from menu import TelaMenu
from router_path import imagemSecundaria

class TelaLogin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        larguraTela = self.master.winfo_screenwidth()
        alturaTela = self.master.winfo_screenheight()
        self.master.geometry(f'{larguraTela}x{alturaTela}+0+0')

        self.tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((larguraTela, alturaTela)))
        tk.Label(self, image=self.tkimage_cli).grid(row=0, column=0)

        self.form = tk.Frame(self)
        self.form.grid(row=0, column=0, padx=30, pady=10)

        frame_botao = tk.Frame(self.form)
        frame_botao.grid(row=2, column=1, pady=5)

        lblusuario = tk.Label(self.form, text="Usuario:", bg="lightskyblue", font=('Calibri', 12, 'bold'))
        lblusuario.grid(row=0, column=0, padx=5, pady=5)
        self.txtusuario = tk.Entry(self.form, font=('Calibri', 12), width=35)
        self.txtusuario.grid(row=0, column=1, padx=5, pady=5)

        lblsenha = tk.Label(self.form, text="Senha:", bg="lightskyblue", font=('Calibri', 12, 'bold'))
        lblsenha.grid(row=1, column=0, padx=5, pady=5)
        self.txtsenha = tk.Entry(self.form, font=('Calibri', 12), width=35, show="*")
        self.txtsenha.grid(row=1, column=1, padx=5, pady=5)

        # Action buttons
        btnmostrar = tk.Button(self.form, text="Mostrar Senha", bg='white', fg='black', font=('Calibri', 12, 'bold'), command=self.mostrarsenha)
        btnmostrar.grid(row=1, column=2, pady=5, padx=10)

        btnsubmeter = tk.Button(frame_botao, text="Login", bg='black', fg='white', font=('Calibri', 12, 'bold'), command=self.validasenha)
        btnsubmeter.grid(row=0, column=0, pady=5, padx=10)
        
        btnsubmeter = tk.Button(frame_botao, text="Sair", bg='black', fg='white', font=('Calibri', 12, 'bold'), command=self.sair)
        btnsubmeter.grid(row=0, column=1, pady=5, padx=10)


        self.txtusuario.focus_set()

    def validasenha(self):
        """Validate login credentials and switch to menu on success."""
        var_login = self.txtusuario.get()
        var_senha = self.txtsenha.get()
        try:
            con = Conexao()
            if not con.db:
                raise ConnectionError("Não foi possível conectar ao banco de dados.")
            
            sql_txt = f"SELECT usuario, nome, senha FROM login WHERE usuario = '{var_login}'"
            rs = con.consultar(sql_txt)

            if rs:
                db_usuario, db_nome, db_senha_hash = rs
                if isinstance(db_senha_hash, bytes) and bcrypt.checkpw(var_senha.encode('utf-8'), db_senha_hash):
                    lblresult = tk.Label(self.form, text="**** Acesso Permitido ***", foreground='blue')
                    lblresult.grid(column=1, row=3)
                    con.fechar()

                    self.master.switch_to_menu()
                else:
                    lblresult = tk.Label(self.form, text="Usuário ou Senha Inválida", foreground='red')
                    lblresult.grid(column=1, row=3)
            else:
                lblresult = tk.Label(self.form, text="Usuário ou Senha Inválida", foreground='red')
                lblresult.grid(column=1, row=3)
        except Exception as e:
            print(f"Erro: {e}")

    def mostrarsenha(self):
        """Toggle password visibility."""
        if self.txtsenha.cget('show') == '':
            self.txtsenha.config(show='*')
        else:
            self.txtsenha.config(show='')

    def sair(self):
        self.master.destroy()
