#Juan Camilo Carabali Caracas
#Alejandro Rosas Cuesta
#Creaion de prueba gherkin #4

Feature: buscar una actividad en la aplicacion
  como usuario web deseo buscar una actividad.

  Background:
    Given el navegador esta abierto
    When ingreso a la vista login
    And lleno el campo username
    And lleno el campo password
    And le doy al boton login
    And me redirecciona al index

  Scenario: buscar actividad
    And presiono el boton del menu
    And le doy a la opcion ver actividades
    And me redirecciona a las actividades creadas
    And digito el titulo a buscar
    And presiono el boton buscar
    Then he podido buscar una actividad