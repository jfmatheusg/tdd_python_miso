class Calculadora:
    def sumar(cadena):
        if cadena =="":
            return 0
        elif "," in cadena or "&" in cadena or ":" in cadena:
            cadena=cadena.replace("&",",")
            cadena = cadena.replace(":", ",")
            numeros=cadena.split(",")
            suma=0
            for num in numeros:
                suma=suma+int(num)
            return suma
        else:
            return int(cadena)


