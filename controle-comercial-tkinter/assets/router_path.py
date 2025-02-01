import os
import sys

global dir
global imagemPadrao
global imagemSecundaria
global pathClientes
global pathCadLogin
global pathConexao
global pathLogin
global pathMenu
global pathProdutos
global pathVendas
dir = os.path.dirname(os.path.abspath(__file__))
if getattr(sys, 'frozen', False):
    imagemSecundaria = os.path.join(sys._MEIPASS, 'fundo_submodulos.jpg')
    imagemPadrao = os.path.join(sys._MEIPASS, 'fundo_menu.jpg')
    pathClientes = os.path.join(sys._MEIPASS, './func_pages/clientes.py')
    pathCadLogin = os.path.join(sys._MEIPASS, './func_pages/cadlogin.py')
    pathConexao = os.path.join(sys._MEIPASS, './func_pages/conexao.py')
    pathLogin = os.path.join(sys._MEIPASS, './func_pages/login.py')
    pathMenu = os.path.join(sys._MEIPASS, './func_pages/menu.py')
    pathProdutos = os.path.join(sys._MEIPASS, './func_pages/produtos.py')
    pathVendas = os.path.join(sys._MEIPASS, './func_pages/vendas.py')
else:
    pathClientes = os.path.join(dir, './func_pages/clientes.py')
    pathCadLogin = os.path.join(dir, './func_pages/cadlogin.py')
    pathConexao = os.path.join(dir, './func_pages/conexao.py')
    pathLogin = os.path.join(dir, './func_pages/login.py')
    pathMenu = os.path.join(dir, './func_pages/menu.py')
    pathProdutos = os.path.join(dir, './func_pages/produtos.py')
    pathVendas = os.path.join(dir, './func_pages/vendas.py')
    imagemPadrao = os.path.join(dir, 'fundo_menu.jpg')
    imagemSecundaria = os.path.join(dir, 'fundo_submodulos.jpg')
