#Criar python -m venv venv --> ambiente onde vai adicionar as coisas
#Código para ativar o virtual enviroment --> .\venv\Scripts\activate
    #Se não funcionar, utilizar o código --> Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
varText = "Textinho"
varInt = 3

print("Algo na tela\n", varText, varInt)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2

print("Resultado da soma: ", soma)