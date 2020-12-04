'''
Juan Camilo Carabali Caracas
Alejandro Rosas Cuesta
Creacion de prueba automatizada #3
'''

from behave import *
from selenium import webdriver
import time


@given('el navegador esta abierto')
def iniciarNavegador(context):
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
    time.sleep(3)


@when('le presiono el boton del menu')
def presionarBotonMenu(context):
    context.driver.find_elements_by_xpath('//body/a[1]')[0].click()
    time.sleep(2)


@when('le doy a la opcion crear actividad')
def presionarOpcionCrear(context):
    context.driver.find_elements_by_xpath('//a[contains(text(),"Crear Actividad")]')[0].click()
    time.sleep(2)


@when('lleno el campo titulo "{titulo}"')
def ingresarTitulo(context, titulo):
    valor = context.driver.find_element_by_xpath('//input[@id="id_titulo"]')
    valor.send_keys(titulo)
    time.sleep(2)


@when('selecciono el dia de inicio de la actividad')
def seleccionarDiaInicio(context):
    context.driver.find_elements_by_xpath("//select[@name='fechaInicial_day']")[0].click()
    context.driver.find_elements_by_xpath("//option[text()='4']")[0].click()
    time.sleep(2)


@when('selecciono el mes de inicio de la actividad')
def seleccionarMesInicio(context):
    context.driver.find_elements_by_xpath("//select[@name='fechaInicial_month']")[0].click()
    context.driver.find_elements_by_xpath("//option[text()='Diciembre']")[0].click()
    time.sleep(2)


@when('selecciono el año de inicio de la actividad')
def seleccionarAñoInicio(context):
    context.driver.find_elements_by_xpath("//select[@name='fechaInicial_year']")[0].click()
    context.driver.find_elements_by_xpath("//option[text()='2020']")[0].click()
    time.sleep(2)


@when('selecciono el dia de finalizacion de la actividad')
def seleccionarDiaFinal(context):
    context.driver.find_elements_by_xpath("//select[@name='fechaFinal_day']")[0].click()
    context.driver.find_elements_by_xpath("//header/div[1]/h5[1]/form[1]/p[3]/select[1]/option[11]")[0].click()
    time.sleep(2)


@when('selecciono el mes de finalizacion de la actividad')
def seleccionarMesFinal(context):
    context.driver.find_elements_by_xpath("//select[@name='fechaFinal_month']")[0].click()
    context.driver.find_elements_by_xpath("//header/div[1]/h5[1]/form[1]/p[3]/select[2]/option[13]")[0].click()
    time.sleep(2)


@when('selecciono el año de finalizacion de la actividad')
def seleccionarAñoFinal(context):
    context.driver.find_elements_by_xpath("//select[@name='fechaFinal_year']")[0].click()
    context.driver.find_elements_by_xpath("//header/div[1]/h5[1]/form[1]/p[3]/select[3]/option[2]")[0].click()
    time.sleep(2)


@when('lleno el campo descripcion "{descripcion}"')
def ingresarDescripcion(context, descripcion):
    valor = context.driver.find_element_by_xpath('//textarea[@id="descripcion"]')
    valor.send_keys(descripcion)
    time.sleep(2)


@when('selecciono un usuario')
def seleccionarUsuario(context):
    context.driver.find_elements_by_xpath('//option[contains(text(),"Alejandro")]')[0].click()
    time.sleep(2)


@when('le doy al boton crear')
def botonCrear(context):
    context.driver.find_elements_by_xpath('//button[contains(text(),"CREAR")]')[0].click()
    time.sleep(5)


@when('me redirecciona a las actividades creadas')
def validarCrear(context):
    text = context.driver.find_element_by_xpath('//h1[contains(text(),"Actividades Creadas")]').text
    assert text == "Actividades Creadas"
    time.sleep(3)


@then('he podido crear una actividad en la aplicacion')
def cerrarNavegador(context):
    context.driver.close()
