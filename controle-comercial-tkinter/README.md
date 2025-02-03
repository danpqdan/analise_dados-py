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

## MERGE fd468f46a3d1935c8d3118567eca5224c78df7b3
### -> ADD: Bind para facilitar o login.
### -> ALT: Background do formulario de login.

## MERGE 49bf05a92b027adbd3b13a666699ac2cb3f53d2f
### -> ADD: Funcionalidade de busca e alteração de vendas.
### -> ADD: Arvore de busca de vendas.
### -> ALT: Corrigido alinhamento dos botões na interface.
### -> FIX: Corrigido logica de auto incremento e update de vendas ja existentes.
### -> REF: Refatorado estrutura do projeto em modulos.

