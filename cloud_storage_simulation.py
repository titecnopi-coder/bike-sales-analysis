from pathlib import Path
import shutil
from datetime import datetime

SOURCE_FILE = Path("data/sales_data_powerbi.csv")

RAW_FOLDER = Path("cloud_storage/raw")
PROCESSED_FOLDER = Path("cloud_storage/processed")

RAW_FOLDER.mkdir(parents=True, exist_ok=True)
PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

raw_file = RAW_FOLDER / f"sales_data_raw_{timestamp}.csv"
processed_file = PROCESSED_FOLDER / f"sales_data_processed_{timestamp}.csv"

shutil.copy(SOURCE_FILE, raw_file)
shutil.copy(SOURCE_FILE, processed_file)

print("Simulación de almacenamiento cloud completada.")
print(f"Archivo raw: {raw_file}")
print(f"Archivo processed: {processed_file}")