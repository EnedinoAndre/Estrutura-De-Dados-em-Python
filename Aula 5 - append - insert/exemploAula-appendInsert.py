def main():

    estados = ['PB','PE','MA','SP']
    print(estados)

    #ADICIONANDO NO ULTIMO ITEM
    estados.append('RJ')
    print(estados)

    #ADICIONANDO 'ESTADO' NA POSIÇÃO 12
    estados.insert(12,'PR')
    print(estados)

    #SOBESCREVER ITEM POR OUTRO ITEM DE ACORDO COM O INDICE
    estados[estados.index('PE')] = 'SC'
    print(estados)

main()