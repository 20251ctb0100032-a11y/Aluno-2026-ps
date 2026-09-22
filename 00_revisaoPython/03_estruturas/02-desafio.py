# =====================================
# SISTEMA DE BIBLIOTECA - VERSÃO FINAL COMENTADA
# =====================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dado
# Autor      : [Luiz Carlos Oliveira Neto]
# Data       : [26/02/2025]
# Repositorio: https://github.com
# =====================================

# ---- CONCEITOS INICIAIS (LISTAS) ----

# Uma lista é uma coleção ordenada de itens
titulos = ["O Programador Pragmático", "Código Limpo", "Entendendo Algoritmos"]

# Acessamos itens pelo índice: 0 é o primeiro, -1 é o último
print("Primeiro livro:", titulos[0])
print("Total de livros :", len(titulos))

# .append() adiciona ao final, .sort() coloca em ordem alfabética
titulos.append("Python Fluente")
titulos.sort()

# ---- CONCEITOS INICIAIS (DICIONÁRIOS) ----

# Dicionários guardam pares de Chave: Valor
livro_exemplo = {
     "titulo": "Código Limpo",
     "autor": "Robert C. Martin",
     "ano": 2008,
     "disponivel": True,
}

# .get() é seguro: se a chave não existir, ele não trava o programa
editora = livro_exemplo.get("editora", "Não informada")

# =========================================================
# RESOLUÇÃO DO ARQUIVO: 01b-debug.py (COM AS CORREÇÕES)
# =========================================================

catalogo = [
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel": False},
    {"titulo": "Python fluente", "autor": "Luciano Ramalho", "disponivel": True},
]

# CORREÇÃO 1: O erro era catalogo[3]. Como a lista tem 3 itens, os índices são 0, 1 e 2.
# O índice [0] pega o primeiro dicionário da lista.
print("\nPrimeiro livro do catálogo:", catalogo[0]["titulo"])

# CORREÇÃO 2: O erro era "\m" e "disponivel == False".
# Usamos "\n" para nova linha e filtramos por True para mostrar os que têm o ✅.
print("\nLivros disponíveis:")
for livro in catalogo:
    if livro["disponivel"] == True:
        print(f" ✅ {livro['titulo']}")

# CORREÇÃO 3: O erro era 'for chave, valor in catalogo[0]'.
# Dicionários precisam do método .items() para percorrer chave e valor ao mesmo tempo.
print("\nAtributos do primeiro livro:")
for chave, valor in catalogo[0].items():
    print(f" {chave}: {valor}")

# CORREÇÃO 4: O erro era ["Autor"] com 'A' maiúsculo.
# Python diferencia maiúsculas/minúsculas (Case Sensitive). A chave correta é "autor".
primeiro_autor = catalogo[0]["autor"]
print("\nAutor do primeiro livro:", primeiro_autor)

# Exibição do total final
print(f"\nTotal de livros processados: {len(catalogo)}")
