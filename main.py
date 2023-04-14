lado1 = int(input('digite um numero para um lado do triangulo: ')) 
lado2 = int(input('digite outro numero para o outro lado do triangulo: '))
lado3 = int(input('digite o ultimo numero do ultimo lado do triangulo: '))

if(lado1 + lado2) <= lado3  :
    print('o triangulo não pode existir')
elif(lado1 + lado3) <= lado2  :
    print('o triangulo não pode existir')
elif(lado3 + lado2) <= lado1  :
    print('o triangulo não pode existir')

elif(lado1 == lado2 == lado3 ) :
    print('Equilátero')
elif(lado1 != lado2 != lado3 ) :
    print('Escaleno')
elif(lado1 == lado2 != lado3 ) or (lado1 != lado2 == lado3 ):
    print('Isóceles')
