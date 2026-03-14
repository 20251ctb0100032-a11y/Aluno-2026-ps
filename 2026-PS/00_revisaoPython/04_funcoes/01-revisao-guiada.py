# =====================================
# SISTEMA DE BIBLIOTECA
# =====================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções
# Autor      : [Luiz Carlos Oliveira Neto]
# Data       : [03/03/2026]
# Repositorio: https://github.com
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

def calcular_imc_v2(peso, altura):
    """Calcula e retorna o IMC. Fórmula: peso / altura²"""
    imc = peso / (altura ** 2)  # ** é o operador de potência
    return imc                  # devolve o resultado para quem chamou

# Coletando dados do usuário
peso_input   = float(input("Peso (kg): "))
altura_input = float(input("Altura (m): "))

# Chamando a função e armazenando o retorno
resultado = calcular_imc_v2(peso_input, altura_input)
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

def classificar_imc_v2(imc, unidade="kg/m²"):
    """Classifica o IMC e retorna classificação e emoji de status."""
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

# Chamada sem o parâmetro opcional
imc_teste = 22.5
class_res, emoji_res = classificar_imc_v2(imc_teste)
print(f"IMC {imc_teste} ({class_res}) {emoji_res}")

# ---- RECURSÃO BÁSICA ----

def contagem_regressiva(n):
    """Exibe contagem regressiva de n até 0 usando recursão."""
    if n < 0:           # CASO BASE
        return
    
    print(n)
    contagem_regressiva(n - 1)  # CHAMADA RECURSIVA

print("\n--- Contagem regressiva ---")
contagem_regressiva(5)

# Fatorial
def fatorial(n):
    if n == 0 or n == 1:   # CASO BASE
        return 1
    return n * fatorial(n - 1)   # CASO RECURSIVO

print("\n--- Fatorial ---")
for i in range(1, 4):
    print(f"  {i}! = {fatorial(i)}")

# ---- FUNÇÃO PRINCIPAL ----

def processar_pessoa():
    """Coleta dados, calcula IMC e exibe resultado completo."""
    nome   = input("\nNome: ")
    p_proc = float(input("Peso (kg): "))
    a_proc = float(input("Altura (m): "))

    imc = calcular_imc(p_proc, a_proc)
    class_p, emoji_p = classificar_imc_v2(imc)

    print("\n--- Resultado ---")
    print(f"Nome          : {nome}")
    print(f"IMC           : {imc:.2f} kg/m²")
    print(f"Classificação : {class_p} {emoji_p}")

# ---- EXECUÇÃO FINAL ----

exibir_cabecalho()

continuar = "s"
while continuar == "s":
    processar_pessoa()
    continuar = input("\nProcessar outra pessoa? (s/n): ").lower()

# ATENÇÃO: exibir_rodape() dará erro se não estiver definida acima!
# exibir_rodape() 

# Arquivo: 01b-debug_corrigido.py
# (Seus códigos de debug com as correções aplicadas conforme sua mensagem)

def saudacao(nome, turno="manhã"):
    mensagem = f"Bom {turno}, {nome}!"
    return mensagem 

def dobrar(x):
    resultado = x * 2
    return resultado

total = 0
def incrementar():
    global total
    total = total + 1

def contagem(n):
    if n < 0: 
        return
    print(n)
    contagem(n - 1)
