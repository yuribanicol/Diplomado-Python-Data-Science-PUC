nombre_tienda1=input("Ingrese nombre tienda 1: ")
nombre_tienda2=input("Ingrese nombre tienda 2: ")

tienda1=nombre_tienda1[0:3].upper()
tienda2=nombre_tienda2[0:3].upper()

if tienda1==tienda2:
    tienda2=tienda2+"2"

costo_tienda1=0
costo_tienda2=0
presupuesto_max=100_000
ronda=1

print(tienda1+": $"+str(costo_tienda1))
print(tienda2+": $"+str(costo_tienda2))
print("")

while costo_tienda1<=presupuesto_max and costo_tienda2<=presupuesto_max:
    print("Ronda "+str(ronda)+":")
    print("")

    print("Ingrese instrucciones tienda 1: ")
    for i in range(3):
        instruccion=input().lower().split()

        if instruccion[0]=="descuento":
            costo_tienda1=costo_tienda1-int(instruccion[1])
        elif instruccion[0]=="despacho":
            if instruccion[1]=="cerca": 
                costo_tienda1=costo_tienda1+1_000
            if instruccion[1]=="normal": 
                costo_tienda1=costo_tienda1+5_000
            if instruccion[1]=="lejos":
                costo_tienda1=costo_tienda1+10_000
        else:
            cantidad=int(instruccion[0])
            precio=int(instruccion[1])

            if cantidad>=10:
                costo_tienda1=costo_tienda1+(cantidad-1)*precio
            else:
                costo_tienda1=costo_tienda1+(cantidad*precio)
    if costo_tienda1<0: 
        costo_tienda1=0
    print("")

    print("Ingrese instrucciones tienda 2: ")
    for i in range(3):
        instruccion=input().lower().split()

        if instruccion[0]=="descuento":
            costo_tienda2=costo_tienda2-int(instruccion[1])
        elif instruccion[0]=="despacho":
            if instruccion[1]=="cerca":
                costo_tienda2=costo_tienda2+1_000
            if instruccion[1]=="normal":
                costo_tienda2=costo_tienda2+5_000
            if instruccion[1]=="lejos":
                costo_tienda2=costo_tienda2+10_000
        else:
            cantidad=int(instruccion[0])
            precio=int(instruccion[1])

            if cantidad>=10:
                costo_tienda2=costo_tienda2+(cantidad-1)*precio
            else:
                costo_tienda2=costo_tienda2+(cantidad*precio)
    if costo_tienda2<0:
        costo_tienda2=0
    print("")

    print(tienda1+": $"+str(costo_tienda1))
    print(tienda2+": $"+str(costo_tienda2))
    print("")

    ronda=ronda+1

if costo_tienda1>presupuesto_max and costo_tienda2>presupuesto_max:
    print("hubo un empate.")
elif costo_tienda1>presupuesto_max:
    print(tienda2,"es mejor.")
else:
    print(tienda1,"es mejor.")




