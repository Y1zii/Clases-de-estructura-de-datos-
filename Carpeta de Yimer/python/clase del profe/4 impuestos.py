edad = int(input("ingresa tu edad ---------> "))
ingreso = float(input("ingresa tu ingreso mensual ---------> "))
if edad >= 16 and ingreso >= 1000:
    print("puede tributar")
else:
    print("no puede tributar")
