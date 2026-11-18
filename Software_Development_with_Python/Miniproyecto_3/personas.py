##############################################################
from random import randint, choice
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre
### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nombre: str, tiempo_entrega: int):
        super().__init__(nombre)
        self.tiempo_entrega = tiempo_entrega
        self.energia = randint(75, 100)
    
    def repartir(self, pedido: list) -> float:
        if len(pedido) <= 2:
            factor_tamano = 5
            factor_velocidad = 1.25
        else:
            factor_tamano = 15
            factor_velocidad = 0.85
        self.energia -= factor_tamano
        
        demora = self.tiempo_entrega * factor_velocidad
        return float(demora)
    
### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre: str, habilidad: int):
        super().__init__(nombre)
        self.habilidad = habilidad
        self.energia = randint(50, 80)
   
    def cocinar(self, informacion_plato: list):
        nombre_plato = informacion_plato[0]
        tipo_plato = informacion_plato[1]

        if tipo_plato == "Bebestible":
            plato_creado = Bebestible(nombre_plato)
            if plato_creado.tamano == "Pequeño":
                self.energia -= 5
            elif plato_creado.tamano == "Mediano":
                self.energia -= 8
            elif plato_creado.tamano == "Grande":
                self.energia -= 10
        else:
            plato_creado = Comestible(nombre_plato)
            self.energia -= 15
        
        if plato_creado.dificultad > self.habilidad:
            factor_calidad = 0.7
        else:
            factor_calidad = 1.5
        plato_creado.calidad = int(plato_creado.calidad * factor_calidad)
        return plato_creado
### FIN PARTE 2.3 ###
       
### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nombre: str, platos_preferidos: list):
        super().__init__(nombre)
        self.platos_preferidos = platos_preferidos

    def recibir_pedido(self, pedido: list, demora: float) -> float:
            calificacion = 10.0
            
            if len(pedido) < len(self.platos_preferidos) or demora >= 20:
                calificacion /= 2

            for plato in pedido:
                if plato.calidad >= 11:
                    calificacion += 1.5
                elif plato.calidad <= 8:
                    calificacion -= 3.0
           
            if calificacion < 0:
                calificacion = 0.0              
            return float(calificacion)
### FIN PARTE 2.4 ###

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = [
        "Jugo Natural",
        "Empanadas",
        ]
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos:
            print(f" - {plato}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
