import math #Importa modulo de la librería math incorporada en Python.

#Define función que calculará la potencia del número
def power_of_number():
    #Asigna número a variable para calcular potencia
    y = 81
    #Define variable que guarda el resultado del calculo de la potencia
    power_of_y = math.pow(y, 2)
    #Imprime power_of_y (potencia de variable "y" al cuadrado)
    print(power_of_y)


#Añade convención
if __name__ == "__main__":
    power_of_number()