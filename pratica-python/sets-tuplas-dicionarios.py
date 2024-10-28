# Dicionarios => Chave/Valor {JSon}
Notas = {"Joao": 6.0, "Maria": 8.0, "Pedro": 6.5}
print(Notas)
print(Notas["Joao"])
Notas.keys()
Notas.values()
print("Joao" in Notas)  # Validação logica
print("Fernando" in Notas)  # Validação logica
del Notas["Joao"]  # Excluir elemento
print(Notas)
Notas["Ana"] = 9  # Incluir elemento
print(Notas)
Notas.get("Geraldo", "Não encontrado! ")

# Sets conjuntos não ordenados de valores não repetidos

bigdata = {"cachorro", "gato", "leao"}
print(bigdata)
print("cachorro" in bigdata)
bigdata.add("camelo")  # adicionar elemento
bigdata
print(len(bigdata))
bigdata.add("cachorro")
print(bigdata)
bigdata

# Tuplas são listas ordenadas
# OBS:: listas usam [], tuplas usam ()
tuplas = (1, 2, 3, 4, 5, 6, 7)
tuplas
tuplas[4]

# Dicionario em que cada posição recebe uma tupla
dic2 = {(0, 1): 0, (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4, (5, 6): 5, (6, 7): 6}
dic2

print(type(Notas))
print(type(bigdata))
print(type(tuplas))
