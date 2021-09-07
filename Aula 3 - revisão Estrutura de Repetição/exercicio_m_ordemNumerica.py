def Ordem(num1,num2,num3):
    for i in [num1,num2,num3]:
        print("i",i)
        print("")
        for j in [num1,num2,num3]:
            print("j",j)
            print("")
            for l in [num1,num2,num3]:
                print("l",l)
                if i < j and j < l:
                    print(i,j,l)
                    print("")

    return num1,num2,num3
def main():
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite um numero: "))
    num3 = int(input("Digite um numero: "))
    Ordem(num1,num2,num3)

main()