def saida_formatada(container):
    return '{' + ', '.join(container) + '}'


def saida_cartesiano(lista_tuples):
    return ', '.join(map(str, lista_tuples))


def operadores(letra, conjuntos):

    if letra == 'U':
        container_uniao = list(set(item for sublista in conjuntos for item in sublista))
        print(f"União: conjunto 1 {saida_formatada(conjuntos[0])}, conjunto 2 {saida_formatada(conjuntos[1])}. Resultado: {saida_formatada(container_uniao)}")

    elif letra == 'I':
        inter = []
        for n in range(len(conjuntos[0])):
            if conjuntos[0][n] in inter:
                continue
            elif conjuntos[0][n] in conjuntos[1]:
                inter.append(conjuntos[0][n])

        print(f"Interseção: conjunto 1 {saida_formatada(conjuntos[0])}, conjunto 2 {saida_formatada(conjuntos[1])}. Resultado: {saida_formatada(inter)}")

    elif letra == 'D':
        difer = []
        for n in range(len(conjuntos[0])):
            if conjuntos[0][n] in difer:
                continue
            elif conjuntos[0][n] not in conjuntos[1]:
                difer.append(conjuntos[0][n])

        print(f"Diferença: conjunto 1 {saida_formatada(conjuntos[0])}, conjunto 2 {saida_formatada(conjuntos[1])}. Resultado: {saida_formatada(difer)}")

    elif letra == 'C':
        cartesiano = []
        controle_duplicatas = set()
        for cada in conjuntos[0]:
            for n in range(len(conjuntos[1])):
                tupla = (int(cada) if cada.isdigit() else cada, int(conjuntos[1][n]) if conjuntos[1][n].isdigit() else conjuntos[1][n])
                if tupla not in controle_duplicatas:  # Verifica se a tupla já foi vista
                    cartesiano.append(tupla)  # Adiciona à lista
                    controle_duplicatas.add(tupla)

        print(f"Cartesiano: conjunto 1  {saida_formatada(conjuntos[0])}, conjunto 2 {saida_formatada(conjuntos[1])}. Resultado: {'{' + saida_cartesiano(cartesiano) + '}'}")



with open("Exemplo_2.txt", "r") as file:
    while True:
        num_operacoes = int(file.readline().strip())
        for _ in range(num_operacoes):
            container = []  # gera um container container ambos conjuntos para cada operação
            operador = file.readline().strip()
            for _ in range(2):
                linha = file.readline().strip()
                numeros = [num for num in linha.split(', ')]
                container.append(numeros)
            operadores(operador, container)
        break
