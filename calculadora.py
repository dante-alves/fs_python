sair = False

while not sair:
    num1 = int(input("Digite um valor: "))
    num2 = int(input("Digite outro valor: "))

    operacao = int(input("Qual operação deseja realizar?\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n 4 - Divisão"))
    match operacao:
        case 1:
            print(f"Resultado: {num1 + num2}")
        case 2:
            print(f"Resiltado: {num1 - num2}")
        case 3:
            print(f"Resultado: {num1 * num2}")
        case 4:
            print(f"Resultado: {num1 / num2}")
        case _:
            print("Operação Inválida.")
    
    sair = True if int(input("Digite 0 para sair: ")) == 0 else False