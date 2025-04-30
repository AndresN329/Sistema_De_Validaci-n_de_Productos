# No se que hacer :) 

print("-" * 40)
print("            Descuenteitor ")
print("-" * 40)

print("\nHola, puedo calcular el total de los productos que compras, incluso con descuento :)")
print("Necesitare algunos datos...")

#Recoleccion de datos :0

nombreP = input("\nPor favor, ingresa el nombre del producto: ")

#precio unitario
while True : 
    try: 
        PrecioU = float(input("\nBien, Ahora ingresa el valor unitario del producto: "))
        if PrecioU > 0:
            break
        else:
            print("\nEl valor tiene que ser positivo -__-")
    except ValueError:
        print("\nDato incorrecto, por favor ingrese un numero >:c") 
        
#Especificar la cantidad de productos    
while True : 
    try: 
        CantidadP = int(input("\n¿Cuantos productos son?: "))
        if CantidadP > 0:
            break
        else:
            print("\nTiene que ser positivo -__-")
    except ValueError:
        print("\nDato incorrecto, por favor ingrese un numero >:c") 

PrecioTotalsinDes = PrecioU * CantidadP
    
#¿Tiene descuento?
while True:
    Descuento = input("\n¿Tu producto tiene descuento?(Si/No): ").lower()
#si tiene descuento entonces...
    if Descuento == "si":
        while True:  
            try:
                porcentaje = int(input("\n¿De cuánto es el descuento?(Ingresa sin '%' pls): "))
                if 0 <= porcentaje <= 100:  
                    PrecioDescuento = PrecioU - (PrecioU * porcentaje / 100)
                    SiDescuento = PrecioTotalsinDes * (porcentaje / 100)
                    TotalconDescuento = PrecioTotalsinDes - SiDescuento
                    break
                else:
                    print("\nDebe estar entre 0 y 100 :)")
            except ValueError:
                print("\nEso no es un valor valido :(")
        break
    elif Descuento == "no":
        PrecioTotalsinDes = PrecioTotalsinDes
        porcentaje = "No aplica"
        break
    else:
        print("Por favor solo 'Si' o 'No' ")



#Impresion de resultados
print("\nEstos son los resultados")
print("\nEl nombre del producto es: ",nombreP)
print("El precio Unitario del producto es: ",PrecioU)
print("Cantidad de productos: ",CantidadP)
print("Valor sin descuento: ",PrecioTotalsinDes)

#aqui me ayudo a hacer lo que queria el mejor amigo de todos... y no hablo de un perro :)
if porcentaje != "No aplica":
    print("Porcentaje de descuento: ",porcentaje,"%")
    print("Descuento total: ",SiDescuento)
    print("Total a pagar: ", TotalconDescuento)
else:
    print("Porcentaje de descuento: ",porcentaje)

print("\nGracias por usar descuenteitor ;)")
