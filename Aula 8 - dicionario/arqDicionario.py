def main():
    #Criando dicionario
    dicionario = {}
    #Inserir dados no dicionário
    dicionario = {1234: ["André",'Rua D', 'P2']}
    dicionario[6564]=["Bruno", "Rua A","P1"]
    dicionario[1111]=["ricardo", "Rua B", "P2"]
    dicionario[36543] = ["André","Rua T","P3"]
    print(dicionario.items())


    '''
    #Varrer Valores do Dicionário
    for valor in dicionario.values():
        print(valor)
    '''

    '''
    #Varrer Chaves do dicionário
    for chave in dicionario.keys():
        print(chave)
    '''


    #Busca por valor = nome
    for valor in dicionario.values():
        if "André" in valor[0]:
            print(valor)


    '''
    #BUSCAR CHAVE PELO NOME
    valorBusca = input("Qual aluno deseja lista: ")
    #ITEM 0 SEMPRE SERÁ O NÚMERO DA CHAVE
    for item in dicionario.items():
        if valorBusca in item[1][0]:
            print(item[0])
    '''

    '''
    #REMOVER ITEM DO DICIONARIO PELA SUA CHAVE
    dicionario.pop(1234)
    print(dicionario)
    '''
    
    '''
    #REMOVE CONTEÚDO DA POSIÇÃO ESPECÍFICA DENTRO DO VALOR USANDO O .ITEMS
    for item in dicionario.items():
        item[1].pop(0)

    print(dicionario.values())
    '''

main()