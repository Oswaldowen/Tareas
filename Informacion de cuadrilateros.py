def verificar_figura(a, b, c, d):
    if a == b == c == d != 0:
        print("Es cuadrado")
    elif (a == b == c != d) or (a == b == d != c) or (a == c == d != b) or (b == c == d != a):
        print("Es rectángulo")
    elif (a == b == 0) or (a == c == 0) or (a == d == 0) or (b == c == 0) or (b == d == 0) or (c == d == 0):
        print("No se encontró figura")
    elif (a == b == c == 0) or (a == b == d == 0) or (a == c == d == 0) or (b == c == d == 0):
        print("No se encontró figura")
    elif (a == b == 0 and c == d) or (a == c == 0 and b == d) or (a == d == 0 and b == c):
        print("No se encontró figura")
    elif (a == b != c == d) or (a == c != b == d) or (a == d != b == c) or (b == c != a == d) or (b == d != a == c) or (c == d != a == b):
        print("Es triángulo")
    else:
        print("Es otro cuadrilátero")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
d = int(input("Ingrese el cuarto número: "))

verificar_figura(a, b, c, d)
