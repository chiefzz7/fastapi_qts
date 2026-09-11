import pytest
import time

from app.faturamento.cobranca import processar_cobranca


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, retorno_esperado",
    [
        (-1, "ESSENCIAL", 3, -1.0),
        (0, "ELITE", 10, -1.0),
        (200, "AVANCADO", -2, -1.0),
        (190, "MEGA", 2, -2.0),
        (290, "", 0, -2.0),
        (300, "essencial ", 0, 300),
        (560, "  AVANCADO ", 0, 560 * (1.0 - 0.10)),
        (980, "ELITE", 0, 980 * (1.0 - 0.20)),
        (210, "AVANCADO", 1, (210 * (1.0 - 0.10)) + 6.0 + (210 * (1.0 - 0.10) * (1 * 0.005))),
        (132, "ELITE", 15, (132 * (1.0 - 0.20)) + 6.0 + (132 * (1.0 - 0.20) * (15 * 0.005))),
        (100, "ESSENCIAL", 16, 100 + 20.0 + 100 * 16 * 0.01),
        (544, "AVANCADO", 20, (544 * (1.0 - 0.10)) + 20.0 + (544 * (1.0 - 0.10) * (20 * 0.01))),
    ],
)
def test_processar_cobranca_funcional(valor_base, plano, dias_atraso, retorno_esperado):
    assert processar_cobranca(valor_base, plano, dias_atraso) == retorno_esperado

