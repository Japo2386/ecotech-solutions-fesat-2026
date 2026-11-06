# EcoTech Solutions — Evaluación Técnica de Desarrollo

**Trabajo Final Integrador | FESAT 2026**

## Descripción del proyecto

Desarrollo de una solución modular en Python para EcoTech Solutions, orientada al procesamiento de datos de sensores, la gestión de inventarios de productos sustentables y el monitoreo de emisiones de carbono.

El proyecto aplica buenas prácticas de programación, Programación Orientada a Objetos (POO), persistencia de datos, pruebas automatizadas e integración web con Django.

## Tecnologías utilizadas

- Python
- Django
- pytest y pytest-django
- JSON
- HTML y CSS
- Git y GitHub

## Estructura del proyecto

```text
ECOTECH SOLUTIONS/
├── ejercicio_1_sensores/
│   └── ejercicio_1_sensores.py
│
├── ejercicio_2_productos/
│   ├── ejercicio_2_productos.py
│   └── catalogo_ecotech.json
│
├── ejercicio_3_auditoria_web/
│   ├── config/
│   ├── sustentabilidad/
│   │   ├── emisiones.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── tests/
│   │   │   └── test_emisiones.py
│   │   └── templates/
│   │       └── sustentabilidad/
│   │           └── panel.html
│   ├── manage.py
│   ├── pytest.ini
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

## Ejercicio 1 — Sanitización y análisis estadístico de sensores

Implementa funciones para normalizar registros de sensores térmicos y generar reportes estadísticos.

**Funcionalidades principales:**
- Limpieza de identificadores.
- Conversión de temperaturas a valores numéricos.
- Tratamiento de registros incompletos o inválidos.
- Cálculo del promedio térmico.
- Identificación de sensores que superan un umbral de temperatura.

**Ejecución desde la carpeta principal:**

```bash
python ejercicio_1_sensores/ejercicio_1_sensores.py
```

## Ejercicio 2 — Modelo de productos, excepciones y persistencia

Implementa un catálogo de dispositivos ecológicos mediante Programación Orientada a Objetos.

**Conceptos aplicados:**
- Encapsulamiento mediante propiedades.
- Herencia y polimorfismo.
- Excepciones personalizadas.
- Validación de stock.
- Serialización y persistencia en JSON.

Los productos válidos se exportan al archivo `catalogo_ecotech.json`.

**Ejecución:**

```bash
python ejercicio_2_productos/ejercicio_2_productos.py
```

## Ejercicio 3 — Auditoría e integración web

Implementa un algoritmo de cálculo de emisiones de carbono y su integración en un panel de monitoreo desarrollado con Django.

**Funcionalidades principales:**
- Cálculo de emisiones a partir del consumo energético.
- Validación de consumos negativos.
- Identificación de la planta industrial de mayor consumo.
- Procesamiento de métricas globales.
- Visualización de resultados mediante una plantilla HTML.
- Pruebas automatizadas con pytest.

### Instalación

Desde la carpeta `ejercicio_3_auditoria_web`, crear un entorno virtual:

```bash
python -m venv .venv
```

En Windows, instalar las dependencias:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Ejecutar las pruebas

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

La auditoría incluye nueve pruebas automatizadas que verifican los cálculos de emisiones, las validaciones, el procesamiento de registros y la respuesta de la vista Django.

**Resultado verificado durante el desarrollo: 9 pruebas aprobadas.**

### Ejecutar el servidor Django

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Acceder desde el navegador a:

http://127.0.0.1:8000/sustentabilidad/

## Datos de prueba

Los registros utilizados son simulados y representan situaciones habituales del entorno industrial. Permiten demostrar el funcionamiento de los algoritmos sin depender de sensores físicos ni de servicios externos.

## Conclusión

El proyecto integra procesamiento y validación de datos, diseño orientado a objetos, persistencia, pruebas automatizadas y desarrollo web.

Su organización modular permite ejecutar y evaluar los tres ejercicios de manera independiente.

---

**EcoTech Solutions | Trabajo Final Integrador FESAT 2026**