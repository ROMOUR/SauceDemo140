#biblioteca
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#classe
class Teste_produtos():

#atributo
    url = "https://www.giulianaflores.com.br/"


#funções e Métodos
    def setup_method(self,method):               # metodo de inialização de testes
        self.driver = webdriver.Chrome()         # instanciar o objeto do selenium webdrive como chrome
        self.driver.implicitly_wait(10)           # define o tempo de espera por elementos em 5 seundos

    def teardown_method(self,method):            # método de finalização dos teste
        self.driver.quit()                       # encerra/

    def test_selecionar_produto(self):           # método de teste
        self.driver.get(self.url)     
        self.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
        self.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".content_checkout").click()
        self.driver.find_element(By.ID, "ContentSite_txtEmail").click()
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("9021930129")
        self.driver.find_element(By.ID, "ContentSite_txtPassword").click()
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("             ")
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
  