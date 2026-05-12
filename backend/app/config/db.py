import pyodbc

#---------------db.py---------------#
#Conección a la base de datos.

def get_connection():

    server = 'Z'
    database = 'GestionDocumental'
    driver = '{ODBC Driver 18 for SQL Server}'

    connection = pyodbc.connect(
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'TrustServerCertificate=yes;'
        f'Trusted_Connection=yes;'
    )
    
    return connection