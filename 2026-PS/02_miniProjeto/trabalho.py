import os
ARQUIVO = os.path.join(os.path.dirname(__file__), "dados.txt") # nome do arquivo onde os jogos serão salvos
SEPARADOR = "|" # separa os campos no catalogo .txt

catalogo = [] # lista de dicionários, cada um representando um jogo

def salvar_arquivo(): # grava a lista de jogos no catalogo .txt
    with open(ARQUIVO, "w", encoding="utf-8") as f: # abre o arquivo para escrita
        for jogo in catalogo: # para cada jogo na lista
            linha = SEPARADOR.join([ # junta os campos do jogo em uma linha usando o separador
                jogo["Nome do jogo"], # campo "Nome do jogo"
                jogo["Gênero"], # campo "Gênero"
                jogo["Criador"], # campo "Criador"
                jogo["Data de lançamento"] # campo "Data de lançamento"
            ])
            f.write(linha + "\n") # escreve a linha no arquivo, seguida de uma nova linha

def carregar_arquivo(): # lê o arquivo catalogo .txt e preenche a lista de jogos
    global catalogo # usa a variável global catalogo para armazenar os jogos lidos do arquivo
    try: # tenta abrir o arquivo para leitura
        with open(ARQUIVO, "r", encoding="utf-8") as f: # abre o arquivo para leitura
            for linha in f: # para cada linha do arquivo
                dados = linha.strip().split(SEPARADOR) # remove espaços em branco e separa os campos usando o separador
                if len(dados) == 4: # verifica se a linha tem os 4 campos esperados
                    catalogo.append({ # adiciona um dicionário com os campos do jogo à lista de catalogo
                        "Nome do jogo": dados[0], # campo "Nome do jogo" é o primeiro elemento da linha
                        "Gênero": dados[1], # campo "Gênero"
                        "Criador": dados[2], # campo "Criador"
                        "Data de lançamento": dados[3] # campo "Data de lançamento"
                    })
    except FileNotFoundError: # se o arquivo não existir, inicia com um catalogo vazio e avisa o usuário
        print("Arquivo não encontrado, será criado automaticamente.")

def listar_jogos(): # exibe a lista de jogos cadastrados no console
    print("\n" + "=" * 50)
    print(" Sistema de Cadastro de Jogos")
    print("=" * 50)
    
    if not catalogo: # se a lista de jogos estiver vazia, avisa o usuário e retorna
        print("Nenhum jogo cadastrado.")
        return
          
    for i, jogo in enumerate(catalogo, 1): # para cada jogo na lista, exibe o número, nome, gênero, criador e data de lançamento
        print(f"{i}. {jogo['Nome do jogo']} - {jogo['Gênero']} | {jogo['Criador']} [{jogo['Data de lançamento']}]")
    print("=" * 50)

def entrada_segura(msg):  # função para ler entrada do usuário, tratando interrupção por teclado (Ctrl+C)
    try:
        return input(msg).strip()
    except KeyboardInterrupt: # se o usuário pressionar Ctrl+C, captura a exceção e retorna None
        print("\nCancelado.")
        return None

def adicionar_jogo(): # função para adicionar um novo jogo ao catalogo, solicitando os dados do usuário e salvando no arquivo
    print("\n--- Adicionar jogo ---")

    nome = entrada_segura("Nome: ") # solicita o nome do jogo e armazena na variável nome, usando a função entrada_segura para tratar interrupção por teclado
    if not nome: return

    genero = entrada_segura("Gênero: ") # solicita o gênero do jogo e armazena na variável genero, usando a função entrada_segura para tratar interrupção por teclado
    criador = entrada_segura("Criador: ") # solicita o criador do jogo e armazena na variável criador, usando a função entrada_segura para tratar interrupção por teclado
    data = entrada_segura("Data: ") # solicita a data de lançamento do jogo e armazena na variável data, usando a função entrada_segura para tratar interrupção por teclado

    catalogo.append({ # adiciona um dicionário com os dados do jogo à lista de catalogo
        "Nome do jogo": nome,
        "Gênero": genero,
        "Criador": criador,
        "Data de lançamento": data
    })

    salvar_arquivo()  # salva a lista de jogos atualizada no arquivo catalogo .txt
    print("Jogo salvo no arquivo!")

def buscar_jogo(): # função para buscar jogos no catalogo, solicitando um termo de busca e exibindo os jogos que correspondem ao termo
    termo = entrada_segura("Buscar: ")
    if not termo: return

    termo = termo.lower() # converte o termo de busca para minúsculas para facilitar a comparação com os nomes dos jogos

    for jogo in catalogo: # para cada jogo na lista de catalogo, verifica se o termo de busca está presente no nome do jogo (convertido para minúsculas)
        if termo in jogo["Nome do jogo"].lower():
            print(jogo["Nome do jogo"], "-", jogo["Criador"])

def menu(): # função principal que exibe o menu de opções para o usuário e chama as funções correspondentes às opções escolhidas, além de carregar os jogos do arquivo ao iniciar
    carregar_arquivo()  

    while True: # loop infinito para exibir o menu até que o usuário escolha sair
        print("\n1-Listar 2-Adicionar 3-Buscar 0-Sair")
        op = entrada_segura("Escolha: ")

        if op == "1": # se o usuário escolher a opção 1, chama a função listar_jogos para exibir a lista de jogos cadastrados
            listar_jogos()
        elif op == "2": # se o usuário escolher a opção 2, chama a função adicionar_jogo para solicitar os dados de um novo jogo e adicioná-lo ao catalogo
            adicionar_jogo()
        elif op == "3": # se o usuário escolher a opção 3, chama a função buscar_jogo para solicitar um termo de busca e exibir os jogos que correspondem ao termo
            buscar_jogo()
        elif op == "0": # se o usuário escolher a opção 0, chama a função salvar_arquivo para garantir que os jogos sejam salvos no arquivo antes de sair, e depois quebra o loop para encerrar o programa
            salvar_arquivo()
            break
        else:
            print("Inválido")

if __name__ == "__main__": # se este arquivo for executado diretamente, chama a função
    menu() # para iniciar o programa, exibindo o menu e permitindo ao usuário interagir com o sistema de cadastro de jogos