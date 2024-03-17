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
        self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click ()
        self.driver.find_element(By.ID, "ContentSite_txtName").click()
        self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Souza junior")
        self.driver.find_element(By.ID, "ContentSite_txtCpf").click()
        self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("476.872.170-20")
        self.driver.find_element(By.ID, "ContentSite_txtEmail").click()
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("konimba323@uorak.com")
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").click()
        self.driver.execute_script("window.scrollTo(0,501)")
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("@L12345")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("18694-076")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("123")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("1498425-1234")
        self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
        self.driver.find_element(By.ID, "perfil-hidden").click()
        