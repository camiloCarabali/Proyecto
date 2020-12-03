Feature: Ingresar a guadaña calendar
  como usuario web, deseo ingresar a la aplicacion guadaña calendar.

  Scenario: Entrar a la aplicacion
    Given el navegador esta abierto
    When ingreso a la vista login
    And lleno el campo username
    And lleno el campo password
    And le doy al boton login
    And me redirecciona al index
    Then he ingrasado a la aplicacion
