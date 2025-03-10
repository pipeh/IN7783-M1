import re

def validar_rut(rut):
    """Valida un RUT chileno en formato 'xxxxxxxx-y'"""
    match = re.match(r"^(\d{7,8})-([0-9Kk])$", rut)
    if not match:
        return False
    cuerpo, digito_verificador = match.groups()
    cuerpo = list(map(int, reversed(cuerpo)))
    factores = [2, 3, 4, 5, 6, 7] * 2  # Se repiten los factores según corresponda
    suma = sum(c * f for c, f in zip(cuerpo, factores))
    resto = 11 - (suma % 11)
    esperado = 'K' if resto == 10 else '0' if resto == 11 else str(resto)
    return esperado == digito_verificador.upper()