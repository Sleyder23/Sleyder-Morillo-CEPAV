import sys
import time
import openpyxl
import random 

def imprimir_lento(texto, velocidad=0.03):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

def obtener_datos_excel():
    try:
        juego_excel = openpyxl.load_workbook('juego.xlsx')
        hoja = juego_excel.active
        salud = hoja['B2'].value
        hambre = hoja['C2'].value
        dia = hoja['D2'].value
        return salud, hambre, dia, juego_excel
    except Exception as e:
        imprimir_lento(f"Error al obtener datos del archivo Excel: {e}")
        imprimir_lento("Iniciando nueva partida....")
        # Si falla, devolvemos un Excel nuevo en blanco para poder guardar más tarde
        return 100, 100, 1, openpyxl.Workbook() 

salud, hambre, dia, juego_excel = obtener_datos_excel()

imprimir_lento("BIENVENIDO A SUPERVIVENCIA EN LA JUNGLA.", 0.05)
time.sleep(1)

while salud > 0:
    print("\n" + "=" * 50)
    imprimir_lento(f" ---------- DIA {dia} ----------", 0.05)
    imprimir_lento(f"Salud: {salud}/100 | Hambre: {hambre}/100")
    print("=" * 50)

    # Todo lo de abajo ahora tiene un "Tab" (4 espacios) a la izquierda 
    # para indicarle a Python que pertenece al bucle while.
    imprimir_lento("OPCIONES:")
    imprimir_lento("1. Buscar comida (Gasta 20 salud, recupera 30 hambre)")
    imprimir_lento("2. Descansar (Recupera 20 salud, gasta 30 hambre)")
    imprimir_lento("3. Explorar (??? Evento Aleatorio ??? - |ALTO RIESGO|)")
    imprimir_lento("4. Guardar y salir del juego")

    opcion = input("Elige una opción (1-4): ")

    print("-" * 30)

    if opcion == "1":
        imprimir_lento("Buscaste en la jungla y encontraste un poco de comida...")
        salud -= 20
        hambre += 30
        dia += 1

    elif opcion == "2":
        imprimir_lento("Armaste un refugio TEMPORAL, decidiste descansar y recuperar energías...")
        salud += 20
        hambre -= 30
        dia += 1

    elif opcion == "3":
        imprimir_lento("Decidiste explorar la jungla, pero no sabes lo que te espera...")
        time.sleep(1)
        suerte = random.randint(1, 3)

        if suerte == 1:
            imprimir_lento("¡Te encontraste con una pantera y te atacó! Lograste escapar pero estas MALHERIDO")
            salud -= 50
            hambre -= 10

        elif suerte == 2:
            imprimir_lento("¡Encontraste un bolso tirado con algunas provisiones y comida!")
            salud += 50

        else:
            imprimir_lento("¡NO ENCONTRASTE NADA UTIL ||HAS PERDIDO ENERGÍA Y TIEMPO!||")
            salud -= 10
            hambre -= 20
        dia += 1

    elif opcion == "4":
        try:
            imprimir_lento("Guardando partida...")
            hoja = juego_excel.active
            hoja['B2'] = salud
            hoja['C2'] = hambre
            hoja['D2'] = dia
            juego_excel.save('juego.xlsx')
            imprimir_lento("Partida guardada. ¡Hasta la próxima!")
            break # Termina el bucle y cierra el juego limpiamente
        except Exception as e:
            imprimir_lento(f"Error al guardar datos en el archivo Excel: {e}")
            imprimir_lento("La partida no pudo guardarse.")
            break 
    else:
        imprimir_lento("Opción inválida. Por favor, elige una opción válida (1-4).")

    # === LÍMITES Y CONSECUENCIAS ===
    if salud > 100:
        salud = 100     

    if hambre > 100:
        hambre = 100

    if hambre <= 0: # Cambiado de < 0 a <= 0 para que aplique exactamente al llegar a cero
        hambre = 0  
        imprimir_lento("¡Te estás muriendo de hambre! Debes buscar comida urgentemente.")
        salud -= 20

    if salud <= 0:
        imprimir_lento("¡Has muerto! Tu salud ha llegado a 0.")
        imprimir_lento("Fin de la partida.")
        break