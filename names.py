def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    one=input("ingrese su nombre")
    two=input("ingrese su apellido")
    name=f"{one} {two}"
    print(name.lower())
    print(name.title())
    print(name.upper())
    print("\t"+name.lower())
