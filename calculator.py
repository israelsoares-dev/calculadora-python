import math
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a<0:
        return'Erro; não existe raiz quadrada de numero negativo'
    return math.sqrt(a)

def salvar_historico(n1, op, n2, resultado):
    with open('historico.txt', 'a', encoding="utf-8") as arquivo:
        arquivo.write(f'{n1} {n2} {op} = {resultado}\n')


continuar = "sim"

while continuar == "sim":
    try:
        op = input("Escolha a operação (+, -, *, /, **, r): ")
        n1 = float(input("Digite o primeiro número: "))

        if op == "r":
            resultado = raiz_quadrada(n1)
        else:
            n2 = float(input("Digite o segundo número: "))

            if op == "+":
                resultado = somar(n1, n2)
            elif op == "-":
                resultado = subtrair(n1, n2)
            elif op == "*":
                resultado = multiplicar(n1, n2)
            elif op == "/":
                resultado = dividir(n1, n2)
            elif op == "**":
                resultado = potencia(n1, n2)
            else:
                resultado = "operação inválida"
    except ValueError:
        print("Erro: digite apenas números válidos.")
        continuar = input("Deseja continuar? (sim/não): ")
        continue

    except OverflowError:
        print("Erro: o resultado é grande demais para ser calculado.")
        continuar = input("Deseja continuar? (sim/não): ")
        continue

    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"Resultado: {resultado:.2f}")
        if op =="r":
            salvar_historico(n1,op, '-', resultado)
        else:
            salvar_historico(n1, op, n2, resultado)

    continuar = input("Deseja continuar? (sim/não): ")

print("Programa encerrado.")


