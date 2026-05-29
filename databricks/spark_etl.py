# =====================================================
# Bike Sales Analytics - Databricks / Spark ETL
# =====================================================

# 1. Leer archivo CSV desde Databricks Workspace
df = spark.read.csv(
    "file:/Workspace/Users/titecnopi@gmail.com/Drafts/sales_data_powerbi.csv",
    header=True,
    inferSchema=True,
    sep=";"
)

display(df)

# 2. Revisar estructura y tipos de datos
df.printSchema()

# 3. Importar funciones de Spark
from pyspark.sql.functions import regexp_replace, col, sum as spark_sum

# 4. Limpieza y transformación
# total_price viene como texto, por eso se cambia coma por punto y se convierte a número decimal
df_clean = df.withColumn(
    "total_price_numeric",
    regexp_replace(col("total_price"), ",", ".").cast("double")
)

# 5. Ventas totales por categoría
ventas_categoria = (
    df_clean.groupBy("category_name")
            .agg(spark_sum("total_price_numeric").alias("ventas_totales"))
            .orderBy(col("ventas_totales").desc())
)

display(ventas_categoria)

# 6. Top 10 productos más vendidos
top_productos = (
    df.groupBy("product_name")
      .agg(spark_sum("quantity").alias("unidades_vendidas"))
      .orderBy(col("unidades_vendidas").desc())
      .limit(10)
)

display(top_productos)

# 7. Guardar resultado como tabla administrada en Databricks
ventas_categoria.write.mode("overwrite").saveAsTable("ventas_por_categoria")



print("Proceso ETL en Databricks finalizado correctamente.")