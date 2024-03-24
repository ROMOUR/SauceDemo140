from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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


@when(u'preencho o campo de email com um email válido')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("anahit3676@uorak.com")

@when(u'preencho o campo de senha com uma senha válida')
def step_impl(context):
   context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("@La12345")

@then(u'seleciono botão continuar')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()