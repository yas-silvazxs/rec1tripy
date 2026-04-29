atividades = ["sair","jogar","estudar"]
palavra = "estudar"
encontrado =  False
for item in atividades:
    if item == palavra:
        encontrado = True
        break

if encontrado:
    print(f"a palavra {palavra}, existe na lista")    
else:
    print(f"a palavra {palavra}, nao existe na lista")    


