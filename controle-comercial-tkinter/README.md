# Projeto de controle comercial

## Foi necessario realizar algumas alterações para sistemas Linux

### 1.0 -> Alterar chamada de rotas com C:
### 2.0 -> Alterar chamdas de telas zoomed

```bash
    if platform.system() == "Windows":
        tela_login.state('zoomed')
    else:
        tela_login.attributes('-zoomed', True)
```

