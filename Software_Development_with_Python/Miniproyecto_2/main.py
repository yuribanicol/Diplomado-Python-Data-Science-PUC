import parametros as p
import random


# NO MODIFICAR
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion, tipo):
        if accion == "acelerar":
            if tipo == "automovil":
                self.resistencia_actual -= 5
            elif tipo == "moto":
                self.resistencia_actual -= 3
        elif accion == "frenar":
            if tipo == "automovil":
                self.resistencia_actual -= 10
            elif tipo == "moto":
                self.resistencia_actual -= 7
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"


# NO MODIFICAR
def seleccionar(vehiculos):
    if not len(vehiculos):
        print("No hay vehículos instanciados todavía")
        return

    print("Los vehículos disponibles son:")
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    while elegido < 0 or elegido >= len(vehiculos):
        print("intentelo de nuevo.")
        elegido = int(input())

    vehiculo = vehiculos[elegido]
    print("Se seleccionó el vehículo", str(vehiculo))
    return vehiculo


# Parte 1: Definición de clases

def avanzar(velocidad, tiempo):
    kilometraje = (velocidad*tiempo)/1000
    return kilometraje


class Automovil:
    def __init__(self, kilometraje, ano):
        self.kilometraje = float(kilometraje)
        self.ano=int(ano)
        self.aceleracion = 0
        self.velocidad = 0
        self.ruedas = [Rueda() for _ in range(4)]
    
    def avanzar(self, tiempo):
        velocidad_ms=self.velocidad/3.6
        kilometraje_avanzado=avanzar(velocidad_ms,tiempo)
        self.kilometraje+=kilometraje_avanzado

    def acelerar(self, tiempo):
        tiempo_horas=tiempo/3600
        self.aceleracion+= tiempo_horas*0.5
        self.velocidad+=self.aceleracion*tiempo_horas

        self.avanzar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("acelerar", "automovil")
        self.aceleracion = 0

    def frenar(self, tiempo):
        tiempo_horas=tiempo/3600
        self.aceleracion-= tiempo_horas*0.5
        self.velocidad+=self.aceleracion*tiempo_horas

        if self.velocidad < 0:
            self.velocidad = 0
        
        self.avanzar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("frenar", "automovil")

        self.aceleracion = 0

    def obtener_kilometraje(self):
        return self.kilometraje
    
    def reemplazar_rueda(self):
        rueda_menor = self.ruedas[0]
        for rueda in self.ruedas:
            if rueda.resistencia_actual < rueda_menor.resistencia_actual:
                rueda_menor = rueda
       
        self.ruedas.remove(rueda_menor)
        self.ruedas.append(Rueda())

    def __str__(self):
        return f"Automóvil del año {self.ano}."


class Moto:
    def __init__(self, kilometraje, ano, cilindrada):
        self.kilometraje = float(kilometraje)
        self.ano=int(ano)
        self.cilindrada=int(cilindrada)
        self.aceleracion = 0
        self.velocidad = 0
        self.ruedas = [Rueda() for _ in range(2)]
    
    def avanzar(self, tiempo):
        velocidad_ms=self.velocidad/3.6
        kilometraje_avanzado=avanzar(velocidad_ms,tiempo)
        self.kilometraje+=kilometraje_avanzado

    def acelerar(self, tiempo):
        tiempo_horas=tiempo/3600
        self.aceleracion+= (tiempo_horas*0.8)+(self.cilindrada*0.2)
        self.velocidad+=self.aceleracion*tiempo_horas*3

        self.avanzar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("acelerar", "moto")
        
        self.aceleracion = 0

    def frenar(self, tiempo):
        tiempo_horas=tiempo/3600
        self.aceleracion-= (tiempo_horas*0.8)+(self.cilindrada*0.2)
        self.velocidad+=self.aceleracion*tiempo_horas*2

        if self.velocidad < 0:
            self.velocidad = 0
        
        self.avanzar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar("frenar", "moto")
        
        self.aceleracion = 0

    def obtener_kilometraje(self):
        return self.kilometraje
    
    def reemplazar_rueda(self):
        ruedas_a_cambiar = []
        for rueda in self.ruedas:
            if rueda.resistencia_actual < (rueda.resistencia_total*0.5):
                ruedas_a_cambiar.append(rueda)

        for rueda in ruedas_a_cambiar:
            self.ruedas.remove(rueda)
            self.ruedas.append(Rueda())

    def __str__(self):
        return f"Moto del año {self.ano}."


# Parte 2: Completar acciones

def accion(vehiculo, opcion):
    if opcion == 2:  # Acelerar
        tiempo = float(input("Ingrese el tiempo en segundos para acelerar: "))
        vehiculo.acelerar(tiempo)
        print(f"Se ha acelerado por {tiempo} segundos, llegando a una velocidad de {vehiculo.velocidad} km/h")
    elif opcion == 3:  # Frenar
        tiempo = float(input("Ingrese el tiempo en segundos para frenar: "))
        vehiculo.frenar(tiempo)
        print(f"Se ha frenado por {tiempo} segundos, llegando a una velocidad de {vehiculo.velocidad} km/h")
    elif opcion == 4:  # Avanzar
        tiempo = float(input("Ingrese el tiempo en segundos para avanzar: "))
        vehiculo.avanzar(tiempo)
        print(f"Se ha avanzado por {tiempo} segundos a una velocidad de {vehiculo.velocidad} km/h")
    elif opcion == 5:  # Cambiar rueda
        vehiculo.reemplazar_rueda()
        print("Se han reemplazado las ruedas con éxito.")
    elif opcion == 6:  # Mostrar Estado
        print(f"Año: {vehiculo.ano}")
        print(f"Velocidad: {vehiculo.velocidad} km/h")
        print(f"Kilometraje: {vehiculo.obtener_kilometraje()} km")
        print("Estado de las ruedas:")
        for rueda in vehiculo.ruedas:
            print(rueda.estado)


def main():
    vehiculos = []

    auto_ejemplo = Automovil(kilometraje=10000.0, ano=2022)
    moto_ejemplo = Moto(kilometraje=5000.0, ano=2020, cilindrada=250)
    
    vehiculos.append(auto_ejemplo)
    vehiculos.append(moto_ejemplo)
    
    # NO MODIFICAR
    vehiculo = None

    dict_opciones = {
        1: ("Seleccionar Vehiculo", seleccionar),
        2: ("Acelerar", accion),
        3: ("Frenar", accion),
        4: ("Avanzar", accion),
        5: ("Reemplazar Rueda", accion),
        6: ("Mostrar Estado", accion),
        0: ("Salir", None)
    }

    opcion = -1
    while opcion != 0:

        for llave, valor in dict_opciones.items():
            print(f"{llave}: {valor[0]}")

        try:
            opcion = int(input("Opción: "))
            print()

        except ValueError:
            print("Ingrese opción válida.")
            opcion = -1

        if opcion != 0 and opcion in dict_opciones.keys():
            if opcion == 1:
                vehiculo = dict_opciones[opcion][1](vehiculos)
            else:
                if vehiculo is None and vehiculos:
                    vehiculo = vehiculos[0]
                if vehiculo is None:
                    print("Aún no hay vehículos...")
                else:
                    dict_opciones[opcion][1](vehiculo, opcion)
        elif opcion == 0:
            pass
        else:
            print("Ingrese opción válida.")
            opcion = -1

        print()


if __name__ == "__main__":
    main()