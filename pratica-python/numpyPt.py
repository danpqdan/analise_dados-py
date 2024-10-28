import numpy as np

# Criando uma matriz unidimensional
ut = np.array([12, 32, 26, 18, 10])
print(ut)
print(type(ut))

# Criar um array com um tipo especiofico
# Cria um array do typo float 64
mtFloat = np.array([1, 2, 3], dtype=np.float64)
print(mtFloat)
print(type(mtFloat))
mtInt = np.array([1, 2, 3], dtype=np.int32)
print(mtInt)
print(type(mtInt))

# Transformar tipos de dados de um array
mtNew = np.array([1.4, 3.6, -5.3, 9.4, 2.22222222])
print(mtNew)
mtNewInt = mtNew.astype(np.int32)
print(mtNewInt)

# Matriz Bidimensional
mtMD = np.array([[7, 2, 13], [1, 5, 9], [5, 10, 13]])
print(mtMD)
print(mtMD.shape)  # Mostra tamanho das dimensões

semRep = np.unique(mtNew)  # Remove itens repetidos
print(semRep)
