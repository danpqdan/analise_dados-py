import os

global dir
global imagemPadrao
global imagemSecundaria
dir = os.path.dirname(os.path.abspath(__file__))
imagemPadrao = os.path.join(dir, 'fundo_menu.jpg')
imagemSecundaria = os.path.join(dir, 'fundo_submodulos.jpg')
