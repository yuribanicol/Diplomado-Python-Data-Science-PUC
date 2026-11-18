# Importar liibrerías necesarias. NO SE DEBE IMPORTAR NINGUNA OTRA LIBRERÍA.
import mysql.connector as db
import csv

# Desde este punto en adelante se debe crear el código solicitado.

# Conexión a la base de datos
conn = db.connect(
    host="localhost",
    user="root",
    password="mysql123",
    database="mp2"
)
cursor = conn.cursor()

# Tabla productos
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    precio INT
);
""")

# Tabla clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(255),
    email VARCHAR(255)
);
""")

# Tabla pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INT PRIMARY KEY,
    fecha DATE,
    direccion VARCHAR(255),
    id_cliente INT,
    detalle VARCHAR(255),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
""")

# Tabla productos_pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos_pedidos (
    id_producto INT,
    id_pedido INT,
    cantidad INT,
    PRIMARY KEY (id_producto, id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
);
""")

conn.commit()

with open('./data/productos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    for row in reader:
        cursor.execute(
            "INSERT INTO productos (id, nombre, descripcion, precio) VALUES (%s, %s, %s, %s)",
            (int(row[0]), row[1], row[2], int(row[3]))
        )

# Cargar clientes.csv
with open('./data/clientes.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    for row in reader:
        cursor.execute(
            "INSERT INTO clientes (id, nombre, email) VALUES (%s, %s, %s)",
            (int(row[0]), row[1], row[2])
        )

# Cargar pedidos.csv
with open('./data/pedidos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    for row in reader:
        cursor.execute(
            "INSERT INTO pedidos (id, fecha, direccion, id_cliente, detalle) VALUES (%s, %s, %s, %s, %s)",
            (int(row[0]), row[1], row[2], int(row[3]), row[4])
        )

# Cargar productos_pedidos.csv
with open('./data/productos_pedidos.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    for row in reader:
        cursor.execute(
            "INSERT INTO productos_pedidos (id_producto, id_pedido, cantidad) VALUES (%s, %s, %s)",
            (int(row[0]), int(row[1]), int(row[2]))
        )

conn.commit()
cursor.close()
conn.close()