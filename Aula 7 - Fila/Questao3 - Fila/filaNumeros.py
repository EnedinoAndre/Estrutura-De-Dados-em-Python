class Fila():
    def __init__(self):
        self.numeros = []

    def adicionarNumeros(self, numero):
        self.numeros.append(numero)

    def retirarNumero(self):
        lista = []
        negativo = 0
        for i in range (len(self.numeros)):
            valor = self.numeros[i]

            if valor > 0:
                lista.append(valor)
            else:
                negativo += 1
        for i in range(len(self.numeros)):
            self.numeros.pop(0)

        for i in lista:
            self.numeros.append(i)

        return negativo

    def mostrarNumeros(self):
        return self.numeros


