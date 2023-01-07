n = int(input("Ingresa un numero n: "))
p = int(input("Ingresa un numero p: "))
def suma_K(n,p):
    if n == 1:
        return p
    else:
        return p * n + suma_K(n-1, p)

print(suma_K(n,p))