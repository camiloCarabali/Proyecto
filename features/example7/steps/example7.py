'''
Juan Camilo Carabali Caracas
Alejandro Rosas Cuesta
Creacion de prueba automatizada #7
'''

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


@when('le doy a la opcion ver calendario')
def step_impl(context):
    context.driver.find_elements_by_xpath('//a[contains(text(),"Ver Calendario")]')[0].click()
    time.sleep(2)


@when('me redirecciona al calendario de actividades')
def step_impl(context):
    text = context.driver.find_element_by_xpath('//h1[contains(text(),"Calendario de Actividades")]').text
    assert text == "Calendario de Actividades"
    time.sleep(2)


@then('he podido visualizar el calendario de actividades')
def step_impl(context):
    context.driver.close()
