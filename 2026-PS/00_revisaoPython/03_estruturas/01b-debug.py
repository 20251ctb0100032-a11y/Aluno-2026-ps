
# =====================================
# SISTEMA DE BIBLIOTECA - VERSÃO CORRIGIDA
# =====================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dado
# Autor      : [Luiz Carlos Oliveira Neto]
# Data       : [26/02/2025]
# Repositorio: https://github.com
# =====================================

# ---- LISTAS: CONCEITO BÁSICO ----
titulos = [
    "O Programador Pragmático",
    "Código Limpo",
    "Entendendo Algoritmos",
]

print("Primeiro livro:", titulos[0])
print("Último livro   :", titulos[-1])
print("Total de livros :", len(titulos))

# ---- MÉTODOS DE LISTA ----
print("\n--- Operações na lista ---")
titulos.append("Python Fluente")
busca = "Código Limpo"
if busca in titulos:
    print(f'"{busca}" está no catálogo.')

titulos.sort()
if "Entendendo Algoritmos" in titulos:
    titulos.remove("Entendendo Algoritmos")

# ---- DICIONÁRIOS: CONCEITO BÁSICO ----
livro = {
     "titulo":     "O Programador Pragmático",
     "autor":      "Andrew Hunt",
     "ano":        1999,
     "disponivel": True,
}

# ---- CATÁLOGO: LISTA DE DICIONÁRIOS ----
catalogo_principal = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999, "disponivel": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008, "disponivel": False},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2016, "disponivel": True},
]

print("\n=== Catálogo da Biblioteca ===")
for item in catalogo_principal:
    status = "✅ Disponível" if item["disponivel"] else "📕 Emprestado"
    print(f' {item["titulo"]} ({item["ano"]}) | {status}')

# =====================================
# RESOLUÇÃO DO EXERCÍCIO: 01b-debug.py
# =====================================
# Abaixo estão as correções dos 4 erros propositais.

catalogo = [
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel": False},
    {"titulo": "Python fluente", "autor": "Luciano Ramalho", "disponivel": True},
]

# CORREÇÃO 1: O índice 3 não existe (a lista vai de 0 a 2). Mudado para [0].
print("\n--- Resolução do Debug ---")
print("Primeiro livro:", catalogo[0]["titulo"]) 

# CORREÇÃO 2: Ajustado \m para \n e lógica de 'disponivel' para True (para mostrar os ✅).
print("\nLivros disponíveis:")
for livro in catalogo:
    if livro["disponivel"] == True:
        print(f' ✅ {livro["titulo"]}')

total = len(catalogo)
print(f"\nTotal de livros no exercício: {total}")

# CORREÇÃO 3: Adicionado .items() para poder acessar chave e valor simultaneamente.
print("\nAtributos do primeiro livro:")
for chave, valor in catalogo[0].items():
    print(f' {chave}: {valor}')

# CORREÇÃO 4: Chave corrigida de "Autor" (Maiúsculo) para "autor" (Minúsculo).
primeiro_autor = catalogo[0]["autor"]
print("\nAutor do primeiro livro:", primeiro_autor)
