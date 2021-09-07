def MenorPreco(produ1,produ2,produ3):
    if produ1 < produ2 and produ1 < produ3:
        print("Menor preço: ",produ1)
    elif produ2 < produ1 and produ2 < produ3:
        print("Menor preço: ",produ2)
    else:
        print("Menor preço: ",produ3)
    return produ1,produ2,produ3
def main():
    produto1 = float(input("Produto 1: "))
    produto2 = float(input("Produto 2: "))
    produto3 = float(input("Produto 3: "))
    MenorPreco(produto1,produto2,produto3)

main()