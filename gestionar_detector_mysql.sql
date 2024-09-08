import mysql.connector

# Configuración de la conexión
config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': '127.0.0.1',
    'database': 'tu_base_de_datos'
}

# Conectar a la base de datos
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Crear la tabla (si aún no existe)
cursor.execute('''
CREATE TABLE IF NOT EXISTS detector_de_radiacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    activo BOOLEAN NOT NULL,
    nivel_radiacion FLOAT
)
''')

# Insertar un nuevo registro
cursor.execute('''
INSERT INTO detector_de_radiacion (activo, nivel_radiacion)
VALUES (%s, %s)
''', (True, 23.45))
conn.commit()

# Seleccionar todos los registros
cursor.execute('SELECT * FROM detector_de_radiacion')
registros = cursor.fetchall()
for registro in registros:
    print(registro)

# Cerrar la conexión
cursor.close()
conn.close()


config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': '127.0.0.1',
    'database': 'tu_base_de_datos'
}
