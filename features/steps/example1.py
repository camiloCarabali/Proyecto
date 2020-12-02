# from behave import *
# from selenium import webdriver
# import time
#
# @given('el navegador esta abierto')
# def iniciarNavegador(context):
#     context.driver = webdriver.Chrome()
#
#
# @when('ingreso a la vista login')
# def abrirServidor(context):
#     context.driver.get("http://localhost:8000/accounts/login/")
#     time.sleep(3)
#
#
# @when('lleno el campo username')
# def llenarUsername(context):
#     username_input = context.driver.find_element_by_xpath('//input[@name="username"]')
#     time.sleep(3)
#     username_input.send_keys('camilocarabali')
#     time.sleep(3)
#
# @when('lleno el campo password')
# def llenarPassword(context):
#     password_input = context.driver.find_element_by_xpath('//input[@name="password"]')
#     time.sleep(3)
#     password_input.send_keys('juan19991995')
#     time.sleep(3)
#
# @when('le doy al boton login')
# def presionarBoton(context):
#     context.driver.find_elements_by_xpath('//button[@class="login100-form-btn"]')[0].click()
#     time.sleep(5)
#
#
# @then('he ingrasado a la aplicacion')
# def cerrarNavegador(context):
#     context.driver.close()
