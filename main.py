def calcular(a, b, operacao):
    if operacao == "1":
        return a + b
    elif operacao == "2":
        return a - b
    elif operacao == "3":
        return a * b
    elif operacao == "4":
        return a / b
    else:
        return None


if __name__ == "__main__":
    print("Aplicação rodando com sucesso! 🚀")
