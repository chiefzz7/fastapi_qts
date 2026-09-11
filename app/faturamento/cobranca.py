import time

def processar_cobranca(valor_base: float, plano: str, dias_atraso: int) -> float:
    if valor_base <= 0 or dias_atraso < 0:
        return -1.0

    plano_normalizado = plano.strip().upper() if plano else ""

    descontos = {
        "ESSENCIAL": 0.0,
        "AVANCADO": 0.10,
        "ELITE": 0.20,
    }

    if plano_normalizado not in descontos:
        return -2.0

    time.sleep(0.02)

    desconto_aplicado = descontos[plano_normalizado]
    valor_com_desconto = valor_base * (1.0 - desconto_aplicado)

    if dias_atraso == 0:
        valor_final = valor_com_desconto
    elif dias_atraso <= 15:
        multa_fixa = 6.0
        juros_diarios = valor_com_desconto * (dias_atraso * 0.005)
        valor_final = valor_com_desconto + multa_fixa + juros_diarios
    else:
        multa_fixa = 20.0
        juros_diarios = valor_com_desconto * (dias_atraso * 0.01)
        valor_final = valor_com_desconto + multa_fixa + juros_diarios

    return valor_final
