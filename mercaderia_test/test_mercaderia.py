from unittest import TestCase
import pytest
from contenedor.basico_hc import BasicoHC

from excepcion.restriccion_excepcion import RestriccionException
from mercaderia.mercaderia import Mercaderia

class MercaderiaTest(TestCase):
    def test_dado_mercaderia_es_especial_cuando_contenedor_no_es_especial_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(True, 1, 1, 1, 2)
        with pytest.raises(RestriccionException):
            mercaderia.verificar_especial(container)

    def test_cuando_largo_mercaderia_es_mayor_que_largo_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(False, 1, 1, 15, 1)
        with pytest.raises(RestriccionException):
            mercaderia.verificar_largo(container)

    def test_cuando_alto_mercaderia_es_mayor_que_alto_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(False, 1, 8, 1, 1)
        with pytest.raises(RestriccionException):
            mercaderia.verificar_alto(container)

    def test_cuando_volumne_mercaderia_es_mayor_que_volumen_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(False, 10, 1, 11, 1)
        with pytest.raises(RestriccionException):
            mercaderia.verificar_volumen(container)
    
    def test_cuando_peso_mercaderia_es_mayor_que_peso_soportado_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(False, 1, 1, 11, 40.9000)
        with pytest.raises(RestriccionException):
            mercaderia.verificar_peso(container)
    

    def test_cuando_ancho_mercaderia_es_mayor_que_ancho_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False)
        mercaderia = Mercaderia(False, 10, 1, 1, 1)
        with pytest.raises(RestriccionException):
            mercaderia.verificar_ancho(container)
    