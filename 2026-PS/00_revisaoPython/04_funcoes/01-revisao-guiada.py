# =====================================
# SISTEMA DE BIBLIOTECA
# =====================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções
# Autor      : [Luiz Carlos Oliveira Neto]
# Data       : [03/03/2026]
# Repositorio: https://github.com/20251ctb0100032-a11y/Aluno-2026-ps.git
# =====================================
#
# DESCRIÇÃO:
# Calcula e classifica o IMC de uma pessoa.
# Demonstra definição de funções, parametros,
# retorno, espaço e recursão.
# ---- FUNÇÃO SEM PARÂMETROS E SEM RETORNO ----
def exibir_cabecalho():
    """Exibe o cabeçalho do sistema no terminal."""
    print("=" * 40)
    print("      SISTEMA DE CÁLCULO DE IMC")
    print("=" * 40)

# --- FUNÇÃO COM PARÂMETROS E RETORNO (Cálculo) ---
def calcular_imc(peso, altura):
    """Calcula o IMC baseado no peso e altura."""
    imc = peso / (altura ** 2)
    return imc

# --- FUNÇÃO COM PARÂMETROS E RETORNO (Classificação) ---
def classificar_imc(imc):
    """Classifica o IMC de acordo com a tabela da OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# --- EXEMPLO DE RECURSÃO (Validação de entrada) ---
def obter_dado_positivo(mensagem):
    """Usa recursão para garantir que o usuário digite um valor positivo."""
    try:
        valor = float(input(mensagem))
        if valor <= 0:
            print("Erro: O valor deve ser maior que zero.")
            return obter_dado_positivo(mensagem) # Chamada recursiva
        return valor
    except ValueError:
        print("Erro: Digite um número válido.")
        return obter_dado_positivo(mensagem) # Chamada recursiva

# --- EXECUÇÃO PRINCIPAL (Escopo e fluxo) ---
exibir_cabecalho()

# Escopo Local: As variáveis abaixo pertencem ao fluxo principal
p = obter_dado_positivo("Digite seu peso (kg): ")
a = obter_dado_positivo("Digite sua altura (m): ")

resultado_imc = calcular_imc(p, a)
classificacao = classificar_imc(resultado_imc)

print("\n" + "-" * 20)
print(f"Seu IMC é: {resultado_imc:.2f}")
print(f"Classificação: {classificacao}")
print("-" * 20)
# ---- FUNÇÃO COM PARÂMETROS E RETORNO ----

def calcular_imc(peso, altura):
    """Calcula e retorna o IMC. Fórmula: peso / altura²"""
    imc = peso / (altura ** 2)  # ** é o operador de potência
    return imc                  # devolve o resultado para quem chamou

# Coletando dados do usuário
peso   = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

# Chamando a função e armazenando o retorno
resultado = calcular_imc(peso, altura)
print(f"Seu IMC é: {resultado:.2f}")
# ---- ESCOPO LOCAL vs. GLOBAL ----

versao = "1.0"  # variável GLOBAL - existe fora de qualquer função

def demonstrar_escopo():
    mensagem = "Olá do interior da função"  # variável LOCAL
    print("Dentro da função:")
    print(f"  mensagem = {mensagem}")       # OK: local existe aqui
    print(f"  versao   = {versao}")         # OK: global é visível dentro

demonstrar_escopo()

print("\nFora da função:")
print(f"  versao   = {versao}")             # OK: global existe aqui
# print(mensagem)                         # ERRO: local não existe aqui!
# ---- VALOR PADRÃO E MÚLTIPLOS RETORNOS ----

def classificar_imc(imc, unidade="kg/m²"):
    """Classifica o IMC e retorna classificação e emoji de status.
    Parâmetro 'unidade' tem valor padrão - não é obrigatório informar."""

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        emoji = "⬇️"
    elif imc < 25.0:
        classificacao = "Peso normal"
        emoji = "✅"
    elif imc < 30.0:
        classificacao = "Sobrepeso"
        emoji = "⚠️"
    else:
        classificacao = "Obesidade"
        emoji = "🔴"

    return classificacao, emoji  # retorna dois valores - Python empacota como tupla

# Chamada sem o parâmetro opcional (usa o padrão "kg/m²")
imc_teste = 22.5
classificacao, emoji = classificar_imc(imc_teste)
print(f"IMC {imc_teste} ({classificacao}) {emoji}")

# Chamada informando o parâmetro opcional
classificacao, emoji = classificar_imc(imc_teste, unidade="lb/in²")
print(f"Mesma chamada com unidade customizada: {classificacao} {emoji}")
# ---- RECURSÃO BÁSICA ----

def contagem_regressiva(n):
    """Exibe contagem regressiva de n até 0 usando recursão."""
    if n < 0:           # CASO BASE: para a recursão
        return
    
    print(n)
    contagem_regressiva(n - 1)  # CHAMADA RECURSIVA: resolve problema menor

print("\n--- Contagem regressiva ---")
contagem_regressiva(5)


# Fatorial: exemplo clássico de recursão com retorno
def fatorial(n):
    """Calcula n! recursivamente. Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120"""
    if n == 0 or n == 1:   # CASO BASE
        return 1
    
    return n * fatorial(n - 1)   # CASO RECURSIVO

print("\n--- Fatorial ---")
for i in range(1, 7):
    print(f"  {i}! = {fatorial(i)}")
# ---- FUNÇÃO PRINCIPAL ----

def processar_pessoa():
    """Coleta dados, calcula IMC e exibe resultado completo."""
    nome   = input("\nNome: ")
    peso   = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    # Reutiliza funções já definidas anteriormente
    imc = calcular_imc(peso, altura)
    classificacao, emoji = classificar_imc(imc)

    print("\n--- Resultado ---")
    print(f"Nome          : {nome}")
    print(f"IMC           : {imc:.2f} kg/m²")
    print(f"Classificação : {classificacao} {emoji}")

# ---- EXECUÇÃO PRINCIPAL ----

exibir_cabecalho()

continuar = "s"
while continuar == "s":
    processar_pessoa()
    # O input precisa estar alinhado com o processar_pessoa()
    continuar = input("\nProcessar outra pessoa? (s/n): ").lower()
        
exibir_rodape()
# Arquivo: 01b-debug_corrigido.py
# CORREÇÃO: Os 4 erros foram resolvidos abaixo!
 
# 1. Adicionado 'return' para devolver a string
def saudacao(nome, turno="manhã"):
    mensagem = f"Bom {turno}, {nome}!"
    return mensagem 

print(saudacao("Ana"))
print(saudacao("Bruno", "tarde"))

# 2. Adicionado 'return' para devolver o cálculo
def dobrar(x):
    resultado = x * 2
    return resultado

print("Dobro de 5:", dobrar(5))

# 3. Adicionado 'global' para acessar a variável externa
total = 0
def incrementar():
    global total
    total = total + 1

incrementar()
print("Total:", total)

# 4. Adicionado 'Caso Base' para parar a recursão no zero
def contagem(n):
    if n < 0: # Condição de parada
        return
    print(n)
    contagem(n - 1)

contagem(3)
