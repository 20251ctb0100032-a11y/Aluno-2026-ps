# SysControl v2.0

## Aluno

**Nome:** (Luiz Carlos Oliveira Neto)

## Variante

**Veículo**

## Descrição

Este projeto foi desenvolvido em Java utilizando os conceitos de Programação Orientada a Objetos (POO), aplicando classes, objetos, encapsulamento, validações e métodos de comportamento.

## Atributos

* modelo
* placa
* ano
* combustivel
* ligado

Todos os atributos foram declarados como `private`.

## Validações implementadas

* O modelo não pode ser vazio.
* Não é permitido abastecer com valor menor ou igual a zero.
* Não é permitido dirigir com combustível insuficiente, consumo inválido ou com o veículo desligado.

## Métodos de comportamento

* `ligar()`
* `abastecer(int litros)`
* `dirigir(int consumo)`
* `resumo()`

## Casos de teste

1. Criação de um veículo com dados válidos.
2. Tentativa de alterar o modelo para um texto vazio.
3. Tentativa de abastecer com valor negativo.
4. Ligar o veículo e dirigir.
5. Tentar dirigir sem combustível suficiente.

## Arquivos do projeto

* `Veiculo.java`
* `Main.java`

## Tecnologias utilizadas

* Java
* Programação Orientada a Objetos (POO)
