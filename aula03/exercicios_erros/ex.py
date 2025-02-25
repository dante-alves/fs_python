# ex01
print("Olá mundo!")
# O erro foi SyntaxError pois faltou um " no final do print

# ex02
nome = "Dante"
print(nome)
# NameError -> Variável não definida

# ex03
def somar(a, b):
    return a + b

try:
    print(somar(10, 5))
except TypeError:
    print("Erro: tentativa de somar tipos incompatíveis.")

# ex04
numeros = [10, 20, 30]

try:
    indice = int(input("Digite um índice para acessar a lista: "))
    print(numeros[indice])
except IndexError:
    print("Índice não existente!")
except ValueError:
    print("Valor inválido! Digite um número.")

# ex05
def dividir(a, b):
    return a / b

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    resultado = dividir(num1, num2)
    print("Resultado:", round(resultado, 2))
except ValueError:
    print("Valor inserido inválido.")
except ZeroDivisionError:
    print("Não pode dividir um número por 0")


# ex 06
dados = {
    "nome": "Dante",
    "idade": "21",
    "cidade": "João Pessoa"
}

try:
    chave = input("Digite a chave que deseja acessar: ")

    print(f"O valor da chave '{chave}' é: {dados[chave]}")
    dados.get(chave, "Chave não encontrada")
except KeyError:
    print("Chave não existente.")

# ex07
def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

f = 0
while f != 1:
    try:
        idade = int(input("Digite sua idade: "))
        print(validar_idade(idade))
        f = 1
    except ValueError:
        print("Valor inválido!")