"""
    Eventos excludentes:
        - Eventos que não podem ocorrer ao mesmo tempo.
        - Somatório de probabilidades: P(A ou B) = P(A) + P(B)
        
        Exemplo:
            Jogar um dado, qual a probabilidade de sair 1 ou par?
            P(A) = 1/6 + 3/6 = 4/6 = 0,6667 = 66,67%
            
    Eventos não excludentes:
        - Eventos que podem ocorrer ao mesmo tempo.
        - Somatório de probabilidades: P(A ou B) = P(A) + P(B) - P(A e B)
        
        Exemplo:
            Jogar um dado, qual a probabilidade de sair 2 ou par?
            P(A) = 1/6 + 3/6 - 1/6 = 3/6 = 0,5 = 50%
            
    Eventos independentes:
        - Mais de um evento, mas não dependem um do outro.
        - Multiplicação de probabilidades: P(A e B) = P(A) * P(B)
        
        Exemplo:
            Qual a probabilidade de jogar dois dados e dar 1 e 6?
            P(A) = 1/6 * 1/6 = 1/36 = 0,0278 = 2,78%
            
    Eventos dependentes:
        - Mais de um evento, mas dependem um do outro.
        - Multiplicação de probabilidades: P(A e B) = P(A) * P(B|A)
        
        Exemplo: 
            Com 6 cartas na mão(A, 2, 3, 4, 5, 6), qual a probabilidade de tirar um A e um 4?
            P(A) = 1/6 * 1/5 = 1/30 = 0,0333 = 3,33%
            
            
            
"""