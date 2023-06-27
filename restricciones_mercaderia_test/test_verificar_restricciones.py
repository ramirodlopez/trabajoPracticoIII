from unittest import TestCase
from unittest.mock import Mock
import pytest
from Contenedor.BasicoHC import BasicoHC
from Excepcion.restriccion_excepcion import RestriccionException
from Mercaderia.Mercaderia import Mercaderia
from Mercaderia.Tipo_Mercaderia import TipoMercaderia
from Restricciones_Mercaderia.Verificar_Restricciones_Mercaderia import VerificarRestricciones

class VerificarRestriccionesTest(TestCase):
    def test_dado_mercaderia_es_tipo_quimico_cuando_contenedor_no_es_especial_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(1, 1, 1, 2, 321, "quimico")
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_especial(container, mercaderia)

    def test_cuando_largo_mercaderia_es_mayor_que_largo_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(1, 1, 15, 1, 321, None)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_largo(container, mercaderia)

    def test_cuando_alto_mercaderia_es_mayor_que_alto_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(1, 8, 1, 1, 321, None)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_alto(container, mercaderia)

    def test_cuando_volumne_mercaderia_es_mayor_que_volumen_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(10, 1, 11, 1, 321, None)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_volumen(container, mercaderia)
    
    def test_cuando_peso_mercaderia_es_mayor_que_peso_soportado_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(1, 1, 11, 40.9000, 321, None)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_peso(container, mercaderia)
    

    def test_cuando_ancho_mercaderia_es_mayor_que_ancho_contenedor_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False)
        mercaderia = Mercaderia(10, 1, 1, 1, 321, None)
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_ancho(container, mercaderia)


    def test_dado_mercaderia_de_tipo_alimenticia_cuando_contenedor_no_es_alimenticio_entonces_ocurre_restriction_exception(self):
        container = BasicoHC(123, False) 
        mercaderia = Mercaderia(1, 1, 1, 2, 321, "alimenticia")
        verificar_restricciones = VerificarRestricciones()
        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_tipo_mercaderia(container, mercaderia)

    def test_dado_un_contenedor_con_mercaderia_tipo_alimento_cuando_se_agrega_mercaderia_tipo_quimico_entonces_ocurre_restriction_exception(self):
        verificar_restricciones_mercaderia = Mock()
        verificar_restricciones_mercaderia.verificar_restricciones.return_value = None 
        container = BasicoHC(123, False) 
        
        mercaderia_quimica = Mercaderia(1, 1, 1, 2, 321, "quimico")  
        mercaderia_alimenticia = Mercaderia(1, 1, 1, 2, 321, "alimenticia") 
         
        container.cargar_mercaderia(mercaderia_quimica, verificar_restricciones_mercaderia)
        verificar_restricciones = VerificarRestricciones()

        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_mercaderias_en_mismo_contenedor(container, mercaderia_alimenticia, TipoMercaderia.ALIMENTICIO, TipoMercaderia.QUIMICO)
    
    
    def test_dado_un_contenedor_con_quimico_cuando_se_agrega_mercaderia_tipo_alimenticio_entonces_ocurre_restriction_exception(self):
        verificar_restricciones_mercaderia = Mock()
        verificar_restricciones_mercaderia.verificar_restricciones.return_value = None 
        container = BasicoHC(123, False) 
        
        mercaderia_quimica = Mercaderia(1, 1, 1, 2, 321, "quimico")  
        mercaderia_alimenticia = Mercaderia(1, 1, 1, 2, 321, "alimenticia") 
         
        container.cargar_mercaderia(mercaderia_alimenticia, verificar_restricciones_mercaderia)
        verificar_restricciones = VerificarRestricciones()

        with pytest.raises(RestriccionException):
            verificar_restricciones.verificar_mercaderias_en_mismo_contenedor(container, mercaderia_quimica, TipoMercaderia.QUIMICO, TipoMercaderia.ALIMENTICIO)
