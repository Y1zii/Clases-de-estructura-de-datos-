p = float(input("ingrese su peso (KG)--->  "))
e = float(input("ingrese su estatura (M) ---> "))
imc = p/(e)**2
print (f"su IMC es : {imc}")
if imc < 18.5:
    print("bajo de peso")
elif imc >= 18.5 and imc < 25:
    print("normal")
elif imc >= 25 and imc <30:
    print("sobrepeso")
elif imc >= 30:
    print("obeso")
else:
    print("estas en peligro")