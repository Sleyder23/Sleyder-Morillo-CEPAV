import time

# Función reutilizable para imprimir texto lento
def imprimir_lento(texto, velocidad=0.03):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print()

# Datos iniciales
TOTAL_LOSAS = 66
PRECIO_LOSA = 15
COSTO_METRO_PISCINA = 20  # Costo estimado de $20 por metro cuadrado de piscina

# Bienvenida (se muestra solo una vez al arrancar)
imprimir_lento("===Bienvenido al pueblo La Balkara=== ===Este es tu sistema de gestion de calculos para asfaltar el pueblo===")
print()


while True:
    
    menu = (
        "=== OPCIONES DE ASFALTADO ===\n"
        "1. Asfaltar con 23 losas (Opción más barata)\n"
        "2. Asfaltar con 26 losas\n"
        "3. Asfaltar con 27 losas\n"
        "4. Asfaltar con 28 losas (Opción más cara)\n"
        "5. Salir del sistema\n"
    )

    imprimir_lento(menu)
    opcion = input("Por favor, selecciona una opción (1-5): ")
    print()

    
    if opcion == "5":
        imprimir_lento("Gracias por usar el sistema de gestión de La Balkara. ¡Hasta pronto!")
        break

    
    if opcion == "1":
        losas_usadas = 23
        advertencia = "ADVERTENCIA: Esta es la opción más económica, pero cubre la menor cantidad de superficie."
        consecuencia = "CONSECUENCIA: Usted ahorrará mas dinero, pero algunas calles o tramos secundarios quedarán sin asfaltar."

    elif opcion == "2":
        losas_usadas = 26
        advertencia = "ADVERTENCIA: Cobertura moderada para las vías principales."
        consecuencia = "CONSECUENCIA: Se asfaltarán los accesos clave, pero la durabilidad en zonas de alto tráfico podría ser limitada a largo plazo."

    elif opcion == "3":
        losas_usadas = 27
        advertencia = "ADVERTENCIA: Cobertura alta con buena distribución de material."
        consecuencia = "CONSECUENCIA: Gran parte del pueblo quedará pavimentado, dejando un margen razonable de material de repuesto en inventario."

    elif opcion == "4":
        losas_usadas = 28
        advertencia = "ADVERTENCIA: Esta es la opción con el mayor costo del catálogo."
        consecuencia = "CONSECUENCIA: Maximiza la superficie asfaltada y la calidad de las calles, pero reduce al mínimo tu presupuesto y material sobrante."

    else:
        imprimir_lento("Opción inválida. Por favor, elige un número del 1 al 5.")
        print()
        continue 

    
    costo_total = losas_usadas * PRECIO_LOSA
    sobrantes = TOTAL_LOSAS - losas_usadas
    dinero_sobrante = sobrantes * PRECIO_LOSA
    metros_piscina = dinero_sobrante // COSTO_METRO_PISCINA  
    costo_mas_cara = 28 * PRECIO_LOSA
    ahorro_vs_maxima = costo_mas_cara - costo_total

    imprimir_lento("--- RESUMEN DEL ASFALTADO ---")
    imprimir_lento(f"Losas a utilizar: {losas_usadas}")
    imprimir_lento(f"Costo total del proyecto: ${costo_total}")
    imprimir_lento(f"Losas que te sobran: {sobrantes} de {TOTAL_LOSAS}")
    imprimir_lento(f"Valor en dinero de las losas sobrantes: ${dinero_sobrante}")
    imprimir_lento(f"Ahorro respecto a la opción más cara (28 losas): ${ahorro_vs_maxima}")
    print()
    
    imprimir_lento(f"⚠️  {advertencia}")
    imprimir_lento(f"📌 {consecuencia}")
    print()
    imprimir_lento(f"🏊 PROYECTO EXTRA: Con los ${dinero_sobrante} que te sobran, te alcanzará para construir una piscina en el patio de tu casa de aprox. {metros_piscina} m².")
    print()


    confirmaciones = 0
    
    while confirmaciones < 2:
        confirmar = input(f"¿Estás seguro de esta elección? (Confirmación {confirmaciones + 1} de 2) [Escribe 's' para confirmar o 'n' para rechazar]: ").strip().lower()
        print()
        
        if confirmar == 's':
            confirmaciones += 1
            if confirmaciones == 1:
                imprimir_lento("✔️ ¡Primera confirmación registrada! Te falta una más para validar la decisión final.")
        else:
            imprimir_lento("❌ Has rechazado o escrito otra cosa. Se cancela el proceso y regresas al menú principal.")
            confirmaciones = 0  
            break               

    
    if confirmaciones == 2:
        imprimir_lento("🎉 ¡Has confirmado 2 veces tu decisión final con éxito! El sistema procesará tu elección y se cerrará.")
        break

    print("=" * 50)
    print()