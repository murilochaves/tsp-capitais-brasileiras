from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def create_driver(url):
    '''
    realiza a criação do driver de acesso
    '''

    # instanciando serviço
    service = Service(ChromeDriverManager().install())

    # criando o driver
    driver = webdriver.Chrome(service=service)

    # espera implícita para abertura do link
    driver.implicitly_wait(7)

    # realizando a abertura do navegador
    driver.get(url)

    return driver


def get_time(driver):
    '''
    coleta o tempo de deslocamento da rota
    '''

    # evitando erros de código
    try:

        # padrão de busca
        xpath = '//div[@id="section-directions-trip-0"]//div[contains(text(), "h")]'

        # espera implícita para abertura do link
        wait = WebDriverWait(driver, timeout=7)

        # componente da busca
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    except:
        
        # padrão de busca
        xpath = '//div[@id="section-directions-trip-0"]//div[contains(text(), "min")]'

        # espera implícita para abertura do link
        wait = WebDriverWait(driver, timeout=7)

        # componente da busca
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    # return float(element.text.replace(' h', ''))

    return element.text


def get_distance(driver):

    # padrão de busca
    xpath = '//div[@id="section-directions-trip-0"]//div[contains(text(), "km")]'

    # espera implícita para abertura do link
    wait = WebDriverWait(driver, timeout=7)

    # componente da busca
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    # return float(element.text.replace(' km', '').replace('.', '').replace(',', '.'))

    return element.text


if __name__ == '__main__':
    '''
    centralizando testes das funcionalidades deste código
    '''

    # testando
    driver = create_driver(
        url='https://www.google.com/maps'
    )
    print(driver)
