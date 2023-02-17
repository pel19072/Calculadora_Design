from datetime import datetime

class calculadora:
    def __init__(self):
        self.resultado = 0
        self.valores = [1]
        self.historial = ""
    
    def __str__(self):
        string = '''
        Calculadora realizada por Daniela Morales y Ricardo Pellecer

        Historial\n'''
        string += self.historial
        return string
    
    def ingreso(self, operacion):
        self.historial += str(datetime.now()) + "\t -- "+operacion+"\n"
    
    def mostrar_resultado(self, operacion):
        return str(self.resultado) + " = " + operacion

    def multiplicar(self, valores):
        self.resultado = 1
        self.ingreso("Multiplicacion")
        for valor in valores:
            self.resultado *=valor
        return self.resultado #self.mostrar_resultado("Multiplicacion de "+str(valores))

    def sumar(self, valores):
        self.ingreso("Suma")
        self.resultado = 0
        for valor in valores:
            self.resultado += valor
        return self.resultado

    def restar(self, valores):
        self.ingreso("Resta")
        self.resultado = 0
        for valor in valores:
            self.resultado -= valor
        return self.resultado

    def dividir(self, valores):
        self.ingreso("Division")
        self.resultado = valores[0]**2
        for valor in valores:
            self.resultado /= valor
        return self.resultado
