import pyodbc

# Configur as informações de conexão
server = "nome do servidor"
database = "nome do banco de dados"
username = "nome de usuario"
password = "senha"

# Estabelecer a conexão
credencials = pyodbc.connect(
    "DRIVER={SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database}"
    f"UID={username}"
    f"PWD={password}"
)

conn = pyodbc.connect(credencials)
print("Conexão Bem Sucedida")

cursor = conn.cursor()
comando = "SELECT * FROM TABELA"
cursor.execute(comando)
cursor.commit()