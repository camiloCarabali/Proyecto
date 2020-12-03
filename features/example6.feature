Feature: eliminar una actividad en la aplicacion
  como usuario web deseo eliminar una actividad de la aplicacion.

  Background:
    Given el navegador esta abierto
    When ingreso a la vista login
    And lleno el campo username
    And lleno el campo password
    And le doy al boton login
    And me redirecciona al index

  Scenario: eliminar actividad
    And presiono el boton del menu
    And le doy a la opcion ver actividades
    And me redirecciona a las actividades creadas
    And presiono el boton eliminar
    And presiono el boton confirmar
    And me redirecciona a las actividades
    Then he podido eliminar una actividad