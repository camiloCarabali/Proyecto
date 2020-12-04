#Juan Camilo Carabali Caracas
#Alejandro Rosas Cuesta
#Creaion de prueba gherkin #5

Feature: editar el dia de finalizacion de una actividad en la aplicacion
  como usuario web deseo modificar el dia de finalizacion de una actividad.

  Background:
    Given el navegador esta abierto
    When ingreso a la vista login
    And lleno el campo username
    And lleno el campo password
    And le doy al boton login
    And me redirecciona al index

  Scenario: editar fecha de finalizacion
    And presiono el boton del menu
    And le doy a la opcion ver actividades
    And me redirecciona a las actividades creadas
    And presiono el boton editar
    And me redirecciona al formulario
    And edito el dia de la finalizacion
    And presiono el boton crear
    And me redirecciona a las actividades
    Then he podido editar una actividad