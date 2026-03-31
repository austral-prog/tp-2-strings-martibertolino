def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    price_product=int(input("ingrese el precio"))
    print(f"Precio: {price_product}")
    sale_product=float(input("ingrese el descuento"))
    print(f"Descuento: {sale_product}")
    price_sale=(price_product-sale_product)
    print(f"Precio con descuento: {price_sale}")
    cant_product=int(input("ingrese el cantidad de producto"))
    total=(cant_product*price_sale)
    print(f"Total: {total}")
