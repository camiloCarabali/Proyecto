from behave import *
from selenium import webdriver
import time


@given('el navegador esta abierto')
def inciarNavegador(context):
    context.driver = webdriver.Chrome()


@when('ingreso a la vista login')
def abrirServidor(context):
    context.driver.get("http://localhost:8000/accounts/login/")
    time.sleep(2)


@when('lleno el campo username')
def llenarUsername(context):
    username_input = context.driver.find_element_by_xpath('//input[@name="username"]')
    time.sleep(2)
    username_input.send_keys('camilocarabali')
    time.sleep(2)


@when('lleno el campo password')
def llenarPassword(context):
    password_input = context.driver.find_element_by_xpath('//input[@name="password"]')
    time.sleep(2)
    password_input.send_keys('juan19991995')
    time.sleep(2)


@when('le doy al boton login')
def presionarBotonLogin(context):
    context.driver.find_elements_by_xpath('//button[@class="login100-form-btn"]')[0].click()
    time.sleep(2)


@when('me redirecciona al index')
def validarIndex(context):
    text = context.driver.find_element_by_xpath('//h1[contains(text(),"Guadaña Calendar")]').text
    assert text == "Guadaña Calendar"
    time.sleep(2)


@when('presiono el boton del menu')
def presionarBotonMenu(context):
    context.driver.find_elements_by_xpath('//body/a[1]')[0].click()
    time.sleep(2)


@when('le doy a la opcion ver actividades')
def presionarOpcionVer(context):
    context.driver.find_elements_by_xpath('//a[contains(text(),"Ver Actividades")]')[0].click()
    time.sleep(2)


@when('me redirecciona a las actividades creadas')
def validarVer(context):
    text = context.driver.find_element_by_xpath('//h1[contains(text(),"Actividades Creadas")]').text
    assert text == "Actividades Creadas"
    time.sleep(2)


@when('digito el titulo a buscar')
def llenarCampoBuscar(context):
    password_input = context.driver.find_element_by_xpath('//input[@name="buscar"]')
    time.sleep(2)
    password_input.send_keys('titulo')
    time.sleep(2)


@when('presiono el boton buscar')
def presionarBotonBuscar(context):
    context.driver.find_elements_by_xpath('//button[contains(text(),"Buscar")]')[0].click()
    time.sleep(2)


@then('he podido buscar una actividad')
def cerrarNavegador(context):
    context.driver.close()
