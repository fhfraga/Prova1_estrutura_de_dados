from bigO import big_O
from ordenacao_bubble_sort import ordenacao_bubble_sort

print(ordenacao_bubble_sort(1, 52, 3, 3))

print(big_O(ordenacao_bubble_sort, entrada_minima_funcao=1,
            entrada_maxima_funcao=100, minimo_loop=1, maximo_loop=1000))
