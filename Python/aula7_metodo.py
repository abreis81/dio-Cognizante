## metodo não deveria retornar valor, no python não se segue muito isso
## função retorna valor
## classe é para englobar

# metodos
#    def soma(a, b):
#        return a + b

#    def subtracao(a, b):
#        return a - b

#    def multiplicacao(a, b):
#        return a * b

#    def divisao(a, b):
#        return a / b

#print (soma(1,2))
#print (subtracao(7,3))
#print (multiplicacao(5,3))
#print (divisao(7,3))


## classe

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


# instanciar a calculadora
calculadora = Calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.divisao())
print(calculadora.soma())