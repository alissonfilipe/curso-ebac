def calcular_expressao(palavras):
    # Converte todos os números para float
    elementos = []
    for i in range(len(palavras)):
        if i % 2 == 0:  # Índices pares: números
            try:
                elementos.append(float(palavras[i]))
            except ValueError:
                print("Erro: número inválido.")
                return None
        else:  # Índices ímpares: operadores
            if palavras[i] not in ['+', '-', '*', '/']:
                print(f"Erro: operador inválido '{palavras[i]}'.")
                return None
            elementos.append(palavras[i])

    # Operações na ordem: *, /, +, -
    i = 1
    while i < len(elementos) - 1:
        op = elementos[i]
        if op in ['*', '/']:
            a = elementos[i - 1]
            b = elementos[i + 1]
            resultado = a * b if op == '*' else a / b
            elementos[i-1:i+2] = [resultado]
            i = 1  # volta ao início
        else:
            i += 2

    # Agora só resta + e -
    i = 1
    while i < len(elementos) - 1:
        op = elementos[i]
        a = elementos[i - 1]
        b = elementos[i + 1]
        resultado = a + b if op == '+' else a - b
        elementos[i-1:i+2] = [resultado]

    return elementos[0]

# -------------------------
print("<----------CALCULADORA PYTHON--------->")
texto = input("Digite a operação (ex: 3 + 5 * 2): ")
palavras = texto.split()

resultado = calcular_expressao(palavras)

if resultado is not None:
    print(f"Resultado: {resultado}")
