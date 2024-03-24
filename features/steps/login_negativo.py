from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estou na página inicial da Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.giulianaflores.com.br/")
    context.driver.implicitly_wait(10) 

@when('clico no botão de login')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#perfil-hidden > img").click()
    element = context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.CSS_SELECTOR, "#UrlLogin > a").click()

    
@when(u'preencho o campo de email com um email invalido')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("1 2 3 3 3")

@when(u'preencho o campo de senha com uma senha válida')
def step_impl(context):
   context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("         ")

@then(u'seleciono botão continuar')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()

@then(u'exibe uma mensagem de erro login negativo')
def step_impl(context):
    element = WebDriverWait(context.driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "span.font_erro"))
        )
    assert "Verifique o E-mail ou CPF digitado!" in element.text