def primeiro_cal(n1,n2):
    resultado = (n1 * 2) + (n2/2)
    return resultado

def segundo_cal(n1,n3):
    resultado = (n1*3)+(n3)
    return resultado

def terceiro_cal(n3):
    resultado = n3 ** 3
    return resultado


def main():
    num1 = int(input("Digite o numero: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = float(input("Digite um número real: "))

    print(primeiro_cal(num1,num2))
    print(segundo_cal(num1,num3))
    print(terceiro_cal(num3))
main()