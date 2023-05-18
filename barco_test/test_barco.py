from unittest import TestCase
from Barco.Basico import Basico
from Barco.Avanzado import Avanzado
from Contenedor.Contenedor import Contenedor
from excepcion.restriccion_excepcion import RestriccionException
from Gps.Gps import Gps

class Test_Barco(TestCase):

    def test_init(self):
        gps = Gps()

        barco = Basico(1, 10, 5000, gps)

        self.assertEqual(barco._id, 1)
        self.assertEqual(barco._cant_max_cont, 10)
        self.assertEqual(barco._peso_max_sopor, 5000)
        self.assertEqual(barco._contenedores, set())
        self.assertEqual(barco._peso_total, 0)
        self.assertEqual(barco._gps, gps)


    def test_calcular_peso_cargado(self):
        barco = Avanzado(1, 10, 10000, None)

        contenedor1 = Contenedor(1, 5000, 10, 1, 2, False)
        contenedor2 = Contenedor(2, 2500, 5, 2, 1, False)
        contenedor3 = Contenedor(3, 3500, 7, 3, 1, False)

        barco.calcular_peso_cargado(contenedor1)
        assert barco.get_peso_total() == 5000
        barco.calcular_peso_cargado(contenedor2)
        assert barco.get_peso_total() == 7500
        barco.calcular_peso_cargado(contenedor3)
        assert barco.get_peso_total() == 11000


    def test_contar_contenedores(self):
        barco = Basico(1, 10, 5000, None)
        contenedor1 = Contenedor(1, 1000, 2.45, 2.6, 6.1, False)
        contenedor2 = Contenedor(2, 1500, 2.45, 2.6, 6.1, False)
        contenedor3 = Contenedor(3, 2000, 2.45, 2.6, 6.1, False)

        assert barco.contar_contenedores() == 0

        barco.agregar_contenedor(contenedor1)
        assert barco.contar_contenedores() == 1

        barco.agregar_contenedor(contenedor2)
        assert barco.contar_contenedores() == 2

        barco.agregar_contenedor(contenedor3)
        assert barco.contar_contenedores() == 3


    def test_es_basico(self):
        barco = Basico(1, 10, 5000, None)

        # Crea un contenedor con dimensiones validas
        contenedor1 = Contenedor(1, 1000, 2.45, 2.6, 6.1, False)

        # Crea un contenedor con dimensiones invalidas
        contenedor2 = Contenedor(2, 1500, 2.46, 2.7, 6.2, False)

        # Verifica que el contenedor que sea basico para la validacion
        assert barco.es_basico(contenedor1) == True

        # Verifica que el contenedor que no sea basico (avanzado) no pase la validacion
        assert barco.es_basico(contenedor2) == False

    def test_agregar_contenedor(self):
        barco = Basico(1, 10, 5000, None)

        contenedor1 = Contenedor(1, 1000, 2.45, 2.6, 6.1, False)
        contenedor2 = Contenedor(2, 1500, 2.45, 2.6, 6.1, False)
        contenedor3 = Contenedor(3, 3000, 2.45, 2.6, 6.1, False)
        contenedor4 = Contenedor(4, 2500, 2.45, 2.6, 6.1, True)

        # Agrega el primer contenedor que deberia ser exitoso
        barco.calcular_peso_cargado(contenedor1)
        barco.agregar_contenedor(contenedor1)
        assert barco.contar_contenedores() == 1

        # Agrega el segundo contenedor que tambien deberia ser exitoso
        barco.calcular_peso_cargado(contenedor2)
        barco.agregar_contenedor(contenedor2)
        assert barco.contar_contenedores() == 2

        #Agrega el tercer contenedor que deberia fallar, ya que supera la cantidad permitida
        barco.calcular_peso_cargado(contenedor3)
        with self.assertRaises(RestriccionException):
            contenedor3.verificar_restricciones_barco_basico(barco)


        # Agrega el cuarto contenedor q deberia fallar, ya que contiene material especial y no se permite
        barco.calcular_peso_cargado(contenedor4)
        with self.assertRaises(RestriccionException):
            contenedor4.verificar_restricciones_barco_basico(barco)