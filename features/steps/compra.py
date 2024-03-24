from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('que estou na página inicial da Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.url = "https://www.giulianaflores.com.br/"
    context.driver.get(context.url)

@when('seleciono um produto')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "carousel-brands .owl-item:nth-child(1) img").click()
    context.driver.find_element(By.CSS_SELECTOR, "img[src*='27120gg.jpg']").click()

@when('preencho o CEP e o complemento')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_txtZip").click()
    context.driver.find_element(By.ID, "ContentSite_txtZip").send_keys("18694")
    context.driver.find_element(By.ID, "ContentSite_txtZipComplement").click()
    context.driver.find_element(By.ID, "ContentSite_txtZipComplement").send_keys("076")
    context.driver.find_element(By.CSS_SELECTOR, ".jOpenShippingPopup").click()
    time.sleep(5)

@when('confirmo os dados de entrega')
def step_impl(context):
    context.driver.find_element(By.ID, "btConfirmShippingData").click()

@when('adiciono o produto ao carrinho')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()

@then(u'sou redirecionado para a página de pagamento')
def step_impl(context):
   context.driver.find_element(By.CLASS_NAME, "bg_carrinho jBasketLink").click()
   context.driver.find_element(By.CLASS_NAME, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click() 

   