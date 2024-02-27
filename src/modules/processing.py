import pulp
import itertools


def tsp(locations, distances):

    def distancia(end1, end2):
        return distances[f'{end1}_{end2}']

    prob = pulp.LpProblem('TSP', pulp.LpMinimize)

    x = pulp.LpVariable.dicts('x', [(i, j) for i in range(
        len(locations)) for j in range(len(locations)) if i != j], cat='Binary')

    prob += pulp.lpSum([distancia(i, j) * x[(i, j)] for i in range(len(locations))
                       for j in range(len(locations)) if i != j])

    # passar apenas uma vez
    for i in range(len(locations)):
        prob += pulp.lpSum([x[(i, j)]
                           for j in range(len(locations)) if i != j]) == 1
        prob += pulp.lpSum([x[(j, i)]
                           for j in range(len(locations)) if i != j]) == 1

    # evitar subturs
    for k in range(len(locations)):
        for s in range(2, len(locations)):
            for subset in itertools.combinations([i for i in range(len(locations)) if i != k], s):
                prob += pulp.lpSum([x[(i, j)]
                                   for i in subset for j in subset if i != j]) <= len(subset) - 1

    prob.solve(pulp.PULP_CBC_CMD())

    # for i in range(len(locations)):
    #     for j in range(len(locations)):
    #         if i != j:
    #             print(i, j, x[(i, j)].value())

    solucao = []
    cidade_inicial = 0
    proxima_cidade = cidade_inicial
    while True:
        for j in range(len(locations)):
            if j != proxima_cidade and x[(proxima_cidade, j)].value() == 1:
                solucao.append((proxima_cidade, j))
                proxima_cidade = j
                break
        if proxima_cidade == cidade_inicial:
            break

    print('Rota: ')
    for i in range(len(solucao)):
        print(solucao[i][0], ' ->> ', solucao[i][1])

    return solucao


def extract_info(data):
    '''
    extrai informações de um dicionário
    '''

    # extraindo a chave
    key = list(data.keys())[0]

    # extraindo a distância
    value = data.get(key).get('distance')

    # padronizando os dados
    value = float(
        value.replace(
            '.', ''
        ).replace(
            'km', ''
        ).strip().replace(
            ',', '.'
        )
    )

    # dados extraídos
    extracted_data = {
        key: value
    }

    return extracted_data
