# Explorando capitais brasileiras: roteiros turísticos com algoritmos genéticos em python

Este repositório destina-se a uma **prova de conceito (_poc_)** de _algoritmos genéticos_, focalizando a criação de possíveis itinerários turísticos nas capitais brasileiras.

## Contextualização

O desafio do [caixeiro viajante (tsp)](https://pt.wikipedia.org/wiki/Problema_do_caixeiro-viajante) é um dos problemas clássicos frequentemente abordados por algoritmos genéticos.

Se trata de uma [pessoa que busca vender seus produtos ao percorrer cidades](https://pt.wikipedia.org/wiki/Caixeiro-viajante), enfrentando algumas restrições notáveis:

1. Visitar todas as cidades e retornar à origem.

2. Evitar revisitar uma cidade já visitada.

3. Percorrer o caminho mais curto possível.

Este é reconhecido como um problema de **np-difícil/complexo**, com uma complexidade **de _n(!nC)_**. Ao adicionar novos caminhos, as possibilidades de rotas aumentam exponencialmente. Para abordar as `26` capitais e o Distrito Federal, junto com o ponto de origem teríamos `n(!28)`, totalizando  `304.888.344.611.713.860.501.504.000.000` (trezentos e quatro octilhões, oitocentos e oitenta e oito setilhões, trezentos e quarenta e quatro sextilhões, seiscentos e onze quintilhões, setecentos e treze quatrilhões, oitocentos e sessenta trilhões, quinhentos e um bilhões, quinhentos e quatro milhões) possibilidades. Algoritmos de estruturas de dados convencionais enfrentariam desafios ao analisar e calcular todas essas rotas em tempo hábil.

A aplicação de algoritmos genéticos nesse cenário permite resolver o problema de forma eficaz, encontrando uma solução válida em pouco tempo, sem recorrer à força bruta em todos os casos.

Este repositório servirá como base para a criação de uma **prova de conceito (poc)** de **algoritmos genéticos**, implementando gradualmente o **caixeiro viajante** em **python**.

A intenção é abordar conceitos teóricos, como _elitismo_, _seleção de pais_, _cruzamentos_, _mutações_ e suas respectivas taxas. Além disso, exploraremos características específicas do problema em questão.

Além da implementação, pretendo buscar maneiras de criar uma interface iterativa amigável para visualizar os dados usando o [google maps](https://www.google.com.br/maps/preview). A rota gerada pelo algoritmo genético será representada através de pontos que simbolizam as cidades e linhas que denotam as rotas. Isso não apenas enriquecerá a experiência visual, mas também proporcionará uma compreensão mais profunda da teoria estudada.

## Licença

<div align='center'>
    <b>
        Licença baseada em MIT
    </b>
    <br/><br/>
    Direitos Autorais (c) 2024 
    <i>
        <a href=https://www.linkedin.com/in/murilochaves/>Murilo Chaves Jayme</a>
    </i>
</div>

<div align='justify'>
    <br/>
    A permissão é concedida por meio deste, gratuitamente, a qualquer pessoa que obtenha uma cópia deste software e dos arquivos de documentação associados (o "Software"), para lidar com o Software sem restrições, incluindo, sem limitação, os direitos de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, e permitir que as pessoas a quem o Software é fornecido o façam, sujeitas às seguintes condições:
    <br/><br/>
    O aviso de direitos autorais acima e este aviso de permissão devem ser incluídos em todas as cópias ou partes substanciais do Software.
    <br/><br/>
    O software é fornecido "como está", sem garantia de qualquer tipo, expressa ou implícita, incluindo, mas não se limitando a garantias de comercialização, adequação a uma finalidade específica e não violação. Em nenhum caso os autores ou detentores de direitos autorais serão responsáveis por qualquer reclamação, danos ou outra responsabilidade, quer em uma ação contratual, delitual ou de outra forma, decorrente de, ou em conexão com, o software ou o uso ou outras operações no software.
</div>
