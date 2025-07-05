from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def obtener_coordenadas(ciudad):
    try:
        geolocator = Nominatim(user_agent="mi_examen_dry7122")
        location = geolocator.geocode(ciudad)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except GeocoderTimedOut:
        print("Tiempo de espera excedido al buscar la ciudad.")
        return None


def calcular_duracion(dist_km, medio):
    velocidades = {
        "auto": 80,
        "avión": 800,
        "bus": 60,
        "tren": 100
    }
    return dist_km / velocidades.get(medio, 60)

def main():
    print("=== Calculadora de distancia entre ciudades (Chile ↔ Argentina) ===\n")
    
    while True:
        origen = input("Ingrese ciudad de origen en Chile (o 's' para salir): ")
        if origen.lower() == 's':
            break

        destino = input("Ingrese ciudad de destino en Argentina: ")
        medio = input("Seleccione medio de transporte (auto, avión, bus, tren): ").lower()

        coord_origen = obtener_coordenadas(origen + ", Chile")
        coord_destino = obtener_coordenadas(destino + ", Argentina")

        if not coord_origen or not coord_destino:
            print("Error al encontrar coordenadas. Intente nuevamente.")
            continue

        distancia_km = geodesic(coord_origen, coord_destino).kilometers
        distancia_mi = distancia_km * 0.621371
        duracion = calcular_duracion(distancia_km, medio)

        print(f"\n Desde {origen} (Chile) hasta {destino} (Argentina):")
        print(f"Distancia: {distancia_km:.2f} km | {distancia_mi:.2f} millas")
        print(f"Tiempo estimado en {medio}: {duracion:.2f} horas")
        print(f"Narrativa: Viajando desde {origen} hasta {destino} en {medio}, recorrerás aproximadamente {int(distancia_km)} km cruzando la cordillera y conectando ambos países.\n")

if __name__ == "__main__":
    main()
