from unittest import TestCase
from unittest.mock import Mock

from Empresa.Empresa import Empresa

class EmpresaTest(TestCase):
    def test_dado_el_id_contenedor_cuando_no_se_encuentra_en_contenedores_entonces_es_none(self):
        contenedor_a = Mock()
        contenedor_a._id = 123
        contenedor_a.get_id.return_value = 123

        contenedor_b = Mock()
        contenedor_b.get_id.return_value = 456       
        contenedores = [contenedor_a, contenedor_b]
        barcos = []
        empresa = Empresa(barcos,contenedores)
        resultado = empresa.buscar_contenedor_por_id(789)
        self.assertIsNone(resultado, "El resultado deberia ser None")


    def test_dado_el_id_contenedor_cuando_esta_presente_en_contenedores_entonces_devuelve_contenedor(self):
        contenedor_a = Mock()
        contenedor_a.get_id.return_value = 123
        contenedor_b = Mock()
        contenedor_b.get_id.return_value = 456
        contenedores = [contenedor_a, contenedor_b]
        barcos = []
        empresa = Empresa(barcos,contenedores)
        contenedor_buscado = empresa.buscar_contenedor_por_id(456)
        self.assertIsNotNone(contenedor_buscado, "El resultado deberia ser Distinto None")
        self.assertEqual(contenedor_buscado, contenedor_b)

    def test_dado_mapa_vacio_cuando_no_obtengo_cantidad_viajes_por_contenedor_entonces_agrego_cantidad_viajes_al_mapa(self):
        contenedor_a = Mock()
        contenedor_a.get_id.return_value = 123
        id_contenedor_a_cantidad_viajes = {}
        barcos = []
        contenedores = []
        empresa = Empresa(barcos,contenedores)
        empresa.aumentar_contador_viajes_contenedor(id_contenedor_a_cantidad_viajes, contenedor_a)
        self.assertEqual(id_contenedor_a_cantidad_viajes[123], 1, "El contador de viajes del contenedor no aumento de la forma deseada" )
    

    def test_dado_mapa_no_vacio_cuando_obtengo_cantidad_viajes_por_contenedor_entonces_aumento_cantidad_viajes(self):
        contenedor_a = Mock()
        contenedor_a.get_id.return_value = 123
        id_contenedor_a_cantidad_viajes = {123:3}
        barcos = []
        contenedores = []
        empresa = Empresa(barcos,contenedores)
        empresa.aumentar_contador_viajes_contenedor(id_contenedor_a_cantidad_viajes, contenedor_a)
        self.assertEqual(id_contenedor_a_cantidad_viajes[123], 4, "El contador de viajes del contenedor no aumento de la forma deseada" )
    

    def test_dado_un_mapa_con_contador_en_cero_cuando_contenedor_esta_completo_con_unica_carga_entonces_verifico_que_aumento_contador(self):
        viaje = Mock()
        barco = Mock()
        contenedor = Mock()
        viaje.get_barco.return_value = barco
        barco.get_contenedores.return_value = [contenedor]
        contenedor.get_id.return_value = 123
        contenedor.esta_completo_con_unica_carga.return_value = True
        id_contenedor_a_cantidad_viajes = {123:0}
        barcos  = []
        contenedores =  []
        empresa = Empresa(barcos, contenedores)
        empresa.actualizar_cantidad_viajes_contenedor(viaje, id_contenedor_a_cantidad_viajes)
        self.assertEqual(id_contenedor_a_cantidad_viajes[123], 1, "El contador no aumento" )
        
    
    def test_dado_un_viaje_finalizado_cuando_busco_contenedor_con_mayor_cantidad_viajes_con_unica_carga_entonces_obtengo_contenedor_de_viaje(self):
        viaje = Mock()
        contenedor = Mock()
        contenedor.get_id.return_value = 123
        viaje.get_estado.return_value = "FINALIZADO"
        barcos = []
        contenedores = [contenedor]
        empresa = Empresa(barcos, contenedores)
        empresa.actualizar_cantidad_viajes_contenedor = Mock(return_value = {123:1})
        empresa.agregar_viaje(viaje)
        contenedor_buscado = empresa.obtener_contenedor_mayor_cantidad_viajes_completo_unica_carga()
        self.assertIsNotNone(contenedor_buscado)
        self.assertEqual(contenedor_buscado, contenedor)

    
    def test_obtener_barco_con_mayor_cantidad_km_recorridos(self):
        # Creo una instancia de Empresa y algunos objetos necesarios para el test
        viaje1 = Mock()
        viaje2 = Mock()
        barco1 = Mock()
        barco2 = Mock()
        gps1 = Mock()
        gps2 = Mock()

        
        # Configuro los mocks necesarios para el test
        viaje1.get_barco.return_value = barco1
        viaje2.get_barco.return_value = barco2
        barco1.get_gps.return_value = gps1
        barco2.get_gps.return_value = gps2
        gps1.obtener_distancia.return_value = 100
        gps2.obtener_distancia.return_value = 200

        # Configuro el valor de barco.get_id() para cada mock de barco
        barco1.get_id.return_value = 1 # Configura el valor de get_id() para barco1
        barco2.get_id.return_value = 2 # Configura el valor de get_id() para barco2

        empresa = Empresa([barco1, barco2], [])

        # Agrego los viajes a la lista de viajes de la empresa
        empresa.agregar_viaje(viaje1)
        empresa.agregar_viaje(viaje2)

        # Ejecuto la funcion a testear
        resultado = empresa.obtener_barco_con_mayor_cantidad_km_recorridos()

        # Verifico que la funcion haya retornado el resultado esperado
        self.assertEqual(resultado, barco2)

        # Verifico que se hayan llamado correctamente los metodos de los mocks
        viaje1.get_barco.assert_called_once()
        viaje2.get_barco.assert_called_once()
        barco1.get_gps.assert_called_once()
        barco2.get_gps.assert_called_once()
        gps1.obtener_distancia.assert_called_once()
        gps2.obtener_distancia.assert_called_once()


    def test_obtener_barco_con_menor_cantidad_km_recorridos(self):
        # Creo una instancia de Empresa y algunos objetos necesarios para el test
        viaje1 = Mock()
        viaje2 = Mock()
        barco1 = Mock()
        barco2 = Mock()
        gps1 = Mock()
        gps2 = Mock()

        
        # Configuro los mocks necesarios para el test
        viaje1.get_barco.return_value = barco1
        viaje2.get_barco.return_value = barco2
        barco1.get_gps.return_value = gps1
        barco2.get_gps.return_value = gps2
        gps1.obtener_distancia.return_value = 100
        gps2.obtener_distancia.return_value = 200

        # Configuro el valor de barco.get_id() para cada mock de barco
        barco1.get_id.return_value = 1 # Configura el valor de get_id() para barco1
        barco2.get_id.return_value = 2 # Configura el valor de get_id() para barco2

        empresa = Empresa([barco1, barco2], [])

        # Agrego los viajes a la lista de viajes de la empresa
        empresa.agregar_viaje(viaje1)
        empresa.agregar_viaje(viaje2)

        # Ejecuto la funcion a testear
        resultado = empresa.obtener_barco_con_menor_cantidad_km_recorridos()

        # Verifico que la funcion haya retornado el resultado esperado
        self.assertEqual(resultado, barco1)

        # Verifico que se hayan llamado correctamente los metodos de los mocks
        viaje1.get_barco.assert_called_once()
        viaje2.get_barco.assert_called_once()
        barco1.get_gps.assert_called_once()
        barco2.get_gps.assert_called_once()
        gps1.obtener_distancia.assert_called_once()
        gps2.obtener_distancia.assert_called_once()
