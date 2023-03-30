# Universidade de Vassouras


[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2022/03/campus_marica.png)](https://universidadedevassouras.edu.br/campus-marica/)
# Conheca o Curso de Engenharia de Software 
[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2021/12/Simbolo_Engenharia_de_Software.jpg)](https://universidadedevassouras.edu.br/graduacao-marica/engenharia-de-software/)

## Equipe
Composta pelos alunos do 3º Periodo, turma B, que são:

* Fernando Fraga
* Jeanderson Amaral
* Larissa Rocha 
* Tainá Narcizo
* Davi Narcizo

# Disciplina e Professor
Estrutura de dados, matéria ministrada pelo professor Marcio Garrido

## Problema

Tendo em vista o conjunto de elementos abaixo, criar um algoritmo que seja capaz de determinar a posição de cada elemento e printar as de forma ascendente os valores, assim como printar separadamente posições atuais. No final imprimir de forma gráfica a notação **Big'O** do seu resultado.

**Entrada**
* Elementos = [[0, 1, 2, 3], [11, 12, 13, 4], [10, 15, 14, 5], [9,8,7,6],];

**Saída**
* [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

* [0:0, 0:1, 0:2, 0:3, 1:3, 2:3, 3:3, 3:2, 3:1, 3:0, 2:0, 1:0, 1:1, 1:2, 2:2, 2:1]

## Bubble Sort

Bubble sort é um algoritmo de ordenação que realiza múltiplas passagens por uma lista, comparando os elementos com os itens posteriores e troca aqueles que tem os itens fora da ordem selecionada (crescente ou decrescente)

![](imagens/bubblepass.png)

## Explicação do código
Abaixo temos alguns pontos principais do código e sua explicação:

### Passo 1
```python
def ordenacao_bubble_sort(minimo, maximo, linha_matriz, coluna_matriz):
    random.seed(42)
    lista = []
    matriz = np.random.randint(minimo, maximo, (linha_matriz, coluna_matriz))
 ```
 Na parte descrita pelo código acima, temos a criação da matriz, onde a mesma
 é criada de forma automática e aleatório. a função `np.random.randint` ([link](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html) para documentação) cria valores aleatórios em um intervalo pre defino, além de devolver no formato desejado, no nosso caso uma matriz. Isso facilita na obtenção de valores aleatórios, podendo fazer vários testes sem ter que criar uma nova matriz na mão em cada um. Além disso, passamos a semente de aleatoriedade (`np.seed`) de forma a que outras pessoas possam testar e obter os mesmos resultados com o experimento.

 ### Passo 2

 ```python
  for linha in range(len(matriz)):
        for coluna, valor in enumerate(matriz[linha]):
            lista.append(matriz[linha][coluna])
 ```
Nesse passo temos a transformação de uma estrutura de dados em outra. Nos saimos da estrutura de matriz para a estrutura de lista. Isso facilita na hora de ordenar os elementos, que faremos no passo 3.

### Passo 3
```python
  for lista_invertida in range(len(lista) - 1, 0, -1):
        for posicao in range(lista_invertida):
            if lista[posicao] > lista[posicao + 1]:
                valor_maior = lista[posicao]
                lista[posicao] = lista[posicao + 1]
                lista[posicao + 1] = valor_maior
```
Nesse passo é onde acontece a ordenação. Indo por partes, na parte 1:

```python
  for lista_invertida in range(len(lista) - 1, 0, -1):
      for posicao in range(lista_invertida):
            
```
faz com que a contagem da lista seja ao contrário, começando de trás pra frente. Isso se deve ao fato do primeiro valor da lista ser o elemento que fará mais comparações, logo ele precisa do maior número de loops, para comparar com cada elemento. Então o valor que entra no segundo loop, será a quantidade de verificações que será feita para o elemento daquela. No caso de uma lista com 9 elementos, o primeiro elemento terá que fazer oito comparações,  a principio, pois ele será comparado com todos para saber se ele é ou não menor que outro. Porém se o elemento não for maior que algum, ele já pula para o próximo até acabar aquele loop interno, indo depois para o externo.

```python
    if lista[posicao] > lista[posicao + 1]:
        valor_maior = lista[posicao]
        lista[posicao] = lista[posicao + 1]
        lista[posicao + 1] = valor_maior
```
Nesse pedaço é que são feitas as comparações entre os elementos, onde basicamente se o elemento anterior for maior que o posterior, eles trocaração de posição na lista.

O código desse projeto pode ser encontrado no [Google Colab](https://colab.research.google.com/drive/1SidKiOq_ipiUzDfxzpsxS6xAXKvSpuPE#scrollTo=FDWejZvGigss) para facilitar sua utilização.