def main():
    nomes = []
    for i in range(0,5):
        nomes.append(input("Digite nome: "))

    for i in range(len(nomes)):
        print(nomes[i])

    '''nomes[nomes.index('André')] = input("Sobrenome: ")
    for i in range(len(nomes)):
        print(nomes[i])'''

    sobrenome = input("Digite seu sobrenome: ")
    for i in nomes:
        nomes[nomes.index(i)]  = i + " " + sobrenome

    print(nomes)

main()