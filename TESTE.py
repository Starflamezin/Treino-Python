a = int(input("A quantidade de valores:"))
temp = []
for i in range(a):
    b = float(input("O valor:"))
    temp.append(b)
c = max(temp)
d = min(temp)
g = sum(temp)/len(temp)
f = print("Todos os valores colocados:",temp)
f = print("A media dos valores:",g)
f = print("O maior valor:",c)
f = print("O menor valor:",d)