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

@when('clico no link "{link}"')
def step_impl(context, link):
    context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()

@when('preencho o formulário de cadastro com nome, CPF, email, senha, CEP, número de endereço, complemento e número de celular')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_txtName").click()
    context.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Rodolfo Moura")
    context.driver.find_element(By.ID, "ContentSite_txtCpf").click()
    context.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("308.835.520-19")
    context.driver.find_element(By.ID, "ContentSite_txtEmail").click()
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("anahit3676@uorak.com")
    context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").click()
    context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("@La12345")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").click()
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("18694-076")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").click()
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("66")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtComplement").click()
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtComplement").send_keys("casa")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").click()
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("14996394136")


@then(u'clico no botão finzalizo o cadastro')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
    context.driver.find_element(By.ID, "perfil-hidden").click()