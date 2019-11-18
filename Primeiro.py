n = int(input("N dos convidados: \n"))#digita e recebe o numero de conviados
lista_numero = []#lista que serao alocados os convidados
i = 1 #contador 
while i <= n: #estrutura de repeticao 
    nome_convidados = input("Digite o nome do convidado:")# nome dos conviados
    lista_numero.append(nome_convidados)#adiciona a lista "lista_numero" os nomes digitados acima
    i += 1 #soma o contador
for a in lista_numero:
    print(a) #printa o nome dos conviados