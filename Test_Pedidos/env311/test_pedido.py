from Pedido.Pedido import Pedido
from unittest import TestCase

class PedidoTest(TestCase):

    def test(self):
        r = Pedido()
        assert r.restoCon(550) == 6


