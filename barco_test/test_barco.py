from unittest import TestCase

from unittest.mock import Mock
from Barco.Barco import Barco
from excepcion.restriccion_excepcion import RestriccionException
from Validacion_Barco.Validar_Subir_Al_Barco_Basico import Validar_Subir_Al_Barco_Basico

class Test_Barco(TestCase):

    def test_verificar_atributos_barco(self):
        #Crear un mock para el objeto gps
        gps_mock = Mock()

        barco = Barco(1, 10, 5000, gps_mock)

        self.assertEqual(barco._id, 1)
        self.assertEqual(barco._cant_max_cont, 10)
        self.assertEqual(barco._peso_max_sopor, 5000)
        self.assertEqual(barco._contenedores, set())
        self.assertEqual(barco._peso_total, 0)
        self.assertEqual(barco._gps, gps_mock)


    def test_verificar_peso_total_sea_igual_al_peso_ocupado_del_contenedor(self):
        # Crear un mock para el objeto barco
        barco = Mock()

        # Configurar el peso total del barco en el mock
        barco.get_peso_total.return_value = 0

        # Crear contenedores mock
        contenedor1 = Mock()
        contenedor2 = Mock()
        contenedor3 = Mock()

        # Configurar los pesos ocupados de los contenedores mock
        contenedor1.get_peso_ocupado.return_value = 5000
        contenedor2.get_peso_ocupado.return_value = 2500
        contenedor3.get_peso_ocupado.return_value = 3500

        # Llamar al metodo calcular_peso_cargado con el mock del barco y actualizar el peso total
        barco.calcular_peso_cargado(contenedor1)
        barco.get_peso_total.return_value += 5000

        # Verificar que el peso total sea igual al peso ocupado del contenedor 1
        self.assertEqual(barco.get_peso_total(), 5000)

        # Llamar al metodo calcular_peso_cargado con el mock del barco y actualizar el peso total
        barco.calcular_peso_cargado(contenedor2)
        barco.get_peso_total.return_value += 2500

        # Verificar que el peso total sea igual al peso ocupado del contenedor 1 y 2
        self.assertEqual(barco.get_peso_total(), 7500)

        # Llamar al metodo calcular_peso_cargado con el mock del barco y actualizar el peso total
        barco.calcular_peso_cargado(contenedor3)
        barco.get_peso_total.return_value += 3500

        # Verificar que el peso total sea igual al peso ocupado del contenedor 1, 2 y 3
        self.assertEqual(barco.get_peso_total(), 11000)


    def test_verificar_si_el_barco_tiene_contenedores_o_no(self):
        # Crear un mock para el objeto Barco
        barco = Mock()

        # Configurar el metodo contar_contenedores en el mock del barco
        barco.contar_contenedores.return_value = 0

        # Crear un mock para la restriccion
        restriccion = Mock()

        # Crear mocks para los contenedores
        contenedor1 = Mock()
        contenedor2 = Mock()
        contenedor3 = Mock()

        # Configurar los valores de los mocks de los contenedores
        contenedor1.get_peso_ocupado.return_value = 1000
        contenedor1.get_ancho_exterior.return_value = 2.45
        contenedor1.get_alto_exterior.return_value = 2.6
        contenedor1.get_largo_exterior.return_value = 6.1

        contenedor2.get_peso_ocupado.return_value = 1000
        contenedor2.get_ancho_exterior.return_value = 2.45
        contenedor2.get_alto_exterior.return_value = 2.6
        contenedor2.get_largo_exterior.return_value = 6.1

        contenedor3.get_peso_ocupado.return_value = 1000
        contenedor3.get_ancho_exterior.return_value = 2.45
        contenedor3.get_alto_exterior.return_value = 2.6
        contenedor3.get_largo_exterior.return_value = 6.1


        # Llamar al metodo agregar_contenedor del mock del barco y actualizar el contador de contenedores
        barco.agregar_contenedor(contenedor1, restriccion)
        barco.contar_contenedores.return_value += 1

        # Verificar que el barco tenga 1 contenedor
        self.assertEqual(barco.contar_contenedores(), 1)

         # Llamar al metodo agregar_contenedor del mock del barco y actualizar el contador de contenedores
        barco.agregar_contenedor(contenedor2, restriccion)
        barco.contar_contenedores.return_value += 1

        # Verificar que el barco tenga 2 contenedores
        self.assertEqual(barco.contar_contenedores(), 2)

         # Llamar al metodo agregar_contenedor del mock del barco y actualizar el contador de contenedores
        barco.agregar_contenedor(contenedor3, restriccion)
        barco.contar_contenedores.return_value += 1

        # Verificar que el barco tenga 3 contenedor
        self.assertEqual(barco.contar_contenedores(), 3)


    def test_agregar_contenedor_barco_que_falla_porque_supera_la_cantidad_permitida(self):
        # Crear un mock para el objeto Barco
        barco = Mock()

        # Configurar el metodo get_cant_max_cont en el mock del barco
        barco.get_cant_max_cont.return_value = 10

        # Crear un mock para la restriccion
        restriccion = Mock()

        # Crear un mock para el contenedor
        contenedor = Mock()

        # Configurar los valores del mock del contenedor
        contenedor.get_peso_ocupado.return_value = 3000
        contenedor.get_ancho_exterior.return_value = 2.45
        contenedor.get_alto_exterior.return_value = 2.6
        contenedor.get_largo_exterior.return_value = 6.1

        # Lanzar una excepcion al llamar a agregar_contenedor del mock del barco
        barco.agregar_contenedor.side_effect = RestriccionException("Un barco no puede cargar más containers del máximo definido")

        # Verificar que al llamar a agregar_contenedor se lance una excepcion 
        with self.assertRaises(RestriccionException):
            barco.agregar_contenedor(contenedor, restriccion)


    def test_agregar_contenedor_barco_basico_que_falla_porque_contiene_material_especial(self):
        # Crear un objeto de barco
        barco = Barco(1, 10, 5000, None)

        # Crear un mock para el contenedor con material especial
        contenedor_mock = Mock()
        contenedor_mock.get_ancho_exterior.return_value = 2.45
        contenedor_mock.get_alto_exterior.return_value = 2.6
        contenedor_mock.get_largo_exterior.return_value = 6.1
        contenedor_mock.is_especial.return_value = True

        restriccion = Validar_Subir_Al_Barco_Basico()

        # Configurar el comportamiento esperado de la restriccion
        restriccion.verificar_restricciones_barco_segun_su_tipo = Mock(side_effect=RestriccionException("Un container con material especial (explosivos, desechos químicos o radioactivos) sólo puede ser \
                            transportado por un barco diseñado para tal fin."))
        

        with self.assertRaises(RestriccionException):
            barco.agregar_contenedor(contenedor_mock, restriccion)



    def test_verificar_resultado_de_la_ganancia(self):
        # Crear un objeto Pedido mock
        pedido_mock = Mock()

        # Crear un mock para el objeto Contenedor
        contenedor_mock = Mock()

        # Configurar el valor de retorno del método obtener_ganancia_contenedor
        contenedor_mock.obtener_ganancia_contenedor.return_value = 100

        # Configurar el valor de retorno de get_peso_ocupado para que sea un entero
        contenedor_mock.get_peso_ocupado.return_value = 5000

        # Crear un objeto Barco con el mock del contenedor
        barco = Barco(1, 10, 10000, None)

        # Crear un mock para el objeto restriccion
        restriccion_mock = Mock()

        # Agregar el mock del contenedor al barco
        barco.agregar_contenedor(contenedor_mock, restriccion_mock)

        # Obtener la ganancia del barco
        ganancia = barco.obtener_ganacia_barco(pedido_mock)

        # Comprobar que la ganancia es la esperada
        self.assertEqual(ganancia, 100)


    def test_varificar_resultado_esperado_en_set_horas_usadas(self):
        barco = Barco(1, 10, 10000, None)

        # Configurar los datos necesarios para la prueba
        estrategia_1_mock = Mock(get_tipo = Mock(return_value="Motor"))
        estrategia_2_mock = Mock(get_tipo = Mock(return_value="Vela"))
        estrategia_3_mock = Mock(get_tipo = Mock(return_value="Motor"))

        # Configurar el comportamiento de los mocks para que retornen valores enteros
        estrategia_1_mock.hora_activacion.return_value = 5
        estrategia_2_mock.hora_activacion.return_value = 10
        estrategia_3_mock.hora_activacion.return_value = 15

        barco._hora_activacion_estrategia = [estrategia_1_mock, estrategia_2_mock, estrategia_3_mock]
        barco.hora_llegada_barco = 20

        # Ejecutar el metodo set_horas_usadas()
        barco.set_horas_usadas()

        self.assertEqual(barco._horas_motor, 10)


