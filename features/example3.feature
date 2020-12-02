Feature: Crear una nueva actividad en la aplicacion
  como usuario web deseo crear una nueva actividad.

  Scenario: crear una actividad
    Given el navegador esta abierto
    When ingreso a la vista login
    And lleno el campo username
    And lleno el campo password
    And le doy al boton login
    And le presiono el boton del menu
    And le doy a la opcion crear actividad
    And lleno el campo titulo
    And selecciono el dia de inicio de la actividad
    And selecciono el mes de inicio de la actividad
    And selecciono el año de inicio de la actividad
    And selecciono el dia de finalizacion de la actividad
    And selecciono el mes de finalizacion de la actividad
    And selecciono el año de finalizacion de la actividad
    And lleno el campo descripcion
    And selecciono un usuario
    And le doy al boton crear
    Then he podido crear una actividad en la aplicacion