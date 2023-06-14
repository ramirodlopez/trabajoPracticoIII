from unittest import TestCase
from Barco.Basico import Basico
from Barco.Avanzado import Avanzado
from Contenedor.BasicoHC import BasicoHC
from Contenedor.flat_rack import FlatRack
from excepcion.restriccion_excepcion import RestriccionException
from Gps.Gps import Gps

class Test_Barco(TestCase):

    def test_verificar_atributos_barco(self):
        gps = Gps()

        barco = Basico(1, 10, 5000, gps)

        self.assertEqual(barco._id, 1)
        self.assertEqual(barco._cant_max_cont, 10)
        self.assertEqual(barco._peso_max_sopor, 5000)
        self.assertEqual(barco._contenedores, set())
        self.assertEqual(barco._peso_total, 0)
        self.assertEqual(barco._gps, gps)


    def test_verificar_peso_total_sea_igual_al_peso_ocupado_del_contenedor(self):
        barco = Avanzado(1, 10, 10000, None)

        contenedor1 = BasicoHC(1, False)
        contenedor2 = BasicoHC(2, False)
        contenedor3 = BasicoHC(3, False)

        contenedor1.set_peso_ocupado(5000)
        barco.calcular_peso_cargado(contenedor1)
        assert barco.get_peso_total() == 5000

        contenedor2.set_peso_ocupado(2500)
        barco.calcular_peso_cargado(contenedor2)
        assert barco.get_peso_total() == 7500

        contenedor3.set_peso_ocupado(3500)
        barco.calcular_peso_cargado(contenedor3)
        assert barco.get_peso_total() == 11000


    def test_verificar_si_el_barco_tiene_contenedores_o_no(self):
        barco = Basico(1, 10, 5000, None)
        contenedor1 = BasicoHC(1, False)
        contenedor2 = BasicoHC(2, False)
        contenedor3 = BasicoHC(3, False)

        assert barco.contar_contenedores() == 0

        contenedor1.set_peso_ocupado(1000)
        contenedor1.set_ancho_exterior(2.45)
        contenedor1.set_alto_exterior(2.6)
        contenedor1.set_largo_exterior(6.1)
        barco.agregar_contenedor(contenedor1)
        assert barco.contar_contenedores() == 1

        contenedor2.set_peso_ocupado(1000)
        contenedor2.set_ancho_exterior(2.45)
        contenedor2.set_alto_exterior(2.6)
        contenedor2.set_largo_exterior(6.1)
        barco.agregar_contenedor(contenedor2)
        assert barco.contar_contenedores() == 2

        contenedor3.set_peso_ocupado(1000)
        contenedor3.set_ancho_exterior(2.45)
        contenedor3.set_alto_exterior(2.6)
        contenedor3.set_largo_exterior(6.1)
        barco.agregar_contenedor(contenedor3)
        assert barco.contar_contenedores() == 3

    def test_agregar_contenedor_barco_que_falla_porque_supera_la_cantidad_permitida(self):
        barco = Basico(1, 10, 2500, None)
        contenedor = BasicoHC(3, False)

        contenedor.set_peso_ocupado(3000)
        contenedor.set_ancho_exterior(2.45)
        contenedor.set_alto_exterior(2.6)
        contenedor.set_largo_exterior(6.1)

        with self.assertRaises(RestriccionException):
            barco.agregar_contenedor(contenedor)

    def test_agregar_contenedor_barco_basico_que_falla_porque_contiene_material_especial(self):
        barco = Basico(1, 10, 5000, None)
        contenedor = FlatRack(4, True)

        contenedor.set_peso_ocupado(2500)
        contenedor.set_ancho_exterior(2.45)
        contenedor.set_alto_exterior(2.6)
        contenedor.set_largo_exterior(6.1)

        with self.assertRaises(RestriccionException):
            barco.agregar_contenedor(contenedor)
