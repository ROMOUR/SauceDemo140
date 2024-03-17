#biblioteca
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#classe
class Teste_produtos():

#atributo
    url = "https://www.saucedemo.com"


#funções e Métodos
    def setup_method(self,method):               # metodo de inialização de testes
        self.driver = webdriver.Chrome()         # instanciar o objeto do selenium webdrive como chrome
        self.driver.implicitly_wait(5)           # define o tempo de espera por elementos em 5 seundos

    def teardown_method(self,method):            # método de finalização dos teste
        self.driver.quit()                       # encerra/

    def test_selecionar_produto(self):           # método de teste
        self.driver.get(self.url)                # abre navegador 
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.NAME,"password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()   # clique no botão de login

        # transição de página

        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"  # confirma se está escrito Products no elemento
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack" # confirma se é a mochila
        # confirma o preço da mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == (
            "$29.99" 
        )