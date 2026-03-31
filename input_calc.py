def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    ba_rec=int(input("ingrese la base del rectangulo"))
    al_rec=int(input("ingrese la altura del rectangulo"))
    area_rec=(ba_rec*al_rec)
    per_rec=(2*al_rec)+(2*ba_rec)
    print(f"Base: {ba_rec}")
    print(f"Altura: {al_rec}")
    print(f"Area: {area_rec}")
    print(f"Perimetro: {per_rec}")
