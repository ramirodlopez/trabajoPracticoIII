

def main():

    num = int(input("Numero: "))
   

    primero = num // 10000

    print({primero})

    quinto = num % 10

    print({quinto})

    if primero == quinto:
        print('es capicua')
    else:
        print('no es capicua')


    


if __name__ == '__main__':
    main()