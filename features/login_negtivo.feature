Feature: Login na Giuliana Flores

  Scenario: Login Negativo
    Given que estou na página inicial da Giuliana Flores
    When clico no botão de login
    And preencho o campo de email com um email invalido 
    And preencho o campo de senha com uma senha válida
    Then seleciono botão continuar
    Then exibe uma mensagem de erro login negativo 