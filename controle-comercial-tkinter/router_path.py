import os

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
pathClientes = os.path.join(dir, 'clientes.py')
pathCadLogin = os.path.join(dir, 'cad_login.py')
pathConexao = os.path.join(dir, 'conexao.py')
pathLogin = os.path.join(dir, 'login.py')
pathMenu = os.path.join(dir, 'menu.py')
pathProdutos = os.path.join(dir, 'produtos.py')
pathVendas = os.path.join(dir, 'vendas.py')

imagemPadrao = os.path.join(dir, 'fundo_menu.jpg')
imagemSecundaria = os.path.join(dir, 'fundo_submodulos.jpg')
