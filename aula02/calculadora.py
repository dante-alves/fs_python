""">>> Desafio: Criar uma Calculadora com Classes  

Você deve criar uma classe chamada Calculadora que permita realizar operações matemáticas básicas, como adição, subtração, multiplicação e divisão. A calculadora também deve ser capaz de armazenar o histórico das operações realizadas. 
Requisitos:  

Classe Calculadora:  
Deve ter um atributo chamado historico, que será uma lista para armazenar as operações realizadas.
Deve ter os seguintes métodos:
- adicionar(a, b): Retorna a soma de a e b e registra a operação no histórico.
- subtrair(a, b): Retorna a diferença entre a e b e registra a operação no histórico.
- multiplicar(a, b): Retorna o produto de a e b e registra a operação no histórico.
- dividir(a, b): Retorna a divisão de a por b e registra a operação no histórico. Caso b seja zero, deve lançar uma exceção informando que a divisão por zero não é permitida.
- mostrar_historico(): Exibe todas as operações realizadas na calculadora, incluindo os números envolvidos e o resultado.

Exemplo de Funcionalidade:  

O usuário deve poder instanciar a classe Calculadora e usar seus métodos para realizar operações.
Após realizar algumas operações, o usuário pode chamar o método mostrar_historico() para ver o histórico completo.

Bônus (opcional):  
Adicione um método chamado limpar_historico() que limpa o histórico de operações.
<<<"""

class Calculadora:

    def __init__(self): 
        self.historico = ['Histórico']
    
    # adição
    def adicionar(self, *numeros):
        total = 0
        expressao = ""

        # adicionar os números um por um ao total(resultado da operação) e na expressão que será salva no histórico
        for numero in numeros:
            expressao += (str(numero)) # adicionando à expressão do histórico
            total += numero # somando os valores
            if numero != numeros[-1]:
                expressao += " + " # enquanto não for o último número da expressão, adiciona o operador + à expressão

        expressao += f" = {total}"
        self.historico.append(expressao) # envia a expressão para o histórico

        print(f"\n{expressao}\n")

        return total # retorna o resultado da conta
    
    # subtração
    def subtrair(self, *numeros):
        total = numeros[0] # adicionar o primeiro número ao total, para só então começar a subtração
        expressao = f"{numeros[0]} - " # adicionar o primeiro número com o - à expressão

        for numero in numeros[1:]: # percorrer do segundo elemento até o último
            expressao += (str(numero))
            total -= numero
            if numero != numeros[-1]:
                expressao += " - "

        expressao += f" = {total}"
        self.historico.append(expressao)

        print(f"\n{expressao}\n")

        return total
    
    # multiplicação
    def multiplicar(self, *numeros):
        total = 1
        expressao = ""

        # multiplicar os números um por um ao total(resultado da operação) e na expressão que será salva no histórico
        for numero in numeros:
            expressao += (str(numero)) 
            total *= numero 
            if numero != numeros[-1]:
                expressao += " x " 

        expressao += f" = {total}"
        self.historico.append(expressao) 

        print(f"\n{expressao}\n")

        return total 
    
    # divisão
    def dividir(self, *numeros):
        # utilizando o try para não deixar o bagui dividir por 0
        try:
            total = numeros[0] # adicionar o primeiro número ao total, para só então começar a divisão
            expressao = f"{numeros[0]} / " # adicionar o primeiro número com o / à expressão

            for numero in numeros[1:]: # percorrer do segundo elemento até o último
                expressao += (str(numero))
                total /= numero
                if numero != numeros[-1]:
                    expressao += " / "

            expressao += f" = {total:.2f}"
            self.historico.append(expressao)

            print(f"\n{expressao}\n")

            return total
        except ZeroDivisionError:
            print("\nErro! Você tentou dividir um número por 0.\n")

    # mostrar o histórico
    def mostrar_historico(self):
        print("\n")
        for operacao in self.historico:
            print(operacao)

    # limpar o histórico
    def limpar_historico(self):
        self.historico.clear()
        self.historico = ['Histórico']


C = Calculadora()

opcao = -1

# loop principal
while opcao != 0:
    opcao = int(input("\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Mostrar histórico\n6 - Limpar histórico\n0 - Sair\n\nInsira uma opção: "))
    valores = []
    if  0 < opcao < 5:
        valores.append(int(input(f"Digite o {len(valores) + 1}º valor: ")))
        valores.append(int(input(f"Digite o {len(valores) + 1}º valor: ")))

    
        while True:
            entrada = (input(f"Digite o {len(valores) + 1}º valor, ou pressione ENTER para realizar a operação: "))
            if entrada == "":
                
                break
            
            try:
                valores.append(int(entrada))
            except ValueError:
                print("Entrada inválida. Digite um valor ou pressione ENTER para continuar.")
    
    match opcao:
        case 1:
            resultado = C.adicionar(*valores) # adicionei esse resultado só para simular o uso do retorno do resultado da função, já que na própria função eu coloquei para printar a expressão completa
        case 2:
            resultado = C.subtrair(*valores)
        case 3:
            resultado = C.multiplicar(*valores)
        case 4:
            resultado = C.dividir(*valores)
        case 5:
            C.mostrar_historico()
        case 6:
            C.limpar_historico()
            print("\nHistórico limpo!\n")
        case 0:
            print("\nAté a próxima!\n")
        case _:
            print("\nOpção inválida!\n")



