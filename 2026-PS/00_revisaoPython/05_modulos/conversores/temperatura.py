# No final de conversores/temperatura.py:

if __name__ == "__main__":
    # Este bloco SÓ executa ao rodar temperatura.py diretamente.
    # Ao ser importado por main.py, este bloco é IGNORADO.
    
    print("Testando temperatura.py...")
    print(f"100°C = {celsius_para_fahrenheit(100)}°F  (esperado: 212.0)")
    print(f"0°C   = {celsius_para_kelvin(0)} K        (esperado: 273.15)")
    print("OK!")
