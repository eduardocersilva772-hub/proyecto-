# convertidor.py
# Avance inicial del Conversor de Divisas

def convertir_divisa(monto, tasa_cambio):
    return monto * tasa_cambio

if __name__ == "__main__":
    print("=== CONVERSOR DE DIVISAS ===")
    
    # Simulación de tasa USD a MXN
    tasa_usd_mxn = 20.0
    monto_usd = 10.0
    
    resultado = convertir_divisa(monto_usd, tasa_usd_mxn)
    print(f"{monto_usd} USD equivalen a {resultado} MXN (Tasa: {tasa_usd_mxn})")