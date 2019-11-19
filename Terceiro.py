def maior_num(colecao):                       
    maior = colecao[0]
    for n in colecao:
       if n>maior:
           maior = n
    return maior
print(maior_num([1, -9, 234, 23333.56, 23333]))

def menor_num(colecao):
    menor = colecao[0]
    for n in colecao:
        if n<menor:
            menor = n
    return menor

print(menor_num([1, -9, 234, 23333.56, 23333]))