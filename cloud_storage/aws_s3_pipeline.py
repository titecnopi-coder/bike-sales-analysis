from pathlib import Path
from datetime import datetime
import shutil
import boto3

# ===============================
# AWS S3 Pipeline - Bike Sales
# ===============================

BUCKET_NAME = "bike-sales-analytics-demo"
AWS_REGION = "us-east-2"

SOURCE_FILE = Path("data/sales_data_powerbiVF.csv")

RAW_FOLDER = Path("cloud_storage/raw")
PROCESSED_FOLDER = Path("cloud_storage/processed")

RAW_FOLDER.mkdir(parents=True, exist_ok=True)
PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

raw_file = RAW_FOLDER / f"sales_data_raw_{timestamp}.csv"
processed_file = PROCESSED_FOLDER / f"sales_data_processed_{timestamp}.csv"

# 1. Crear copias locales tipo Data Lake
shutil.copy(SOURCE_FILE, raw_file)
shutil.copy(SOURCE_FILE, processed_file)

print("Archivos preparados localmente:")
print(f"Raw: {raw_file}")
print(f"Processed: {processed_file}")

# 2. Conectar con AWS S3
s3 = boto3.client("s3", region_name=AWS_REGION)

# 3. Subir archivos a S3
s3.upload_file(str(raw_file), BUCKET_NAME, f"raw/{raw_file.name}")
s3.upload_file(str(processed_file), BUCKET_NAME, f"processed/{processed_file.name}")

print("Archivos subidos correctamente a AWS S3.")
print(f"s3://{BUCKET_NAME}/raw/{raw_file.name}")
print(f"s3://{BUCKET_NAME}/processed/{processed_file.name}")