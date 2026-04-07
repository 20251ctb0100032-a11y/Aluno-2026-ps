#==============================================================================
# ARQUIVO: trabalho.py
#DISCIPLINA: Programação de Sistemas (2026-PS)
#Aula:14 - Mini Projeto: Sistema de Cadastro de Jogos
#Integrantes: Kauê Mendes, Luiz Carlos, Luiz
#==============================================================================
import os  # isso aqui serve pra mexer com arquivos/pastas

# ===== CONFIGURAÇÕES =====
# define onde o arquivo vai ficar (no mesmo lugar do código)
ARQUIVO = os.path.join(os.path.dirname(__file__), "dados.txt") 

SEPARADOR = "|"  # separador dos dados dentro do arquivo

catalogo = []  # lista onde ficam os jogos


# ===== SALVAR NO ARQUIVO =====
def salvar_arquivo(): 
    # abre o arquivo no modo de escrita (apaga e escreve tudo de novo)
    with open(ARQUIVO, "w", encoding="utf-8") as f: 
        for jogo in catalogo: 
            # junta as informações do jogo em uma linha só
            linha = SEPARADOR.join([ 
                jogo["Nome do jogo"], 
                jogo["Gênero"], 
                jogo["Criador"], 
                jogo["Data de lançamento"] 
            ])
            f.write(linha + "\n")  # escreve no arquivo


# ===== CARREGAR DO ARQUIVO =====
def carregar_arquivo():  
    global catalogo 
    catalogo = []  # limpa a lista pra não duplicar
    
    try: 
        with open(ARQUIVO, "r", encoding="utf-8") as f: 
            for linha in f: 
                # separa os dados usando o "|"
                dados = linha.strip().split(SEPARADOR) 
                
                # se tiver tudo certo (4 campos), adiciona
                if len(dados) == 4: 
                    catalogo.append({ 
                        "Nome do jogo": dados[0], 
                        "Gênero": dados[1], 
                        "Criador": dados[2], 
                        "Data de lançamento": dados[3] 
                    })
    except FileNotFoundError: 
        # se não existir arquivo ainda
        print("Arquivo não encontrado, será criado automaticamente.")


# ===== LISTAR JOGOS =====
def listar_jogos(): 
    print("\n" + "=" * 50)
    print(" Sistema de Cadastro de Jogos")
    print("=" * 50)
    
    # se não tiver nada
    if not catalogo: 
        print("Nenhum jogo cadastrado.")
        return
          
    # mostra todos os jogos com número
    for i, jogo in enumerate(catalogo, 1): 
        print(f"{i}. {jogo['Nome do jogo']} - {jogo['Gênero']} | {jogo['Criador']} [{jogo['Data de lançamento']}]")
    
    print("=" * 50)


# ===== ENTRADA SEGURA =====
def entrada_segura(msg): 
    try:
        return input(msg).strip()  # lê o que o usuário digitar
    except KeyboardInterrupt: 
        # se apertar Ctrl+C
        print("\nCancelado.")
        return None


# ===== ADICIONAR JOGO =====
def adicionar_jogo(): 
    print("\n--- Adicionar jogo ---")

    nome = entrada_segura("Nome: ") 
    if not nome: return  # se não digitar nome, cancela

    genero = entrada_segura("Gênero: ") 
    criador = entrada_segura("Criador: ") 
    data = entrada_segura("Data: ") 

    # verifica se tá tudo preenchido
    if not genero or not criador or not data:
        print("Todos os campos são obrigatórios!")
        return

    # adiciona na lista
    catalogo.append({ 
        "Nome do jogo": nome,
        "Gênero": genero,
        "Criador": criador,
        "Data de lançamento": data
    })

    salvar_arquivo()  # salva no arquivo
    print("Jogo salvo!")


# ===== BUSCAR JOGO =====
def buscar_jogo(): 
    termo = entrada_segura("Buscar: ")
    if not termo: return

    termo = termo.lower() 
    encontrados = False

    # procura pelo nome
    for jogo in catalogo: 
        if termo in jogo["Nome do jogo"].lower():
            print(f"{jogo['Nome do jogo']} - {jogo['Gênero']} | {jogo['Criador']} [{jogo['Data de lançamento']}]")
            encontrados = True

    if not encontrados:
        print("Nada encontrado.")


# ===== REMOVER JOGO =====
def remover_jogo():
    listar_jogos()

    if not catalogo:
        return

    try:
        # pede o número do jogo
        indice = int(entrada_segura("Número do jogo para remover: "))
        
        if 1 <= indice <= len(catalogo):
            removido = catalogo.pop(indice - 1)  # remove da lista
            salvar_arquivo()
            print(f"Jogo '{removido['Nome do jogo']}' removido!")
        else:
            print("Número inválido.")
    
    except (ValueError, TypeError):
        print("Entrada inválida.")


# ===== MENU =====
def menu(): 
    carregar_arquivo()  # carrega tudo quando começa  

    while True: 
        print("\n1-Listar 2-Adicionar 3-Buscar 4-Remover 0-Sair")
        op = entrada_segura("Escolha: ")

        if op == "1": 
            listar_jogos()
        elif op == "2": 
            adicionar_jogo()
        elif op == "3": 
            buscar_jogo()
        elif op == "4":
            remover_jogo()
        elif op == "0": 
            salvar_arquivo()
            break
        else:
            print("Inválido")


# inicia o programa
if __name__ == "__main__": 
    menu()