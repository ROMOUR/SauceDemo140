import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
        self.driver.find_element(By.CLASS_NAME, "carousel-brands .owl-item:nth-child(1) img").click ()
        self.driver.find_element(By.CSS_SELECTOR, "img[src*='27120gg.jpg']").click()
        self.driver.find_element(By.ID, "ContentSite_txtZip").click()
        self.driver.find_element(By.ID, "ContentSite_txtZip").send_keys ("18694")
        self.driver.find_element(By.ID, "ContentSite_txtZipComplement").click()
        self.driver.find_element(By.ID, "ContentSite_txtZipComplement").send_keys ("076")
        self.driver.find_element(By.CSS_SELECTOR, ".jOpenShippingPopup").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "btConfirmShippingData").click()
        self.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
        