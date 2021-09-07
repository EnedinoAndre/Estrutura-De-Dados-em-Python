def main():
    inicio = int(input("Inicio: "))
    fim = int(input("Fim: "))
    for i in range (inicio,fim+1):
        print(i ** 2)


    while (inicio <= fim):
        print(inicio * inicio)
        inicio += 1
main()