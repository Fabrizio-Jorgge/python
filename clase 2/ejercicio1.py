'''
crear un programa que pida dos numeros 
y obtenga como resultado cual de ellos es par
o si ambos lo son 
# Si ambos son pares, mostrar el mensaje "Ambos números son pares"
# Si uno es par y el otro impar, mostrar "Uno es par y el otro es impar"
'''

# Solicitar dos números al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Verificar la paridad
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos números son pares")
elif (num1 % 2 == 0 and num2 % 2 != 0) or (num1 % 2 != 0 and num2 % 2 == 0):
    print("Uno es par y el otro es impar")
else:
    print("Ambos son impares")
