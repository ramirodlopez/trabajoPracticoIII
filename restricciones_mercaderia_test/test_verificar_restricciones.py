from unittest import TestCase
import pytest
from Contenedor.BasicoHC import BasicoHC
from Excepcion.Restriccion_Excepcion import RestriccionException
from Mercaderia.Mercaderia import Mercaderia
from Restricciones_Mercaderia.Verificar_Restricciones_Mercaderia import VerificarRestricciones

class VerificarRestriccionesTest(TestCase):
    def test_dado_mercaderia_es_especial_cuando_contenedor_no_es_especial_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(True, 1, 1, 1, 2, 321)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_especial(container, mercaderia)

    def test_cuando_largo_mercaderia_es_mayor_que_largo_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(False, 1, 1, 15, 1, 321)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_largo(container, mercaderia)

    def test_cuando_alto_mercaderia_es_mayor_que_alto_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(False, 1, 8, 1, 1, 321)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_alto(container, mercaderia)

    def test_cuando_volumne_mercaderia_es_mayor_que_volumen_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(False, 10, 1, 11, 1, 321)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_volumen(container, mercaderia)
    
    def test_cuando_peso_mercaderia_es_mayor_que_peso_soportado_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(False, 1, 1, 11, 40.9000, 321)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_peso(container, mercaderia)
    

    def test_cuando_ancho_mercaderia_es_mayor_que_ancho_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False)
        mercaderia = Mercaderia(False, 10, 1, 1, 1, 321)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_ancho(container, mercaderia)