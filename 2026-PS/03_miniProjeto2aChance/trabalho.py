#==============================================================================
# ARQUIVO: trabalho.py
# DISCIPLINA: Programação de Sistemas (2026-PS)
# Aula:14 - Mini Projeto
# Integrantes: Kauê Mendes, Luiz Carlos, Luiz
#==============================================================================

import os  # importa biblioteca para trabalhar com arquivos e caminhos

# ===== CONFIGURAÇÕES =====

# define o caminho do arquivo "dados.txt" na mesma pasta do programa
ARQUIVO = os.path.join(os.path.dirname(__file__), "dados.txt") 

SEPARADOR = "|"  # caractere usado para separar os dados no arquivo

catalogo = []  # lista onde os contatos serão armazenados


#==============================================================================
# SISTEMA DE AGENDA DE CONTATOS
#==============================================================================


def salvar_arquivo():
    """Função que salva todos os contatos no arquivo."""
    try:  # tenta executar o bloco (caso dê erro, vai pro except)
        with open(ARQUIVO, "w", encoding="utf-8") as f:  # abre o arquivo para escrita
            for contato in catalogo:  # percorre todos os contatos da lista
                
                # junta os dados do contato usando o separador
                linha = SEPARADOR.join([
                    contato["Nome"],     
                    contato["Telefone"],  
                    contato["Email"]     
                ])
                f.write(linha + "\n")  # escreve no arquivo
    except Exception as e:
        print("Erro ao salvar:", e)  # mostra erro se acontecer


def carregar_arquivo():
    """Função que carrega contatos do arquivo para a lista catalogo."""
    global catalogo  # permite modificar a variável global
    catalogo = []  # limpa a lista antes de carregar

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:  # abre o arquivo para leitura
            for linha in f:  # percorre cada linha do arquivo
                
                dados = linha.strip().split(SEPARADOR)  # separa os dados

                if len(dados) == 3:  # verifica se tem os 3 campos
                    catalogo.append({
                        "Nome": dados[0],
                        "Telefone": dados[1],
                        "Email": dados[2]
                    })
    except FileNotFoundError:
        print("Arquivo será criado automaticamente.")  # se não existir arquivo


def entrada_segura(msg):
    """Função que captura entrada do usuário com segurança."""
    try:
        return input(msg).strip()  # pega entrada e remove espaços
    except KeyboardInterrupt:
        print("\nCancelado.")
        return None  # retorna vazio se usuário cancelar


def listar_contatos():
    """Lista todos os contatos cadastrados."""
    print("\n" + "=" * 50)  # linha decorativa
    print("AGENDA DE CONTATOS")
    print("=" * 50)

    if not catalogo:  # verifica se lista está vazia
        print("Nenhum contato cadastrado.")
        return

    # contatos mostrando com número
    for i, contato in enumerate(catalogo, 1):
        print(f"{i}. {contato['Nome']} | Tel: {contato['Telefone']} | Email: {contato['Email']}")


def adicionar_contato():
    """Adiciona um novo contato com validação."""
    print("\n--- Novo Contato ---")

    nome = entrada_segura("Nome: ")
    if not nome:  # se nome estiver vazio
        return

    telefone = entrada_segura("Telefone: ")
    email = entrada_segura("Email: ")

    # valida se todos os campos foram preenchidos
    if not telefone or not email:
        print("Todos os campos são obrigatórios!")
        return

    # valida se email tem "@"
    if "@" not in email:
        print("Email inválido!")
        return

    # adiciona contato na lista
    catalogo.append({
        "Nome": nome,
        "Telefone": telefone,
        "Email": email
    })

    salvar_arquivo()  # salva no arquivo
    print("Contato salvo!")


def buscar_contato():
    """Busca contatos pelo nome ou telefone."""
    termo = entrada_segura("Buscar: ")
    if not termo:
        return

    termo = termo.lower()  # deixa tudo minúsculo
    encontrados = False  # variável para controle

    for contato in catalogo:  # percorre lista
        # verifica se termo está no nome ou telefone
        if termo in contato["Nome"].lower() or termo in contato["Telefone"]:
            print(f"{contato['Nome']} | Tel: {contato['Telefone']} | Email: {contato['Email']}")
            encontrados = True

    if not encontrados:
        print("Nada encontrado.")


def remover_contato():
    """Remove um contato pelo número."""
    listar_contatos()  # mostra lista

    if not catalogo:
        return

    try:
        # pede número e converte para inteiro
        indice = int(entrada_segura("Número para remover: "))

        # verifica se número é válido
        if 1 <= indice <= len(catalogo):
            removido = catalogo.pop(indice - 1)  # remove da lista
            salvar_arquivo()
            print(f"Contato '{removido['Nome']}' removido!")
        else:
            print("Número inválido.")

    except:
        print("Erro na entrada.")  # erro caso digite algo errado


def editar_contato():
    """Edita um contato existente."""
    listar_contatos()

    if not catalogo:
        return

    try:
        indice = int(entrada_segura("Número para editar: "))

        if 1 <= indice <= len(catalogo):
            contato = catalogo[indice - 1]

            print("Deixe vazio para não alterar")

            nome = entrada_segura("Novo nome: ")
            telefone = entrada_segura("Novo telefone: ")
            email = entrada_segura("Novo email: ")

            # só altera se o usuário digitou algo
            if nome:
                contato["Nome"] = nome
            if telefone:
                contato["Telefone"] = telefone
            if email:
                if "@" not in email:
                    print("Email inválido!")
                    return
                contato["Email"] = email

            salvar_arquivo()
            print("Contato atualizado!")

        else:
            print("Número inválido.")

    except:
        print("Erro na edição.")


def menu():
    """Menu principal do sistema."""
    carregar_arquivo()  # carrega dados ao iniciar

    while True:  # loop infinito do menu
        print("\n1-Listar 2-Adicionar 3-Buscar 4-Remover 5-Editar 0-Sair")
        op = entrada_segura("Escolha: ")

        # verifica opção escolhida
        if op == "1":
            listar_contatos()
        elif op == "2":
            adicionar_contato()
        elif op == "3":
            buscar_contato()
        elif op == "4":
            remover_contato()
        elif op == "5":
            editar_contato()
        elif op == "0":
            salvar_arquivo()
            break  # sai do programa
        else:
            print("Opção inválida.")


# ponto de entrada do programa
if __name__ == "__main__":
    menu()  # inicia o sistema