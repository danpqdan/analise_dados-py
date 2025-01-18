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

## MERGE 5453b31d97fd1da96520ed9ef12e1ad8cfd583d0: 
### -> ADD: Funcionalidade de gerenciamento de cliente
### -> REF: Refatorado arvore visual para ClienteTreeview

## MERGE c89baf701e8ef294b60097ac8f121cf398d98de8
### -> ADD: Funcionalidades de gerenciamento de produtos
### -> REF: Refatorado arvore visual para ProdutoTreeview
