"""
    Pequeas amostras:
        - Probabilidade a "longo prazo" é diferente de probabilidade a "curto prazo".
        
        Exemplo:    
            jogando um dado 6 vezes, qual a média esperada?
            - 1, 2, 3, 4, 5, 6 = 3,5
            
        Codigo com pequenos numeros:
            x = sample(range(1, 7), 6)
            mean(x)

            1 = 3.8 , 2 = 3.1, 3 = 2.8, 4 = 2.1
            
        Codigo com grandes numeros:
            x = sample(range(1, 7), 1000000, replace = T)
            mean(x)
            
            [4] = ~3.5
            
            
        Conclusão:
            - A média de um dado é 3,5, mas jogando poucas vezes o resultado pode ser diferente.
            - Quanto mais vezes jogar, mais próximo de 3,5 será a média.
            - A probabilidade a "longo prazo" é diferente de probabilidade a "curto prazo".
            

"""