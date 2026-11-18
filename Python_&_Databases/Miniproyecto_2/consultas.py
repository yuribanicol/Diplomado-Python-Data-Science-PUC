# Importar librerías necesarias. NO SE DEBE IMPORTAR NINGUNA OTRA LIBRERÍA.
import mysql.connector as db

# Conexión a la base de datos
conn = db.connect(
  host="localhost",
  user="root",
  password="mysql123", # Cambiar por la contraseña de su base de datos
  database="mp2"
)

# Crear cursor
cursor = conn.cursor()

# NO TOCAR. Función que encapsula lógica para ejecutar una consulta y mostrar los resultados.
def run_query(query, header):
  if not query or query == '':
    print("No se definió consulta para ejecutar")
    return
  try:
    cursor.execute(query)
    rows = cursor.fetchall()
    print(header + '\n')
    for row in rows:
      print(row)
  except Exception as e:
    print('Consulta resultó en error: ' + str(e))


# ---------- CONSULTA 1 ----------
# RELLENAR SOLAMENTE LA VARIABLE consulta_1
consulta_1 = """
SELECT COUNT(*) 
FROM pedidos p 
JOIN clientes c ON p.id_cliente = c.id 
WHERE c.email = 'jessicaflores@example.com';
"""

print('\n\n' + '-'*10 + ' INICIO CONSULTA 1 ' + '-'*10 + '\n')
run_query(consulta_1, 'Número de pedidos realizados por cliente con email jessicaflores@example.com:')
print('\n' + '-'*10 + ' FIN CONSULTA 1 ' + '-'*10 + '\n')


# ---------- CONSULTA 2 ----------
# RELLENAR SOLAMENTE LA VARIABLE consulta_2
consulta_2 = """
SELECT pr.id, pr.nombre, pr.precio, pp.cantidad 
FROM productos_pedidos pp 
JOIN productos pr ON pp.id_producto = pr.id 
WHERE pp.id_pedido = 2 
ORDER BY pr.id ASC;
"""

print('\n\n' + '-'*10 + ' INICIO CONSULTA 2 ' + '-'*10 + '\n')
run_query(consulta_2, 'id, nombre, precio y cantidad de productos solicitados en pedido con id 2:')
print('\n' + '-'*10 + ' FIN CONSULTA 2 ' + '-'*10 + '\n')


# ---------- CONSULTA 3 ----------
# RELLENAR SOLAMENTE LA VARIABLE consulta_3
consulta_3 = """
SELECT p.id, p.direccion, p.detalle, p.fecha 
FROM pedidos p 
JOIN productos_pedidos pp ON p.id = pp.id_pedido 
JOIN productos pr ON pp.id_producto = pr.id 
WHERE pr.nombre = 'Tablet' 
  AND p.fecha BETWEEN '2024-01-05' AND '2024-01-07' 
ORDER BY p.fecha DESC;
"""

print('\n\n' + '-'*10 + ' INICIO CONSULTA 3 ' + '-'*10 + '\n')
run_query(consulta_3, 'id, direccion, detalle y fecha de todos los pedidos entre el 5 de enero y el 7 de enero (incluyendo ambas fechas) que contengan un Tablet, ordenados por fecha descendentemente:')
print('\n' + '-'*10 + ' FIN CONSULTA 3 ' + '-'*10 + '\n')


cursor.close()
conn.close()
