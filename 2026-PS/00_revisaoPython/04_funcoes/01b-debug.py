# =====================================
# SISTEMA DE CÁLCULO DE IMC (CORRIGIDO)
# =====================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções
# Autor      : [Luiz Carlos Oliveira Neto]
# Data       : [03/03/2026]
# Repositorio: https://github.com/20251ctb0100032-a11y/Aluno-2026-ps.git
# =====================================

# ---- FUNÇÕES DE INTERFACE ----

def exibir_cabecalho():
    """Exibe o cabeçalho do sistema."""
    print("\n" + "=" * 40)
    print("      SISTEMA DE CÁLCULO DE IMC")
    print("=" * 40)

def exibir_rodape():
    """Exibe a mensagem de encerramento (Corrigido: estava faltando a definição)."""
    print("\n" + "=" * 40)
    print("   SISTEMA ENCERRADO COM SUCESSO")
    print("=" * 40)

# ---- FUNÇÕES DE CÁLCULO E LÓGICA ----

def calcular_imc(peso, altura):
    """Calcula o IMC. Fórmula: peso / altura²"""
    return peso / (altura ** 2)

def classificar_imc(imc, unidade="kg/m²"):
    """Classifica o IMC e retorna a categoria e um emoji."""
    if imc < 18.5:
        return "Abaixo do peso", "⬇️"
    elif 18.5 <= imc < 25:
        return "Peso normal", "✅"
    elif 25 <= imc < 30:
        return "Sobrepeso", "⚠️"
    else:
        return "Obesidade", "🔴"

# ---- FUNÇÃO RECURSIVA PARA VALIDAÇÃO ----

def obter_dado_positivo(mensagem):
    """Garante que o usuário digite um valor numérico e positivo."""
    try:
        valor = float(input(mensagem))
        if valor <= 0:
            print("Erro: O valor deve ser maior que zero.")
            return obter_dado_positivo(mensagem) # Recursão
        return valor
    except ValueError:
        print("Erro: Digite um número válido.")
        return obter_dado_positivo(mensagem) # Recursão

# ---- PROCESSAMENTO PRINCIPAL ----

def processar_pessoa():
    """Executa o fluxo completo para uma pessoa."""
    nome = input("\nNome: ")
    p = obter_dado_positivo(f"Peso de {nome} (kg): ")
    a = obter_dado_positivo(f"Altura de {nome} (m): ")

    imc = calcular_imc(p, a)
    classificacao, emoji = classificar_imc(imc)

    print("\n" + "-" * 30)
    print(f" RESULTADO PARA: {nome.upper()}")
    print(f" IMC           : {imc:.2f}")
    print(f" Classificação : {classificacao} {emoji}")
    print("-" * 30)

# =========================================================
# RESOLUÇÃO DO ARQUIVO: 01b-debug_corrigido.py
# =========================================================
# Aqui estão as correções dos 4 erros de lógica e escopo:

# 1. ERRO DE RETORNO: Adicionado 'return' para a função devolver o valor.
def saudacao(nome, turno="manhã"):
    return f"Bom {turno}, {nome}!"

# 2. ERRO DE RETORNO: Adicionado 'return' para o resultado ser usado fora da função.
def dobrar(x):
    return x * 2

# 3. ERRO DE ESCOPO: Usado 'global' para modificar a variável fora da função.
total = 0
def incrementar():
    global total
    total += 1

# 4. ERRO DE RECURSÃO: Adicionado 'Caso Base' (if n < 0) para evitar loop infinito.
def contagem(n):
    if n < 0:
        return
    print(f"Contando: {n}")
    contagem(n - 1)

# =====================================
# EXECUÇÃO DO PROGRAMA
# =====================================

if __name__ == "__main__":
    exibir_cabecalho()
    
    continuar = "s"
    while continuar == "s":
        processar_pessoa()
        continuar = input("\nProcessar outra pessoa? (s/n): ").lower()
    
    exibir_rodape()

    # Demonstrando as funções do Debug
    print("\n--- Teste das Funções Corrigidas (Debug) ---")
    print(saudacao("Luiz"))
    print(f"Dobro de 10: {dobrar(10)}")
    incrementar()
    print(f"Total incrementado: {total}")
    contagem(3)
