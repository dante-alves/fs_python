# Stacktrace de Erro em Python
    # O tipo do erro
    # Onde o erro ocorreu (linha do código)
    
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: Não pode dividir um número por zero") # como definir a mensagem que será enviada pelo erro
    return a / b

#resultado = dividir(10, 0)
#print(resultado)
# --> vai dar o erro ZeroDivisonError. Por isso utilizar o try-except

try:
    print(dividir(10, 0))
except ZeroDivisionError as e: # salvando a mensagem do erro em "e"
    print(e)


