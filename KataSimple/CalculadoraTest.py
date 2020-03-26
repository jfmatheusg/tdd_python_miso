from unittest import TestCase

from calculadora.Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora.sumar(""), 0, "Cadena vacia")

    def test_sumar_unacadena(self):
        self.assertEqual(Calculadora.sumar(("1")), 1, "Un numero")

    def test_sumar_cadenaconUnNumero(self):
        self.assertEqual(Calculadora.sumar(("1")), 1, "Cadena con Un numero")
        self.assertEqual(Calculadora.sumar(("2")), 2, "Cadena con Un numero")

    def test_sumar_cadenacondosNumeros(self):
        self.assertEqual(Calculadora.sumar(("1,3")), 4, "Dos numeros")

    def test_sumar_cadenaconvariosNumeros(self):
        self.assertEqual(Calculadora.sumar(("5,2,4,1")), 12, "Varios numeros")

    def test_sumar_cadenaconSeparadores(self):
        self.assertEqual(Calculadora.sumar(("5,2&4:1:2&8")), 22, "Varios numeros con dif sep")

# if tam > 3:
#    return tam, int(min)
# else:
