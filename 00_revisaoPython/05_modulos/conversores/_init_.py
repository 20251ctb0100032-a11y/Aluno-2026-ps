# conversores/__init__.py
# Expõe a API pública do pacote.

from .temperatura import celsius_para_fahrenheit, celsius_para_kelvin, \
fahrenheit_para_celsius
from .distancia   import km_para_milhas, milhas_para_km, metros_para_pes

# O "." antes do nome = importação relativa (módulo dentro DESTE pacote)

__all__ = [
    "celsius_para_fahrenheit", "celsius_para_kelvin", "fahrenheit_para_celsius",
    "km_para_milhas", "milhas_para_km", "metros_para_pes",
]

# ---- BLOCO 3: API LIMPA DO PACOTE ----

from conversores import km_para_milhas, celsius_para_fahrenheit
# Funciona porque __init__.py já expôs essas funções


print("\n=== API Limpa ===")
print(f"100 km = {km_para_milhas(100):.2f} milhas")
print(f"25°C   = {celsius_para_fahrenheit(25):.1f}°F")

