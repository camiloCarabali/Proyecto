#Juan Camilo Carabali Caracas
#Alejandro Rosas Cuesta
#Creaion de prueba gherkin #3

Feature: Crear una nueva actividad en la aplicacion
  como usuario web deseo crear una nueva actividad.

  Background:
    Given el navegador esta abierto
    When ingreso a la vista login
    And lleno el campo username
    And lleno el campo password
    And le doy al boton login
    And me redirecciona al index

  Scenario Outline: crear una actividad
    And le presiono el boton del menu
    And le doy a la opcion crear actividad
    And lleno el campo titulo "<titulo>"
    And selecciono el dia de inicio de la actividad
    And selecciono el mes de inicio de la actividad
    And selecciono el año de inicio de la actividad
    And selecciono el dia de finalizacion de la actividad
    And selecciono el mes de finalizacion de la actividad
    And selecciono el año de finalizacion de la actividad
    And lleno el campo descripcion "<descripcion>"
    And selecciono un usuario
    And le doy al boton crear
    And me redirecciona a las actividades creadas
    Then he podido crear una actividad en la aplicacion

  Examples:
    |titulo|descripcion|
    |prueba1 |descripcion1 |
    |prueba2 |descripcion2 |
