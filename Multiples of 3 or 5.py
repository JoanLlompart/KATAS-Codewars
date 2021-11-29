#Si enumeramos todos los números naturales por debajo de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es de 23.

#termine la solución para que devuelva la suma de todos los múltiplos de 3 o 5 por debajo del número pasado. Además, si el número es negativo, devuelva 0 (para los idiomas que los tienen).

#def solution(number):


    #for multiple in number
number = int(input('escribe aqui el numero'))

def solution(number):
    total_sum = 0
    for multiple in range(1, number):
        if (multiple%3 == 0 or multiple%5 == 0):
            total_sum = total_sum+multiple
    return total_sum