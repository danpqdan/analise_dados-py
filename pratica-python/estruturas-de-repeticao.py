#while =>

count = 1
while count <= 5:
    print(count)
    count+=1
        
#for incremental =>
for item in range(0, 5, 1):
    print(item)
    
for item in range(0, 5):
    print(item + 1)
    
#for decremental =>
for item in range(10, 0, -1):
    print(item)

#Exemplo de break
for item in range(0,10):
    if item == 4:
        break
    print(item)
    
#Exemplo de continue
#Nesse exemplo pulamos o item do continue
for item in range(0,10):
    if item == 4:
        print("Continuaremos... ")
        continue
    print(item)