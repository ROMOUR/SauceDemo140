Feature: Cadastro na Giuliana Flores

  Scenario: Cadastro de usuário na Giuliana Flores
    Given que estou na página inicial da Giuliana Flores
    When clico no botão de login
    And clico no link "Ainda não sou cadastrado"
    And preencho o formulário de cadastro com nome, CPF, email, senha, CEP, número de endereço, complemento e número de celular
    Then clico no botão finzalizo o cadastro
