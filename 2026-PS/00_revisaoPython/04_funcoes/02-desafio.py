# =========================================================
# SISTEMA DE CÁLCULO DE IMC - CORRIGIDO E DESCRITO
# =========================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções
# Autor      : [Luiz Carlos Oliveira Neto]
# Data       : [03/03/2026]
# =========================================================

# ---- 1. FUNÇÕES DE INTERFACE (Sem retorno) ----

def exibir_cabecalho():
    """Exibe o título visual no terminal."""
    print("\n" + "=" * 40)
    print("      SISTEMA DE CÁLCULO DE IMC")
    print("=" * 40)

def exibir_rodape():
    """Exibe a mensagem de encerramento. (Corrigido: Adicionada definição)"""
    print("\n" + "=" * 40)
    print("   SISTEMA ENCERRADO COM SUCESSO")
    print("=" * 40)


# ---- 2. FUNÇÕES DE CÁLCULO E LÓGICA (Com parâmetros e retorno) ----

def calcular_imc(peso, altura):
    """Calcula o IMC. Fórmula: peso dividido pelo quadrado da altura."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Classifica o IMC de acordo com os limites da OMS e retorna classificação + emoji."""
    if imc < 18.5:
        return "Abaixo do peso", "⬇️"
    elif 18.5 <= imc < 25:
        return "Peso normal", "✅"
    elif 25 <= imc < 30:
        return "Sobrepeso", "⚠️"
    else:
        return "Obesidade", "🔴"


# ---- 3. RECURSÃO E VALIDAÇÃO (Garante dados corretos) ----

def obter_dado_positivo(mensagem):
    """
    Usa RECURSÃO para forçar o usuário a digitar um valor válido e positivo.
    Se o valor for inválido, a função chama a si mesma novamente.
    """
    try:
        valor = float(input(mensagem))
        if valor <= 0:
            print("Erro: O valor deve ser maior que zero.")
            return obter_dado_positivo(mensagem) # Chamada recursiva
        return valor
    except ValueError:
        print("Erro: Digite um número válido (use ponto para decimais).")
        return obter_dado_positivo(mensagem) # Chamada recursiva


# ---- 4. PROCESSAMENTO E FLUXO PRINCIPAL ----

def processar_pessoa():
    """Coordena a coleta de dados, cálculo e exibição do resultado."""
    print("\n--- Nova Consulta ---")
    nome = input("Nome do paciente: ")
    p = obter_dado_positivo(f"Digite o peso de {nome} (kg): ")
    a = obter_dado_positivo(f"Digite a altura de {nome} (m): ")

    # Chamada das funções e armazenamento dos resultados
    imc_resultado = calcular_imc(p, a)
    classificacao, emoji = classificar_imc(imc_resultado)

    # Exibição formatada
    print("\n" + "-" * 30)
    print(f" FICHA: {nome.upper()}")
    print(f" IMC  : {imc_resultado:.2f}")
    print(f" STATUS: {classificacao} {emoji}")
    print("-" * 30)


# =========================================================
# RESOLUÇÃO DO EXERCÍCIO: 01b-debug_corrigido.py
# =========================================================

# CORREÇÃO 1: Adicionado 'return' para que a string saia da função e possa ser impressa.
def saudacao(nome, turno="manhã"):
    return f"Bom {turno}, {nome}!"

# CORREÇÃO 2: Adicionado 'return' para devolver o resultado do cálculo matemático.
def dobrar(x):
    return x * 2

# CORREÇÃO 3: Adicionado a palavra-chave 'global' para que a função possa
# alterar a variável 'total' que foi criada fora dela (no escopo global).
total = 0
def incrementar():
    global total
    total = total + 1

# CORREÇÃO 4: Adicionado o CASO BASE (if n < 0) para parar a contagem.
# Sem isso, a função chamaria a si mesma infinitamente até travar o computador.
def contagem(n):
    if n < 0:
        return
    print(f"Contagem: {n}")
    contagem(n - 1)


# =========================================================
# INÍCIO DA EXECUÇÃO DO PROGRAMA
# =========================================================

if __name__ == "__main__":
    exibir_cabecalho()
    
    # Loop de repetição do sistema
    continuar = "s"
    while continuar == "s":
        processar_pessoa()
        continuar = input("\nProcessar outra pessoa? (s/n): ").lower()
    
    exibir_rodape()

    # Demonstração rápida das correções do Debug no console
    print("\n[LOG DE DEBUG CORRIGIDO]")
    print(saudacao("Luiz Carlos"))
    print(f"Teste Dobro (5): {dobrar(5)}")
    incrementar()
    print(f"Variável Global Total: {total}")
    contagem(3)
