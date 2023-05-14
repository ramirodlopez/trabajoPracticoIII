'''from unittest import TestCase
from contenedor.basico import Basico
from mercaderia.mercaderia import Mercaderia

class ContainerTest(TestCase):
    def test_dado_contenedor_esta_completo_cuando_tengo_unica_mercaderia_entonces_es_contenedor_completo_unica_carga(self):
        container = Basico(123, False)
        container._completo = True
        container._mercaderias = []
        mercaderia = Mercaderia(False, 1, 1, 15, 1)
        container._mercaderias.append(mercaderia)
        resultado = container.esta_completo_con_unica_carga()
        assert resultado == True

    def test_dado_contenedor_esta_completo_cuando_no_tenga_unica_mercaderia_entonces_no_es_contenedor_completo_unica_carga(self):
        container = Basico(123, False)
        container._completo = True
        container._mercaderias = []
        mercaderia_1 = Mercaderia(False, 2, 2.3,2 ,1)
        container._mercaderias.append(mercaderia_1)
        mercaderia_2 = Mercaderia(False, 1, 1, 14,1)
        container._mercaderias.append(mercaderia_2)
        resultado = container.esta_completo_con_unica_carga()
        assert resultado == False'''