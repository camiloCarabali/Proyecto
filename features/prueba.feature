Feature: Ingresar al proyecto

  Scenario: Ingresar a la aplicacion "Guadaña calendar"
    Given que estoy en el servidor
    And tengo conexion a este
    And tengo mis credenciales para iniciar sesion
    When introduzco mis datos en el login
    And le doy al boton ingresar
    And se realiza la validacion
    And me redirecciona al index
    Then he podido ingresar a la aplicacion exitosamente