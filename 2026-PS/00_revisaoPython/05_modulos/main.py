# =================================================
# SISTEMA DE COMVERSÃO DE UNIDADES
# =================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 07 - Revisão: Módulos
# Autor      : [Luiz Carlos Oliveira Neto]
# Data       : [12/03/2026]
# Repositório: https://github.com/20251ctb0100032-a11y/Aluno-2026-ps.git
#==================================================

# ---- BLOCO 1: STDLIB ----

import math               # importa o módulo
from random import randint, choice  # importa apenas funções especificas
from datetime import datetime # importa a classe datetime do módulo datetime

print("=== Explorando a Stdlib ===")
print(f"n = {math.pi:.4f}")
print(f"V2 = {math.sqrt (2) :.4f}")
print(f"Número aleatório: {randint(1, 100)}")
print(f"Unidade sorteada: {choice(["km", "milhas", "metros"])}")
print(f"Agora: {datetime.now() .strftime('%d/%m/%Y %H:%M')}")

# conversores/temperatura.py

def celsius_para_fahrenheit(celsius) :
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius) :
    """Converte Celsius para Kelvin."""
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit) :
    """Converte Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9

# Constante do módulo
ZERO_ABSOLUTO_CELSIUS = -273.15

# ---- BLOCO 2: MÓDULO PRÓPRIO ----

from conversores import temperatura # importa o módulo do pacote

print ("\n=== Conversão de Temperatura ===")
valor = 100.0
print (f"{valor}  C = {temperatura.celsius_para_fahrenheit(valor):.1f} F")
print (f"{valor}  C = {temperatura.celsius_para_kelvin(valor):.2f} K")
print (f"Zero absoluto: {temperatura.ZERO_ABSOLUTO_CELSIUS} C")

# conversores/distancia.py

def km_para_milhas(km) :
    """Converte quilômetros para milhas."""
    return km * 0.621371

def milhas_para_km(milhas):
    """Converte milhas para quilômetros."""
    return milhas / 0.621371

def metros_para_pes(metros):
    """Converte metros para pés."""
    return metros * 3.28084

# conversores/_init_.py
# Expôe a API pública do pacote.