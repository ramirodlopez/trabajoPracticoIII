from unittest import TestCase
from unittest.mock import Mock
from Contenedor.Basico import Basico
from Contenedor.Builder.Basico_Builder import BuilderBasico
from Contenedor.Director import Director
from Mercaderia.Mercaderia import Mercaderia

class ContainerTest(TestCase):
    def test_dado_mercaderia_pasa_restricciones_cuando_cargo_mercaderia_entonces_verifico_misma_mercaderia_contenedor(self):
        peso = 10
        ancho = 1
        alto = 1.2
        largo = 2
        
        mercaderia_mock = Mock()
        mercaderia_mock.__esEspecial = False
        mercaderia_mock.__ancho = ancho
        mercaderia_mock.__alto = alto
        mercaderia_mock.__largo = largo
        mercaderia_mock.__peso = peso
        mercaderia_mock.__id = 123
        
        mercaderia_mock.get_peso.return_value = peso
        mercaderia_mock.devolver_volumen.return_value = ancho * alto * largo

        verificar_restricciones_mercaderia = Mock()
        verificar_restricciones_mercaderia.verificar_restricciones.return_value = None 

        builder_basico = BuilderBasico()
        director = Director()
        director.builder = builder_basico
        contenedor = director.crear_contenedor_basico(132, False)
        contenedor.verificar_completo = Mock()(return_value = None)
        contenedor.cargar_mercaderia(mercaderia_mock, verificar_restricciones_mercaderia)    

        assert len(contenedor.get_mercaderias()) == 1
        mercaderia = contenedor.get_mercaderias()[0]
        assert mercaderia_mock.__eq__(mercaderia)
        
        self.assertEqual(contenedor.get_peso_ocupado(), mercaderia_mock.get_peso())
        self.assertEqual(contenedor.get_volumen_ocupado(), mercaderia_mock.devolver_volumen())
        
        
    
    def test_cuando_peso_ocupado_es_igual_a_peso_max_entonces_contenedor_esta_completo(self):
        builder_basico = BuilderBasico()
        director = Director()
        director.builder = builder_basico
        contenedor = director.crear_contenedor_basico(132, False)
        contenedor.set_peso_ocupado(24000)
        peso_ocupado = contenedor.get_peso_ocupado()
        peso_maximo = contenedor.get_peso_max()
        self.assertEqual(peso_ocupado, peso_maximo) 

    def test_cuando_volumen_ocupado_es_igual_a_volumen_max_entonces_contenedor_esta_completo(self):
        builder_basico = BuilderBasico()
        director = Director()
        director.builder = builder_basico
        contenedor = director.crear_contenedor_basico(132, False)
        contenedor.set_volumen_ocupado(32.42999999999999)
        volumen_ocupado = contenedor.get_volumen_ocupado()
        volumen_maximo = contenedor.get_volumen()
        self.assertEqual(volumen_ocupado, volumen_maximo) 

    
    def test_cuando_peso_o_volumen_ocupado_es_igual_a_peso_o_volumen_max_entonces_contenedor_esta_completo(self):
        builder_basico = BuilderBasico()
        director = Director()
        director.builder = builder_basico
        contenedor = director.crear_contenedor_basico(132, False)
        contenedor.set_volumen_ocupado(32.42999999999999)
        contenedor.set_peso_ocupado(24000)
        contenedor.verificar_completo()
        self.assertTrue(contenedor.esta_completo())

    def  test_cuando_peso_o_volumen_ocupado_es_distinto_a_peso_o_volumen_max_entonces_contenedor_no_esta_completo(self):
        contenedor = Basico(123, False)
        contenedor.set_volumen_ocupado(377)
        contenedor.set_peso_ocupado(240)
        contenedor.verificar_completo()
        self.assertFalse(contenedor.esta_completo())

    def test_dado_contenedor_esta_completo_cuando_tengo_unica_mercaderia_entonces_es_contenedor_completo_unica_carga(self):
        contenedor = Basico(123, False)
        contenedor._completo = True
        contenedor._mercaderias = []
        mercaderia = Mercaderia(False, 1, 1, 15, 1, 132)
        contenedor._mercaderias.append(mercaderia)
        resultado = contenedor.esta_completo_con_unica_carga()
        assert resultado


    def test_dado_contenedor_esta_completo_cuando_no_tenga_unica_mercaderia_entonces_no_es_contenedor_completo_unica_carga(self):
        contenedor = Basico(123, False)
        contenedor._completo = True
        contenedor._mercaderias = []
        mercaderia_1 = Mercaderia(False, 2, 2.3,2 ,1, 235)
        contenedor._mercaderias.append(mercaderia_1)
        mercaderia_2 = Mercaderia(False, 1, 1, 14,1, 454)
        contenedor._mercaderias.append(mercaderia_2)
        resultado = contenedor.esta_completo_con_unica_carga()
        assert not resultado
    
 
    