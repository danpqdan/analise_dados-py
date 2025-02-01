import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from assets.router_path import imagemSecundaria


def create_widgets_cadlogin(self):
        
    larguraTela = self.master.winfo_screenwidth()
    alturaTela = self.master.winfo_screenheight()
    self.master.geometry(f'{larguraTela}x{alturaTela}+0+0')

    self.tkimage_cli = ImageTk.PhotoImage(Image.open(imagemSecundaria).resize((larguraTela, alturaTela)))
    tk.Label(self, image=self.tkimage_cli).grid(row=0, column=0)

    lblUsuario = tk.Label(self, text ="Usuario:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = "w")
    lblUsuario.place(x = 50, y = 60, width=80,height=25)
    entry = tk.Entry(self, width = 100)
    self.txtUsuario = tk.Entry(self, width = 35, font=('Calibri', 12))
    self.txtUsuario.place(x = 150, y = 60, width = 100, height=25)

    lblNome = tk.Label(self, text ="Nome:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = "w")
    lblNome.place(x = 50, y = 100, width=80, height=25)
    self.txtNome = tk.Entry(self, font=('Calibri', 12))
    self.txtNome.place(x = 150, y = 100, width = 360, height=25)

    lblSenha = tk.Label(self, text ="Senha:", bg="lightskyblue", fg="black", font=('Calibri', 12), anchor = "w")
    lblSenha.place(x = 50, y = 140, width=80, height=25)
    self.txtsenha = tk.Entry(self, show = "*" , width = 35, font=('Calibri', 12))
    self.txtsenha.place(x = 150, y = 140, width = 100, height=25)

    submitbtn = tk.Button(self, text ="Gravar", 
                            bg ='black',foreground='white', font=('Calibri', 12, 'bold'), command = self.gravar)
    submitbtn.place(x = 150, y = 190, width = 65)

    submitbtn = tk.Button(self, text ="Excluir", 
                            bg ='red',foreground='white', font=('Calibri', 12, 'bold'), command = self.excluir)
    submitbtn.place(x = 230, y = 190, width = 65)

    submitbtn = tk.Button(self, text ="Limpar", 
                            bg ='green',foreground='white', font=('Calibri', 12, 'bold'), command = self.limpar)
    submitbtn.place(x = 310, y = 190, width = 65)

    submitbtn = tk.Button(self, text ="Menu", 
                            bg ='yellow',foreground='black', font=('Calibri', 12, 'bold'), command = self.master.switch_to_menu)
    submitbtn.place(x = 390, y = 190, width = 65)

    buscabtn = tk.Button(self, text ="Pesquisar", 
                            bg ='white',foreground='black', font=('Calibri', 12, 'bold'), command = self.buscar)
    buscabtn.place(x = 280, y = 60, width = 90, height=25)

    style = ttk.Style()

    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=("Calibri", 10))
    style.configure("mystyle.Treeview.Heading", font=("Calibri", 12, "bold"))


    self.tree = ttk.Treeview(self, column=("c1", "c2", "c3", "c4"), show='headings', style="mystyle.Treeview", padding=0)

    self.tree.columnconfigure(0, weight=1)
    self.tree.rowconfigure(0, weight=1)

    self.tree.column("#1")
    self.tree.heading("#1", text="Código")
    self.tree.column("#1", width = 100, anchor ='c')

    self.tree.column("#2")
    self.tree.heading("#2", text="Usuario")
    self.tree.column("#2", width = 130, anchor ='c')

    self.tree.column("#3")
    self.tree.heading("#3", text="Nome")
    self.tree.column("#3", width = 250, anchor ='c')

    self.tree.column("#4")
    self.tree.heading("#4", text="Criado Em")
    self.tree.column("#4", width = 200, anchor ='c')


    self.tree.place(x=50, y=260, height=200)

    scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
    self.tree.configure(yscroll=scrollbar.set)
    scrollbar.place(x = 731, y = 260 , height=200)

    self.visualizar()
    self.txtUsuario.focus_set()