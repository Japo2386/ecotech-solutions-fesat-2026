from django.shortcuts import render

from .emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    """Procesa las métricas y las envía al panel web."""
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1200},
        {"planta": "Planta Sur", "consumo_kwh": 950},
        {"planta": "Planta Central", "consumo_kwh": 1800},
    ]

    contexto = obtener_metricas_consumo(registros)
    contexto["registros"] = registros

    return render(
        request,
        "sustentabilidad/panel.html",
        contexto,
    )
