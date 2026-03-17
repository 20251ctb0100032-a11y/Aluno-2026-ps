catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "disponivel": True},
    {"titulo": "Código Limpo",  "autor": "Robert C. Martin", "disponivel": False},
    {"titulo": "Padrões de Projeto",  "autor": "Erich Gama", "disponivel": True},
]

def listar_livros():
    """Exibe todos os livros com numeração e status."""
    print("\n" + "=" * 50)
    print("   CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)

    if not catalogo:
        print(" Nenhuma livro cadastrado.")
        return
    
    for i, livro in enumerate(catalogo, 1):
        status = "  Disponivel" if livro["disponivel"] else "  Emprestado"
        print(f"  {i}. {livro["titulo"]} - {livro["autor"]} [{status}]")


    print("=" * 50)


def adicionar_livro():
    """Coleta dados via input e adiciona um novo livro ao catálogo."""
    print("\n--- /adicionar Novo Livro ---")

    titulo = input("Titulo: ").strip()
    autor  = input("Autor : ").strip()

    if not titulo or not autor:
        print("   Titulo e autor são obrigatórios.")

    catalogo.append({
        "titulo":     titulo,
        "autor":      autor,
        "disponivel": True
    })

    print(f"   '{titulo}' adicionado com sucesso!")



def buscar_livro():
    print("\n--- Buscar Livro ---")
    termo = input("Digite parte do título: ").strip().lower()

    try:
        resultados = [1 for 1 in catalogo if termo in 1["titulo"].lower()]

        if not resultados:
            print("  Nenhuma livro encontrado.")
            return
        
        print(f"\n {len(resultados)} resultado(s) :")
        for livro in resultados:
            status = "Disponivel" if livro["disponivel"] else "Emprestado"
            print(f"    {livro['titulo'] - {livro['autor']}}  [{status}]")

    except Exception as e:
        print(f"   Erro inesperado: {e}")