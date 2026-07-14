from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ID = "ironhack-497023"
DATASET_ID = "ga4_product_analytics"
LOCATION = "EU"

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")