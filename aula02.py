# input
nome = input("Digite o seu nome: ")
print(nome.title())

# Loop for
nomes = ['Leticia', 'Marcos', 'Paulo']
for x in nomes:
    print(x)


# Listas -> Ordenada, mutável, indexada
lista = [5, 10, 15, 20, 30, 30, 30]
print(lista)

lista.append(25)
print(lista)

lista.insert(6, 30)
print(lista)

lista.remove(30)
for x in lista:
    if x == 30:
        lista.remove(x)
print(lista)

print(lista[0])

print(len(lista))

lista.pop() # Se colocar algum número como argumento, ele vai remover o valor naquele índice. Se não, ele remove o último elemento
print(lista)

lista.clear()
print(lista)
# Tuplas --> Valores são imutáveis -> é feito com parênteses
tupla = (5, 10)

print(tupla[0])
print(tupla[1])

#tupla[1] = 30 -> isso dá erro pois é imutável


# Dicionários
dicionario = {
    "1": "Primeiro",
    "2": "Segundo",
    "3": "Terceiro"
}

print(dicionario["1"])

dicionario["4"] = "Quarto" # como adicionar uma nova chave-valor

print(dicionario["4"])

del dicionario["1"] # como deletar uma chave valor
print(dicionario)
# Conjuntos(Set) -> Não ordenados, mutáveis e não permitem elementos duplicados
numeros = {1, 2, 3, 4, 5}

numeros.add(6)
print(numeros)

numeros.remove(3)
print(numeros)

numeros.add(2) # se tentar adicionar um número já existente não vai fazer nada
print(numeros)

# Operações com Conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B) # união de (valores presentes em A ou B)
print(A & B) # interseção (valores presentes em A e B)
print(A - B) # diferença (valores em A que não estão em B)
print(A ^ B) # diferença simétrica (valores que estão em A ou B, mas não em ambos)