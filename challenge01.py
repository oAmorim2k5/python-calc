import os, json

def salvar_dados_json(dados, nome_arquivo): #Salvando operações em um arquivo JSON
    try:
        with open(nome_arquivo, 'w') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def ler_dados_json(nome_arquivo): #Lendo operações em um arquivo JSON
    try:
        with open(nome_arquivo, "r") as arquivo_json:
            dados = json.load(arquivo_json)
            print(f"Dados de operações:\n ${nome_arquivo}")
    except Exception as e:
        print(f"Erro ao ler os dados: ${e}")

def continua(result): #Printa resultado e continua após ação
    print(result)
    input("Pressione Enter para continuar...")

def calc(numUm, operador, numDois): #calculadora
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
        dados = {
            "primeiroNumero": numUm,
            "segundoNumero": numDois,
            "operador": operador,
            "resultado": result
        } 
        return dados
        
    except Exception as e:
        return f"Erro: {str(e)}"
    
if __name__ == "__main__": 
    while True: #MAIN
        os.system("cls")
        try:
            nome_arquivo = "challenges01.json" #Arquivo json

            print("Exemplo de entrada: num01 + num02")
            operacao = input("Operação: ").split(" ")

            numUm = float(operacao[0])
            operador = str(operacao[1])
            numDois = float(operacao[2])

            nova_operacao = calc(numUm, operador, numDois)
        
            continua(nova_operacao)

        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de digitar números e operadores corretamente.")
            input("Pressione Enter para continuar...")
        except IndexError:
            print("Erro: Formato de operação inválido. Use o formato 'numero operador numero'.")
            input("Pressione Enter para continuar...")
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            input("Pressione Enter para continuar...")            