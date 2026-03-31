def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    name=input("Ingrese nombre: ").lower()
    print(f"Contiene a: {"a" in name}")
    print(f"Contiene e: {"e" in name}")
    print(f"Contiene i: {"i" in name}")
    print(f"Contiene o: {"o" in name}")
    print(f"Contiene u: {"u" in name}")
