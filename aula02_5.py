# Funções
def saudacao(nome):
    x = 0
    print(f"Olá, {nome}")


saudacao("Dante")
saudacao("Bob")


def imprimir_soma(n1, n2):
    print(soma(n1, n2))

def soma(n1, n2):
    return n1 + n2

imprimir_soma(5, 10)

# Programaçao Orientada a Objetos (POO)
# criar um objeto

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def apresentar(self):
        print(f"Olá! meu nome é {self.nome}, e tenho {self.idade} anos.")
    
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    
p1 = Pessoa("Dante", 21, 66, 1.67)

p1.apresentar

print(f"Meu IMC é de {p1.calcular_imc():.2f}")


class Carro:
    def __init__(self):
        self.porta_fechada = True
        self.dentro_do_carro = False
        self.pneu_furado = False
        self.gasolina = True
        self.km = 0
    
    def entrar_carro_motorista(self):
        self.porta_fechada = False
    
    def fechar_portas(self):
        self.porta_fechada = True
        
    def passar_pedregulho(self):
        self.pneu_furado = True

    def consertar_pneu(self):
        self.pneu_furado = False

    def encher_tanque(self):
        self.gasolina = True

    def dirigir(self, km):
        if not self.pneu_furado and (self.gasolina and self.porta_fechada and self.dentro_do_carro):
            self.km = km
            self.gasolina = False
            print(f"Andei {km}km!")
        else:
            print("Não é possível andar agora. Verifique o carro!")
    
    def verificar_carro(self):
        if self.pneu_furado == True:
            print("O pneu está furado!")

        if self.porta_fechada == False:
            print("Porta(s) abertas!")
        
        if self.gasolina == False:
            print("Carro sem gasolina!")

car = Carro()

opc = -1

while opc != 0:
    print("1 - Entrar no carro\n2 - Fechar a porta\n3 - Dirigir\n4 - ")