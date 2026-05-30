# 🚴 Bike Sales Analytics Platform

## Descripción

Proyecto de analítica de datos enfocado en ventas de bicicletas. El objetivo fue construir una solución completa de análisis utilizando Python, PostgreSQL, SQL y Power BI.

El proyecto incluye procesos de limpieza, transformación, carga de datos, consultas SQL analíticas y visualización de KPIs en un dashboard interactivo.

---

## Arquitectura del proyecto

```text
CSV / Datos fuente
        ↓
Python + Pandas
        ↓
PostgreSQL
        ↓
Power BI
```

---

## Tecnologías utilizadas

* Python
* Pandas
* SQLAlchemy
* PostgreSQL
* SQL
* Power BI
* Git / GitHub

---

## Proceso realizado

* Limpieza y transformación de datos con Python y Pandas.
* Carga de datos en PostgreSQL mediante ETL.
* Desarrollo de consultas SQL analíticas.
* Creación de dashboard interactivo en Power BI.

---

## KPIs principales

* Ventas Totales
* Órdenes Totales
* Productos Vendidos
* Ventas por Categoría
* Top 10 Productos Más Vendidos
* Ventas por Tienda

---

## Dashboard Preview

![Dashboard Preview](dashboard_preview.png)

---

## Habilidades demostradas

* Limpieza y transformación de datos
* Procesos ETL con Python
* Carga de datos en PostgreSQL
* Consultas SQL analíticas
* Visualización de datos en Power BI
* Documentación técnica de proyecto

## Databricks / Spark

Se realizó una práctica en Databricks usando Spark para cargar el dataset de ventas, revisar el esquema, transformar columnas numéricas y generar agregaciones analíticas.

Flujo realizado:

CSV
↓
Databricks Notebook
↓
Spark DataFrame
↓
Limpieza de tipos de datos
↓
Agregaciones por categoría y producto
↓
Tabla analítica en Databricks

### Actividades realizadas

- Carga de CSV usando Spark DataFrames.
- Validación de esquema y tipos de datos.
- Limpieza y transformación de columnas numéricas.
- Agregaciones analíticas por categoría y producto.
- Persistencia de tabla analítica en Databricks.

### Tecnologías

- Databricks
- Apache Spark
- PySpark


## Multicloud Data Pipeline - Bike Sales Analytics

Este proyecto demuestra un pipeline de datos completo desde la simulación local hasta la nube real, integrando diferentes herramientas y plataformas:

### Flujo de datos
1. CSV local → Carpeta raw/processed (simulación de Data Lake)
2. Spark / Databricks:
   - Lectura de CSV
   - Limpieza de columnas numéricas
   - Agregaciones: ventas por categoría y top productos
   - Guardado como tabla analítica en Databricks
3. AWS S3:
   - Subida de archivos raw y processed
   - Simulación de almacenamiento cloud real
4. Power BI:
   - Conexión a CSV limpio o tabla Databricks
   - Dashboard interactivo de ventas y KPIs

### Tecnologías utilizadas
- Python, Pandas, PySpark
- PostgreSQL
- Databricks / Spark
- AWS S3
- Power BI
- Git / GitHub



## Cloud & Multicloud

El proyecto evolucionó desde una simulación local de almacenamiento tipo Data Lake (`raw/processed`) hacia integración con servicios cloud reales.

Se implementó almacenamiento en AWS S3 para carga automática de archivos mediante Python y boto3, junto con procesamiento distribuido usando Spark y Databricks.

Adicionalmente, se exploraron conceptos de arquitectura multicloud utilizando Azure y AWS como referencia para pipelines modernos de datos y analítica.
