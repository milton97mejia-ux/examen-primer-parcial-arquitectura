from django.test import TestCase
from .utils import convertir_numero, analizar_texto_utf8


class PruebasAnalizador(TestCase):

    # Prueba 1: Conversión válida y ajuste de bytes
    def test_conversion_valida(self):
        res = convertir_numero("255", 10)
        self.assertEqual(res["decimal"], "255")
        self.assertEqual(res["binario"], "11111111")
        self.assertEqual(res["bits_significativos"], 8)
        self.assertEqual(res["bytes_necesarios"], 1)

    # Prueba 2: Ajuste correcto al siguiente límite de byte (ej. 256 necesita 16 bits)
    def test_ajuste_limite_byte(self):
        res = convertir_numero("256", 10)
        self.assertEqual(res["binario"], "0000000100000000")
        self.assertEqual(res["bytes_necesarios"], 2)

    # Prueba 3: Error cuando un dígito no pertenece a la base seleccionada
    def test_error_digito_invalido_base(self):
        with self.assertRaises(ValueError):
            convertir_numero("1021", 2)  # El '2' no es válido en binario

    # Prueba 4: Error cuando el valor excede el límite máximo (65535)
    def test_error_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            convertir_numero("65536", 10)

    # Prueba 5: Análisis de texto UTF-8 con la letra 'ñ'
    def test_analisis_utf8_con_enie(self):
        res = analizar_texto_utf8("Año")
        self.assertEqual(len(res), 3)
        # La 'ñ' debe tener 2 bytes en UTF-8 (0xC3 0xB1)
        enie_data = res[1]
        self.assertEqual(enie_data["caracter"], "ñ")
        self.assertEqual(enie_data["bytes_utf8"], "0xC3 0xB1")

    # Prueba 6: Error cuando el texto supera el límite de 20 caracteres
    def test_error_longitud_texto_excedida(self):
        texto_largo = "a" * 21
        with self.assertRaises(ValueError):
            analizar_texto_utf8(texto_largo)