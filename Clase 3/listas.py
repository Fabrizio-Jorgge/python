'''
Ejemplos de listas en Python
'''

array = ["futbol", "PC", 18.6, 18, [6,7,10.4], True, False]
print(array)

#Acceso a los elementos de la lista
print(array[0])  # Acceso al primer elemento
print(array[4]) 
print(array[0:3])
print(len(array))  # Longitud de la lista
array.append(66)  # Añadir un nuevo elemento al final
print(array)
array.insert(2, "baloncesto")  # Insertar un elemento en una posición específica
print(array)
array.extend(["tenis", "natación"])  # Añadir varios elementos al final
print(array)
array.remove("PC")  # Eliminar un elemento específico
print(array)
array.pop(2)  # Eliminar el último elemento
array.clear()  # Limpiar la lista
print(array)
array = ["futbol", "PC", 18.6, 18, [6,7,10.4], True, False]
array2 = ["baloncesto", "tenis", "natación"]
array3 = array + array2  # Concatenar dos listas
print(array3)
print("fubol" in array3)
print(array3.count("natacion")) 
print(array3.index("tenis"))  # Encontrar el índice de un elemento
array4= [1,2,3,4,5,6,7,8,9,10]
array4.reverse()  # Invertir el orden de los elementos
print(array4)
array5 = [5, 3, 8, 1, 2]
array5.sort()  # Ordenar la lista
print(array5)
