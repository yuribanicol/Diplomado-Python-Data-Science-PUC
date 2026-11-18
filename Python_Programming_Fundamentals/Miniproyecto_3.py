dic_disponibilidad={}
archivo_disponibilidad=open("disponibilidad.txt","r",errors="ignore")
archivo_en_lineas_disponibilidad=archivo_disponibilidad.readlines()
archivo_disponibilidad.close()

for linea in archivo_en_lineas_disponibilidad:
    linea=linea.rstrip('\n')
    datos = linea.split(" ")
    if len(datos)==2:
        dic_disponibilidad[datos[0].lower()]=int(datos[1])

dic_pacientes={}
archivo_pacientes=open("pacientes.csv","r",errors="ignore")
archivo_en_lineas_pacientes=archivo_pacientes.readlines()
archivo_pacientes.close()

for linea in archivo_en_lineas_pacientes:
    linea=linea.rstrip('\n')
    if linea != "":
        datos=linea.split(",")
        nombre=datos.pop(0).lower().strip()
        dic_pacientes[nombre]=[examen.lower().strip() for examen in datos]

def imprimir(disponibilidad):
    for examen, horas in disponibilidad.items():
        print(examen.upper()+":",horas)
def atender(nombre_paciente,disponibilidad,pacientes):
    nombre_busqueda=nombre_paciente.lower()
    if nombre_busqueda not in pacientes:
        print("No se puede atender a",nombre_paciente,"porque no se encuentra en la reserva de horas.")
        return

    lista_de_examenes = pacientes[nombre_busqueda]
    puede_atender = True
    examen_fallido = ""

    for examen in lista_de_examenes:
        if disponibilidad.get(examen,0)==0:
            puede_atender=False
            examen_fallido=examen.upper()
            break
    if puede_atender:
        for examen in lista_de_examenes:
            disponibilidad[examen]=disponibilidad[examen]-1
        print("Se ha atendido con éxito a",nombre_paciente.upper()+"!")
    else:
        print("No es posible atender a",nombre_paciente.upper(),"porque no existen horas disponibles para el examen",examen_fallido+".")
def agregar(lista_examenes,disponibilidad):
    for examen in lista_examenes:
        examen_min = examen.lower()
        if examen_min in disponibilidad:
            disponibilidad[examen_min]=disponibilidad[examen_min]+1

while True:
    imprimir(dic_disponibilidad)
    entrada=input("Bienvenido/a, ingrese la instrucción a continuación: ")
    
    if entrada.lower()=="stop":
        break        
    partes=entrada.split(" ")
    if len(partes)>1:
        comando=partes[0].lower()
        if comando=="atender":
            atender(partes[1],dic_disponibilidad,dic_pacientes)
        elif comando=="agregar":
            agregar(partes[1:],dic_disponibilidad)