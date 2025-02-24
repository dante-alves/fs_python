# estrutura with
# "r" read, "w" write, "a" append
nome_arquivo = "arquivo.txt"

# para ler uma linha
with open(nome_arquivo, "r") as arquivo: # as arquivo para armazenar o conteúdo lido na variável arquivo
    texto = arquivo.read()

print(texto)

# para ler várias linhas
with open(nome_arquivo, "r", encoding="utf8") as arquivo: # encoding="utf8" pra ler caracteres especiais
    mensagem = arquivo.readlines() # readlines armazena cada linha num índice de uma lista

print(mensagem)
print(mensagem[0]) # chamar a primeira linha
print(mensagem[1])

# procurar dados dentro de uma linha
for linha in mensagem:
    
    if "pular" in linha:
        print(linha)

# criar/substituir os dados de um arquivo
nome_arquivo2 = "senha"

with open(nome_arquivo2, "w") as arquivo:
    arquivo.write("789921")

# adicionar novas informações sem substituir o arquivo --> utilizar o "a"
with open(nome_arquivo2, "a") as arquivo:
    arquivo.write("\n40028922")
    