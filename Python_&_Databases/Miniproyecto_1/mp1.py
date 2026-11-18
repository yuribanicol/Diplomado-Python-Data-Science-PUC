import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql123",
    database="mp1"
)

cursor = conexion.cursor()

# Consulta 5a: Filtrar por RUT 77886308-1
print("Consulta 5a:")
query_a = "SELECT * FROM sociedades WHERE rut = '77886308-1'"
cursor.execute(query_a)
resultado_a = cursor.fetchall()
for fila in resultado_a:
    print(fila)

# Consulta 5b: Sociedades que empiezan con 'Agencia'
print("\nConsulta 5b:")
query_b = "SELECT * FROM sociedades WHERE nombre LIKE 'Agencia%'"
cursor.execute(query_b)
resultado_b = cursor.fetchall()
for fila in resultado_b:
    print(fila)
print("Total sociedades encontradas:", len(resultado_b))

# Consulta 5c: Sociedades con capital mayor o igual a 400.000.000
print("\nConsulta 5c:")
query_c = "SELECT * FROM sociedades WHERE capital >= 400000000"
cursor.execute(query_c)
resultado_c = cursor.fetchall()
for fila in resultado_c:
    print(fila)
print("Total sociedades encontradas:", len(resultado_c))

# Inserción 6: Agregar nueva sociedad
print("\nInserción 6:")
query_insert = """
    INSERT IGNORE INTO sociedades (id, rut, nombre, registro, comuna, capital)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
datos_nueva_sociedad = (
    5156305,
    '77721389-K',
    'Estrellas SpA',
    '2024-03-11 00:00:00',
    'PROVIDENCIA',
    1000000
)

cursor.execute(query_insert, datos_nueva_sociedad)
conexion.commit()
print("Nueva sociedad insertada correctamente.")

# Cerrar conexión
cursor.close()
conexion.close()