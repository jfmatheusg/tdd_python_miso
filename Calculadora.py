class Calculadora:
    def sumar(cadena):
        if cadena =="":
            return 0
        elif "," in cadena:
            numeros=cadena.split(",")
            suma=0
            for num in numeros:
                suma=suma+int(num)
            return suma
        else:
            return int(cadena)

