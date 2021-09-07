print("------------------------------------- EXERCÍCIO H ----------------------------------------------")
def SalarioBruto(salario_hora,horas_traba):
    resultado = salario_hora * horas_traba
    salario_bruto = resultado

    def ImpostoRenda():
        resultado_IR = resultado * 0.11
        return resultado_IR
    imposto_renda = ImpostoRenda()

    def CalculoInss():
        resultado_inss = resultado * 0.08
        return resultado_inss
    inss = CalculoInss()

    def CalculoSindicato():
        resultado_sindicato = resultado * 0.05
        return resultado_sindicato
    sindicato = CalculoSindicato()

    def CalculoSalarioLiquido():
        salario_liquido = salario_bruto - inss - sindicato - imposto_renda
        return salario_liquido
    salario_liquido = CalculoSalarioLiquido()

    def CalculoDescontos():
        descontos = inss+imposto_renda+sindicato
        return descontos
    descontos = CalculoDescontos()

    print("Salário Bruto: R$",salario_bruto,"\nImposto de Renda: R$",imposto_renda,"\nINSS: R$",inss)
    print("Sindicato: R$",sindicato,"\nSalário Líquido: R$",salario_liquido,"\nDescontos: R$",descontos)

    return resultado,ImpostoRenda(),CalculoInss(),CalculoSindicato(),CalculoSalarioLiquido(),CalculoDescontos()

print("------------------------------------- EXERCÍCIO I ----------------------------------------------")
'''def PositivoNegativo(num):
    if num >= 0:
        print("Número Positivo")
    else:
        print("Número Negativo")
    return num '''

print("------------------------------------- EXERCÍCIO J ----------------------------------------------")
'''def Sexo(sexo):
    if sexo == 'M':
        print("Masculino")
    elif sexo == 'F':
        print("Feminino")
    else:
        print("Sexo Inválido")
    return sexo'''

print("------------------------------------- EXERCÍCIO K ----------------------------------------------")
'''def CalcularMedia(nota1,nota2):
    media = (nota1 + nota2) / 2
    if media == 10 :
        print("Aprovado com Distinção")
    elif media >= 7 :
        print("Aprovado")
    else:
        print("Reprovado")
    return media'''

print("------------------------------------- EXERCÍCIO O ----------------------------------------------")
def Tabuada(numero):
    for i in range(1,11):
        resultado_soma = numero + i
        resultado_sub = numero - i
        resultado_multi = numero * i
        resultado_divi = numero / i
        print(numero,"+",i,"=",resultado_soma,"     ",numero,"-",i,"=",resultado_sub,"     "
              ,numero,"*",i,"=",resultado_multi,"     ",numero,"/",i,"=",resultado_divi)
    return resultado_soma,resultado_sub,resultado_multi,resultado_divi


#MÉTODO PRINCIPAL
def main():
    salario_hora = float(input("Salário/Hora: "))
    horas_trabalhadas = int(input("Horas trabalhadas no mês: "))
    SalarioBruto(salario_hora,horas_trabalhadas)

    '''num = int(input("Digite um número: "))
    PositivoNegativo(num)'''

    '''sexo = input("Digite seu gênero, M para masculino e F para feminino: ")
    Sexo(sexo)'''

    '''nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    CalcularMedia(nota1,nota2)'''

    numero = int(input("Digite o número desejado para ver a tabuada: "))
    Tabuada(numero)

main()