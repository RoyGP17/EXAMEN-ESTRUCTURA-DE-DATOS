n = int(input("Ingrese un número: "))
p = int(input("Ingrese la base numérica deseada: "))
def convertir_a_base(numero, base):
    if numero == 0:
      return 0
    resultado = convertir_a_base(numero // base, base)
    return  resultado + (numero % base)

print(convertir_a_base(n, p))