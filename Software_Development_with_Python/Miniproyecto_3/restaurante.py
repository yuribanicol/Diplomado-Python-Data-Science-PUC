##############################################################
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre: str, platos: dict, cocineros: list, repartidores: list):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0.0

    def recibir_pedidos(self, clientes: list):
        calificaciones_totales = 0.0

        for cliente in clientes:
            platos_a_cocinar = cliente.platos_preferidos
            pedido = []

            for nombre_plato in platos_a_cocinar:
               cocinero_disponible = None
               for c in self.cocineros:
                   if c.energia > 0:
                       cocinero_disponible = c
                       break
                
               if cocinero_disponible and nombre_plato in self.platos:
                    informacion_plato = self.platos[nombre_plato]
                    plato_cocinado = cocinero_disponible.cocinar(informacion_plato)
                    pedido.append(plato_cocinado)
            
            repartidor_disponible = None
            for r in self.repartidores:
                if r.energia > 0:
                    repartidor_disponible = r
                    break
            if repartidor_disponible:
                demora = repartidor_disponible.repartir(pedido)
            else:
                pedido = []
                demora = 0.0

            calificacion_cliente = cliente.recibir_pedido(pedido, demora)
            calificaciones_totales += calificacion_cliente
        
        if len(clientes) > 0:
            self.calificacion = calificaciones_totales / len(clientes)
        else:
            self.calificacion = 0.0
### FIN PARTE 3 #


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
