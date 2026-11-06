

def limpiar_registro_sensor(registro_raw):

    registro_limpio = {}

    sensor_id = registro_raw.get("sensor_id", "")
    
    registro_limpio["sensor_id"] = str(sensor_id or "").strip()

    temperatura = registro_raw.get("temperatura", 0.0)

    if isinstance(temperatura, (int, float)):
        registro_limpio["temperatura"] = float(temperatura)
    else:
        try:
            temperatura_texto = str(temperatura).upper()

            temperatura_texto = (
                temperatura_texto
                .replace("C", "")
                .replace("F", "")
                .replace("°", "")
                .strip()
            )

            registro_limpio["temperatura"] = float(temperatura_texto)

        except ValueError:
            
            registro_limpio["temperatura"] = 0.0

    
    ubicacion = registro_raw.get("ubicacion", "")

    if isinstance(ubicacion, str) and ubicacion.strip():
        registro_limpio["ubicacion"] = ubicacion.strip()
    else:
        registro_limpio["ubicacion"] = "Área No Asignada"

    return registro_limpio


def generar_resumen_sensores(
    lista_sensores_limpios, umbral_temperatura
):
    
    if not lista_sensores_limpios:
        return ([], 0.0)

    sumatoria_termica = 0.0
    lista_sensores_alerta = []

    
    for sensor in lista_sensores_limpios:
        temperatura = sensor["temperatura"]
        sumatoria_termica += temperatura

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    
    cantidad_sensores = len(lista_sensores_limpios)

    promedio_temperatura = round(
        sumatoria_termica / cantidad_sensores, 2
    )

    return (lista_sensores_alerta, promedio_temperatura)


def main():
    
    datos_crudos_planta = [
        {
            "sensor_id": "  SENSOR-001  ",
            "temperatura": "24.5C",
            "ubicacion": "Planta Norte",
        },
        {
            "sensor_id": "SENSOR-002",
            "temperatura": "31.2°C",
            "ubicacion": "  Planta Sur  ",
        },
        {
            "sensor_id": " SENSOR-003 ",
            "temperatura": 19.8,
            "ubicacion": "",
        },
        {
            "sensor_id": "SENSOR-004",
            "temperatura": "42.0°C",
            "ubicacion": "Reactor Central",
        },
        {
            "sensor_id": "SENSOR-005 ",
            "temperatura": "TXT_CORRUPTO",
            "ubicacion": "Almacén",
        },
    ]

    umbral_alerta = 30.0

    print("=" * 60)
    print("         ECOTECH SOLUTIONS - MONITOREO TÉRMICO")
    print("=" * 60)

    
    sensores_limpios = []

    for registro in datos_crudos_planta:
        sensor_limpio = limpiar_registro_sensor(registro)
        sensores_limpios.append(sensor_limpio)

    print("\nREGISTROS NORMALIZADOS")
    print("-" * 60)

    for sensor in sensores_limpios:
        print(f"Sensor: {sensor['sensor_id']}")
        print(f"Temperatura: {sensor['temperatura']:.2f} °C")
        print(f"Ubicación: {sensor['ubicacion']}")
        print("-" * 60)

    
    sensores_alerta, promedio = generar_resumen_sensores(
        sensores_limpios, umbral_alerta
    )

    print("\nREPORTE ESTADÍSTICO")
    print("-" * 60)
    print(f"Sensores procesados: {len(sensores_limpios)}")
    print(f"Umbral de alerta: {umbral_alerta:.2f} °C")
    print(f"Temperatura promedio: {promedio:.2f} °C")
    print(f"Cantidad de alertas: {len(sensores_alerta)}")

    print("\nSENSORES EN ALERTA:")

    if sensores_alerta:
        for sensor_id in sensores_alerta:
            print(f"  - {sensor_id}")
    else:
        print("  No se detectaron sensores en alerta.")

    print("\n" + "=" * 60)
    print("              FIN DEL REPORTE")
    print("=" * 60)


if __name__ == "__main__":
    main()
