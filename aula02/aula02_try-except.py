try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado:.2f}")
except ZeroDivisionError:
    print("Erro! Você tentou dividir um número por 0.")
except ValueError:
    print("Erro! Você digitou um valor inválido.")