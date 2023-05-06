class Pedido:

   def restoCon(self, number):
        resto = number % 100

        cant_cien_kilos = 0

        if resto == 0:
            cant_cien_kilos = number // 100  # 300 // 100 = 3; 3*1000
        else:
            cant_cien_kilos = number // 100 + 1  # 469 // 100 = 4 + 1

        return cant_cien_kilos