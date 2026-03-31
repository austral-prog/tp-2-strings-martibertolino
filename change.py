def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto=float(input("ingrese el gasto"))
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    dinero=int(input("ingrese el dinero recibido"))
    print(dinero)
    print()
    print("Vuelto")
    vuelto=(dinero-gasto)
    print()
    print("Pesos:")
    vuelto_entero=(int(vuelto))
    print(vuelto_entero)
    print("Centavos:")
    print(int(round((vuelto-vuelto_entero)*100)))
