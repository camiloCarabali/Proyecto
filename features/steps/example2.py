from behave import *
from selenium import webdriver
import time


@given('el navegador esta abierto')
def iniciarNavegador(context):
    context.driver = webdriver.Chrome()


@when('ingreso a la vista del login')
def abrirServidor(context):
    context.driver.get("http://localhost:8000/accounts/login/")
    time.sleep(3)


@when('le doy al boton visitante')
def presionarBoton(context):
    context.driver.find_elements_by_xpath('//a[contains(text(),"Visitante")]')[0].click()
    time.sleep(3)


@then('he podido ingresar a la aplicacion como visitante')
def cerrarNavegador(context):
    context.driver.close()

