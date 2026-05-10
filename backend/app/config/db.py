import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():

    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        f'SERVER={os.getenv("DB_SERVER")};'
        f'DATABASE={os.getenv("DB_DATABASE")};'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
    
    return connection