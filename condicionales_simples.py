print("SISTEMA PARA CALCULAR EL PROMEDIO DEL ALUMNO")
nombre = input("cual es tu nombre: ")
matematicas = int(input(nombre + "¿Cual es la calificacion de matematicas?: "))
quimicas = int(input(nombre + "¿Cual es la calificacion de quimicas?: "))
biologia = int(input(nombre + "¿Cual es la calificacion de biologia?: "))

promedio = (matematicas + quimicas + biologia) /3
promedio = int(promedio)

if promedio >= 6:
    print('FELISIDADES ' + nombre + ' "APROBASTE" con un promedio de: ',promedio)
    
    print("Fin.")
else:
     
     print('REPROBADO lo sentimos: ' + nombre + ' "REPROBADO" con un promedio de: ',promedio)
     print('REPROBADO lo sentimos: ' + nombre + ' "REPROBADO" con un promedio de: ',round(promedio))
     
print("Fin.")

    
