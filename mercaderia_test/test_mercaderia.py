from unittest import TestCase
from unittest.mock import Mock

from Mercaderia.Mercaderia import Mercaderia


class MercaderiaTest(TestCase):
    def test_cuando_se_obtiene_ganancia_de_mercaderia_entonces_se_retorna_la_ganancia_correcta(self):
        mercaderia = Mercaderia(1, 1, 15, 1, 132, None)
        pedido = Mock()
        ganancia_pedido = pedido.obtener_ganancia_pedido.return_value = 50
        ganancia = mercaderia.obtener_ganancia_mercaderia(123, pedido)
        self.assertEqual(ganancia, ganancia_pedido)