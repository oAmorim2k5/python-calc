import os

def continua(result): #Printa resultado e continua após ação
    print(result)
    input("Pressione Enter para continuar...")

def calc(numUm, operador, numDois):
    result = 0
    try:
        if operador == "+": #Somar
            return numUm + numDois
        elif operador == "-": #Subtrair
            return numUm - numDois
        elif operador == "*": #Multiplicar
            return numUm * numDois
        elif operador == "/": #Dividir
            if numDois != 0:
                return numUm / numDois
            else:
                return "Operador invalido, divisão por 0"
        elif operador == "**": #Exponenciação
            return numUm ** numDois
    except Exception as e:
        return f"Erro: {str(e)}"
    
while True: #MAIN
    os.system("cls")
    try:
        print("Exemplo de entrada: num01 + num02")
        operacao = input("Operação: ").split(" ")

        numUm = float(operacao[0])
        operador = str(operacao[1])
        numDois = float(operacao[2])

        result = calc(numUm, operador, numDois)
        continua(result)

    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de digitar números e operadores corretamente.")
        input("Pressione Enter para continuar...")
    except IndexError:
        print("Erro: Formato de operação inválido. Use o formato 'numero operador numero'.")
        input("Pressione Enter para continuar...")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
        input("Pressione Enter para continuar...")

