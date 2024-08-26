def process_operations(file_name):
    with open(file_name, 'r') as file:                            # Função para abrir os arquivos para executar
        numero_de_operacoes = int(file.readline().strip())        # lê a primeira linha do código para realizar a quantidade necessária de operações

        for _ in range(numero_de_operacoes):
            operacao = file.readline().strip()                    # Vê qual operação será realizada
            conjunto1 = set(file.readline().strip().split(', '))
            conjunto2 = set(file.readline().strip().split(', '))

            if operacao == 'U':
                resultado = conjunto1.union(conjunto2)
                nome_da_operacao = "União"

            elif operacao == 'I':
                resultado = conjunto1.intersection(conjunto2)
                nome_da_operacao = "Interseção"

            elif operacao == 'D':
                resultado = conjunto1.difference(conjunto2)
                nome_da_operacao = "Diferença"

            elif operacao == 'C':
                resultado = {(x, y) for x in conjunto1 for y in conjunto2}
                nome_da_operacao = "Produto Cartesiano"

            print("{}: conjunto 1 {}, conjunto 2 {}. Resultado = {} ".format(nome_da_operacao, conjunto1, conjunto2, resultado))

if __name__ == "__main__":
    process_operations('ex01.txt')                                 # Escolha o arquivo que vc quer executar

