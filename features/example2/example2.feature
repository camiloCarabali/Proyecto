#Juan Camilo Carabali Caracas
#Alejandro Rosas Cuesta
#Creaion de prueba gherkin #2

Feature: Ingresar como visitante
  como usuario web deseo entrar a la aplicacion como un visitante.

  Scenario: Ingreso a la aplicacion como visitante
    Given el navegador esta abierto
    When ingreso a la vista del login
    And le doy al boton visitante
    Then he podido ingresar a la aplicacion como visitante