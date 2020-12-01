Feature: Ingresar al proyecto

  Scenario: Entrar a la aplicacion
    Given el navegador esta abierto
    When ingreso a la vista login
    And lleno el campo username
    And lleno el campo password
    And le doy al boton login
    Then he ingrasado a la aplicacion
