import random 
import difflib

while True:

 metro_caracas = {
    "Propatria": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Plaza Sucre": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Gato Negro": {"linea": "Línea 1", "transferencia": "Metrobús"},
    "Agua Salud": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Caño Amarillo": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Capitolio": {"linea": "Línea 1", "transferencia": "Línea 2 (El Silencio)"},
    "La Hoyada": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Parque Carabobo": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Bellas Artes": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Colegio De Ingenieros": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Plaza Venezuela": {"linea": "Línea 1", "transferencia": "Línea 2 / Línea 3 / Línea 4"},
    "Sabana Grande": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Chacaíto": {"linea": "Línea 1", "transferencia": "Metrobús"},
    "Chacao": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Altamira": {"linea": "Línea 1", "transferencia": "Metrobús"},
    "Miranda": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "Los Dos Caminos": {"linea": "Línea 1", "transferencia": "Metrobús"},
    "Los Cortijos": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "La California": {"linea": "Línea 1", "transferencia": "Metrobús"},
    "Petare": {"linea": "Línea 1", "transferencia": "Cabletrén / Metrobús"},
    "Palo Verde": {"linea": "Línea 1", "transferencia": "Ninguna"},
    "El Silencio": {"linea": "Línea 2", "transferencia": "Línea 1 (Capitolio)"},
    "Capuchinos": {"linea": "Línea 2", "transferencia": "Línea 4"},
    "Maternidad": {"linea": "Línea 2", "transferencia": "Ninguna"},
    "Artigas": {"linea": "Línea 2", "transferencia": "Ninguna"},
    "La Paz": {"linea": "Línea 2", "transferencia": "Metrobús"},
    "La Yaguara": {"linea": "Línea 2", "transferencia": "Ninguna"},
    "Carapita": {"linea": "Línea 2", "transferencia": "Ninguna"},
    "Antímano": {"linea": "Línea 2", "transferencia": "Ninguna"},
    "Mamera": {"linea": "Línea 2", "transferencia": "Bifurcación Zoológico / Adjuntas"},
    "Caricuao": {"linea": "Línea 2", "transferencia": "Ninguna"},
    "Zoológico": {"linea": "Línea 2", "transferencia": "Ninguna"},
    "Ruiz Pineda": {"linea": "Línea 2", "transferencia": "Ninguna"},
    "Las Adjuntas": {"linea": "Línea 2", "transferencia": "Metro Los Teques"},
    "Ciudad Universitaria": {"linea": "Línea 3", "transferencia": "Ninguna"},
    "Los Símbolos": {"linea": "Línea 3", "transferencia": "Ninguna"},
    "La Bandera": {"linea": "Línea 3", "transferencia": "Terminal de Oriente / BusCaracas"},
    "El Valle": {"linea": "Línea 3", "transferencia": "Metrobús"},
    "Los Jardines": {"linea": "Línea 3", "transferencia": "Ninguna"},
    "Coche": {"linea": "Línea 3", "transferencia": "Ninguna"},
    "Mercado": {"linea": "Línea 3", "transferencia": "Ninguna"},
    "La Rinconada": {"linea": "Línea 3", "transferencia": "Ferrocarril central (IAFE)"},
    "Zona Rental": {"linea": "Línea 4", "transferencia": "Línea 1 / Línea 3 / Línea 5"},
    "Parque Central": {"linea": "Línea 4", "transferencia": "Metrocable"},
    "Nuevo Circo": {"linea": "Línea 4", "transferencia": "Ninguna"},
    "Teatros": {"linea": "Línea 4", "transferencia": "Ninguna"},
    "Bello Monte": {"linea": "Línea 5", "transferencia": "Línea 4 (Zona Rental)"}
}


 print("=== BIENVENIDO AL ASISTENTE DE RUTA DEL METRO DE CARACAS ===")

 origen = input("¿En qué estación inicia tu viaje?: ").strip().title()
 destino = input("¿A qué estación te diriges?: ").strip().title()

 print("\n--- CALCULANDO RUTA ---")


 if origen in metro_caracas and destino in metro_caracas:
    
    linea_origen = metro_caracas[origen]["linea"]
    linea_destino = metro_caracas[destino]["linea"]
    
    print(f"📍 Origen: {origen} ({linea_origen})")
    print(f"🏁 Destino: {destino} ({linea_destino})")
    
    
    if linea_origen == linea_destino:
        print("\n✅ Tipo de viaje: DIRECTO (Permaneces en la misma línea).")
        
        tiempo_viaje = random.randint(4, 15)
    else:
        print("\n⚠️ Tipo de viaje: CON TRANSFERENCIA.")
        print(f"   Debes cambiar de la {linea_origen} a la {linea_destino}.")
        
        tiempo_viaje = random.randint(20, 45)
        
    
    print(f"⏱️  Tiempo estimado de viaje: {tiempo_viaje} minutos.")
    

    transf_origen = metro_caracas[origen]["transferencia"]
    transf_destino = metro_caracas[destino]["transferencia"]
    
    print("\n--- Información de conexiones en tus estaciones ---")
    if transf_origen != "Ninguna":
        print(f"• En tu origen ({origen}) hay transferencia disponible hacia: {transf_origen}")
    else:
        print(f"• Tu origen ({origen}) no cuenta con transferencias a otros sistemas externos.")
        
    if transf_destino != "Ninguna":
        print(f"• En tu destino ({destino}) hay transferencia disponible hacia: {transf_destino}")

else:
    print("❌ Error: Una o ambas estaciones no existen en el sistema.")
    print("Por favor, verifica que estén bien escritas (Ej: Plaza Venezuela, La Paz, Capitolio).")
