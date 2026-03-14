# =================================================
# SISTEMA DE COMVERSÃO DE UNIDADES
# =================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 07 - Revisão: Módulos
# Autor      : [Luiz Carlos Oliveira Neto]
# Data       : [12/03/2026]
# Repositório: https://github.com/20251ctb0100032-a11y/Aluno-2026-ps.git
#==================================================
from conversores import (
    celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius,
    km_para_milhas, milhas_para_km, metros_para_pes,
)

from utils import cabecalho_secao, formatar_resultado, linha_separadora


def menu_temperatura():
    print(cabecalho_secao("Conversão de Temperatura"))
    valor = float(input("  Valor em °C: "))
    print(formatar_resultado("°C -> °F", valor, "°C", 
celsius_para_fahrenheit(valor), "°F"))
    print(formatar_resultado("°C -> K", valor, "°C", celsius_para_kelvin(valor), 
"K"))

def menu_distancia():
    print(cabecalho_secao("Conversão de Distância"))
    valor = float(input("  Valor em km: "))
    print(formatar_resultado("km -> mi", valor, "km", km_para_milhas(valor), 
"mi"))
    print(formatar_resultado("km -> pés", valor * 1000, "m", metros_para_pes(valor 
* 1000), "pés"))


def main():
    print(linha_separadora())
    print("  SISTEMA DE CONVERSÃO DE UNIDADES")
    print(linha_separadora())

    opcoes = {"1": menu_temperatura, "2": menu_distancia}

    while True:
        print("\n  [1] Temperatura  [2] Distância  [0] Sair")
        escolha = input("  Opção: ").strip()

        if escolha == "0":
            print("\nSistema encerrado.")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("  Opção inválida.")


if __name__ == "__main__":
    main()

# ---- BLOCO 1: STDLIB ----

import math                                 # importa o módulo inteiro
from random import randint, choice          # importa apenas funções específicas
from datetime import datetime               # importa a classe datetime do módulo datetime

print("=== Explorando a Stdlib ===")

print(f"π = {math.pi:.4f}")
print(f"√2 = {math.sqrt(2):.4f}")
print(f"Número aleatório: {randint(1, 100)}")
print(f"Unidade sorteada: {choice(['km', 'milhas', 'metros'])}")
print(f"Agora: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# conversores/temperatura.py

def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    """Converte Celsius para Kelvin."""
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5/9

# Constante do módulo
ZERO_ABSOLUTO_CELSIUS = -273.15

# ---- BLOCO 2: MÓDULO PRÓPRIO ----

from conversores import temperatura    # importa o módulo do pacote


print("\n=== Conversão de Temperatura ===")
valor = 100.0
print(f"{valor}°C = {temperatura.celsius_para_fahrenheit(valor):.1f}°F")
print(f"{valor}°C = {temperatura.celsius_para_kelvin(valor):.2f} K")
print(f"Zero absoluto: {temperatura.ZERO_ABSOLUTO_CELSIUS}°C")

# conversores/distancia.py

def km_para_milhas(km):
    """Converte quilômetros para milhas."""
    return km * 0.621371

def milhas_para_km(milhas):
    """Converte milhas para quilômetros."""
    return milhas / 0.621371

def metros_para_pes(metros):
    """Converte metros para pés."""
    return metros * 3.28084

# ---- BLOCO 4: CAMADAS ----

from utils import cabecalho_secao, formatar_resultado


print(cabecalho_secao("Conversões de Distância"))
print(formatar_resultado("km->mi", 100, "km", km_para_milhas(100), "mi"))
print(formatar_resultado("mi->km", 62, "mi", milhas_para_km(62),   "km"))


print(cabecalho_secao("Conversões de Temperatura"))
print(formatar_resultado("°C->°F", 100, "°C", celsius_para_fahrenheit(100), "°F"))
print(formatar_resultado("°C->K",  100, "°C", celsius_para_kelvin(100),     "K"))
