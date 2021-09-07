def Fatorial(num):
    fatorial = 1
    i = 2

    while i <= num:
        print("I",i)
        fatorial = fatorial * i
        print("Fat",fatorial)
        i = i + 1

    print(fatorial)
    return fatorial

def main():
    num = int(input("Digite um número para saber seu fatorial:"))
    Fatorial(num)

main()