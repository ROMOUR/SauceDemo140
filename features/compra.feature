Feature: Seleção de Produto na Giuliana Flores

  Scenario: Selecionar um produto e efetuar a compra
    Given que estou na página inicial da Giuliana Flores
    When seleciono um produto
    And preencho o CEP e o complemento
    And confirmo os dados de entrega
    And adiciono o produto ao carrinho
    Then sou redirecionado para a página de pagamento