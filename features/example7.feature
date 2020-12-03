Feature: ver calendario de actividades de la aplicacion
  como usuario web deseo visualizar el calendario de actividades de la aplicacion.

  Background:
    Given el navegador esta abierto
    When ingreso a la vista login
    And lleno el campo username
    And lleno el campo password
    And le doy al boton login
    And me redirecciona al index

  Scenario: visualizar calendario
    And presiono el boton del menu
    And le doy a la opcion ver calendario
    And me redirecciona al calendario de actividades
    Then he podido visualizar el calendario de actividades