import random

import numpy as np


def ordenacao_bubble_sort(minimo, maximo, linha_matriz, coluna_matriz):
    """Função para aplicação de ordenação bubble sort
        Parameters
        ----------
        minimo: int
            Valor mínimo do intervalo para a seleção de valores aleatórios
        maximo: int
            Valor máximo do intervalo para a seleção de valores aleatórios
        linha_matriz: int
            Quantidade de linhas na matriz
        coluna_matriz: int
            Quantidade de colunas na matriz
        Returns
        -------
        list
            lista ordenada do menor para o maior com as posições inicias dos
            elementos.
        """
    random.seed(42)
    lista = []
    matriz = np.random.randint(minimo, maximo, (linha_matriz, coluna_matriz))
    print(f'A matriz de entrada é:\n{matriz}\n')
    print('--------------------------------------------------------------------')
    for linha in range(len(matriz)):
        for coluna, valor in enumerate(matriz[linha]):
            lista.append(matriz[linha][coluna])
            print(
                f'O número {valor} estava na posição: linha {linha} e coluna {coluna}')
    print('--------------------------------------------------------------------')
    for lista_invertida in range(len(lista) - 1, 0, -1):
        for posicao in range(lista_invertida):
            if lista[posicao] > lista[posicao + 1]:
                valor_maior = lista[posicao]
                lista[posicao] = lista[posicao + 1]
                lista[posicao + 1] = valor_maior
    return print(f'Lista final {lista}:')
