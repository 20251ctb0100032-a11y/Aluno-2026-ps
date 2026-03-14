# debug_teste/01b-debug.py
# Versão CORRIGIDA

# CORREÇÃO 1: Removido 'import Temperatura' pois o módulo correto é 'conversores' 
# (Em Python, nomes de módulos são usualmente minúsculos).
from conversores import celsius_para_kelvin, km_para_milhas

# O cálculo agora funciona pois a função foi importada corretamente acima.
resultado = celsius_para_kelvin(25)
print(f"25°C em K: {resultado}")

from utils.formatador import formatar_resultado

# CORREÇÃO 2: Removido o argumento "extra". 
# A função 'formatar_resultado' aceita apenas 5 argumentos (rotulo, valor1, unid1, valor2, unid2).
print(formatar_resultado("teste", 100, "km", 62.1, "mi"))

# CORREÇÃO 3: Ajustado para usar 'km_para_milhas' que foi unificado no primeiro import.
# Antes, o código tentava usar uma função que não havia sido importada naquele bloco.
print(f"50 km = {km_para_milhas(50):.2f} mi")

# CORREÇÃO 4: Removido 'from debug_teste import algo'.
# Esta linha causava erro por tentar importar um módulo inexistente ou criar uma importação circular.
