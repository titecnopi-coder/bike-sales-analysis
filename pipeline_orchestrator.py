import subprocess

print("🚀 Iniciando pipeline de datos...\n")

# Simulación cloud
print("☁️ Ejecutando cloud storage simulation...")
subprocess.run(["python", "cloud_storage_simulation.py"])

# Carga PostgreSQL
print("\n🐘 Cargando datos a PostgreSQL...")
subprocess.run(["python", "load_to_postgres.py"])

print("\n✅ Pipeline completado correctamente.")