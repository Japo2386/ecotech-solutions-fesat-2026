
import pytest

from sustentabilidad.emisiones import (
    calcular_emisiones_carbono,
    obtener_metricas_consumo,
)


def test_consumo_nominal():
    resultado = calcular_emisiones_carbono(100)
    assert resultado == pytest.approx(40.0)


def test_factor_personalizado():
    resultado = calcular_emisiones_carbono(200, 0.5)
    assert resultado == pytest.approx(100.0)


def test_consumo_cero():
    resultado = calcular_emisiones_carbono(0)
    assert resultado == pytest.approx(0.0)


def test_consumo_decimal():
    resultado = calcular_emisiones_carbono(125.5)
    assert resultado == pytest.approx(50.2)


def test_consumo_negativo():
    with pytest.raises(ValueError):
        calcular_emisiones_carbono(-10)


def test_metricas_consumo():
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1200},
        {"planta": "Planta Sur", "consumo_kwh": 950},
        {"planta": "Planta Central", "consumo_kwh": 1800},
    ]

    resultado = obtener_metricas_consumo(registros)

    assert resultado["total_emisiones"] == pytest.approx(1580.0)
    assert resultado["planta_mayor_consumo"] == "Planta Central"


def test_registros_vacios():
    resultado = obtener_metricas_consumo([])

    assert resultado["total_emisiones"] == 0.0
    assert resultado["planta_mayor_consumo"] is None


def test_metricas_consumo_negativo():
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": -100}
    ]

    with pytest.raises(ValueError):
        obtener_metricas_consumo(registros)

def test_vista_panel_sustentabilidad(client):
    respuesta = client.get("/sustentabilidad/")

    assert respuesta.status_code == 200
    assert respuesta.context["total_emisiones"] == pytest.approx(1580.0)
    assert respuesta.context["planta_mayor_consumo"] == "Planta Central"
    assert b"EcoTech Solutions" in respuesta.content