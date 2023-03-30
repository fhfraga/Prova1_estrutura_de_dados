import time

import plotly.express as px


def big_O(funcao, entrada_minima_funcao, entrada_maxima_funcao,
          minimo_loop, maximo_loop):
    """Função para plotagem do gráfico de Big'O
        Parameters
        ----------
        funcao: function
            Função que será avaliada
        entrada_minima_funcao: int
            Valor minimo do intervalo para a seleção de valores aleatórios na função
        entrada_maxima_funcao: int
            Valor máximo do intervalo para a seleção de valores aleatórios na função
        minimo_loop: int
            Valor mínimo do intervalo do loop
        maximo_loop: int
            Valor máximo do intervalo do loop
        Returns
        -------
        plot
            Gráfico da complexidade do algoritmo.
        """

    ns_1 = []
    tempos_1 = []

    for n in range(minimo_loop, maximo_loop):
        start = time.perf_counter_ns()
        result = funcao(entrada_minima_funcao, entrada_maxima_funcao, n, 1)
        end = time.perf_counter_ns()
        segundos = (end-start) * 10**-9
        ns_1.append(n)
        tempos_1.append(segundos)

    fig = px.line(x=ns_1, y=tempos_1,
                  labels={
                      "x": "Valor de n",
                      "y": "Tempo de execução (em segundos)"
                  },
                  title="Gráfico de complexidade Big'O")
    return fig.show()
