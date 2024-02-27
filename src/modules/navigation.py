from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def visible_route_button(driver):
    '''
    verifica se está à mostra o botão de rotas
    '''

    # padrão de busca
    xpath = '//button[@aria-label="Fechar rotas"]'

    # encontrando o elemento
    element = driver.find_elements(By.XPATH, xpath)

    # validando se o elemento foi encontrado
    view = len(element) > 0

    return view


def set_destination(locate, driver, box=1):
    '''
    insere um destino
    '''

    # validando se, não está à mostra a seção de rotas
    if not visible_route_button(driver):

        # componente da busca
        element = driver.find_element(By.ID, 'searchboxinput')

        # removendo dados que estão na busca
        element.clear()

        # preenchendo o destino
        element.send_keys(locate)

        # executando a busca
        element.send_keys(Keys.RETURN)

    # se encontrou as rotas
    else:

        # padrão de busca
        xpath = '//div[contains(@id, "directions-searchbox")]//input'

        # componente da busca
        elements = driver.find_elements(By.XPATH, xpath)

        # validando apenas os elementos que estão sendo mostrados
        elements = [element for element in elements if element.is_displayed()]

        # se existir dados
        if len(elements) >= box:

            # caixa de endereço
            element = elements[box - 1]

            # selecionando todo o conteúdo do input
            element.send_keys(Keys.CONTROL + 'a')

            # removendo dados que poderiam estar na busca
            element.send_keys(Keys.DELETE)

            # preenchendo o detino
            element.send_keys(locate)

            # executando a busca
            element.send_keys(Keys.RETURN)

        else:
            print(
                f'não foi possível adicionar o endereço: {
                    len(elements)
                } | {
                    box
                }'
            )


def click_routes_button(driver):
    '''
    abre a seção de rotas clicando no botão
    '''

    # padrão de busca
    xpath = '//button[@data-value="Rotas"]'

    # espera implícita para abertura do link
    wait = WebDriverWait(driver, timeout=7)

    # componente da busca
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    # clicando no botão
    element.click()

    # padrão de busca
    xpath = '//button[@aria-label="Fechar rotas"]'

    # espera implícita para abertura do link
    wait = WebDriverWait(driver, timeout=7)

    # componente da busca
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


def set_driving(driver, driving='carro'):
    '''
    seleciona o tipo de condução desejada
    '''

    # padrão de busca
    xpath = f'//img[@aria-label="{driving.capitalize()}"]'

    # espera implícita para abertura do link
    wait = WebDriverWait(driver, timeout=7)

    # componente da busca
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    # clicando
    element.click()


def add_route_box(driver):
    '''
    adiciona uma caixa de rotas
    '''

    # padrão da caixa de adicionar destino
    xpath = '//span[text()="Adicionar destino"]'

    # aguardando
    wait = WebDriverWait(driver, timeout=7)

    # esperando estar visível
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    # buscando o elemento
    botao_adiciona_destino = driver.find_element(By.XPATH, xpath)

    # clicando
    botao_adiciona_destino.click()


def plot_routes(locations, solution, driver):

    # setando o primeiro destino, para abrir as rotas
    set_destination(locations[0], driver, box=1)

    # pontos da rota
    points = [point[0] for point in solution]

    # para cada solução
    for i in range(len(points)):

        # adicionando os dados
        set_destination(
            locations[points[i]], driver, i + 1
        )

        # adicionando uma nova caixa de rota
        add_route_box(driver)

    # adicionando os dados
    set_destination(
        locations[points[0]], driver, len(locations) + 1
    )
