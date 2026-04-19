def calcular(a, b, operacao):
    if operacao == "1":
        return a + b
    elif operacao == "2":
        return a - b
    elif operacao == "3":
        return a * b
    elif operacao == "4":
        if b == 0:
            return "Erro: divisão por zero"
        return a / b
    else:
        return None


def main():
    print("Calculadora Simples em Python")
    print("-------------------------------")

    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        print("\nEscolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        op = input("Opção: ")

        resultado = calcular(a, b, op)

        if resultado is None:
            print("Operação inválida")
        else:
            print(f"Resultado: {resultado}")

    except ValueError:
        print("Erro: digite apenas números válidos")

    print("\n✔ Sistema finalizado.")


if __name__ == "__main__":
    main()
