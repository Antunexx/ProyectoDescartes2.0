import folium

# Crear mapa centrado en Córdoba
m = folium.Map(location=[-31.4173, -64.1830], zoom_start=12)

# 🔵 Línea A (Subte Este-Oeste) - (Modificada)
subte_a = [
    (-31.4242, -64.1220),  # INFINITO OPEN
    (-31.4250, -64.1632),  # San Vicente
    (-31.4173, -64.1830),  # Plaza San Martín (Centro) 🔄 Conexión con Línea B
    (-31.4260, -64.1875),  # Nueva Córdoba
    (-31.4390, -64.1895),  # Ciudad Universitaria
    (-31.4175, -64.2205),  # Estadio Kempes
    (-31.4425, -64.2115),  # Fuerza Aérea (Ruta 20)
    (-31.4596, -64.2259)   # Villa El Libertador
]
folium.PolyLine(subte_a, color="blue", weight=5, opacity=0.7, tooltip="Línea A (Este-Oeste)").add_to(m)

# 🔴 Línea B (Subte Norte-Sur) - (Modificada)
subte_b = [
    (-31.3155, -64.2083),  # Aeropuerto Pajas Blancas
    (-31.3220, -64.2438),  # Argüello
    (-31.3665, -64.2111),  # Monseñor Pablo Cabrera
    (-31.3972, -64.1878),  # Alta Córdoba
    (-31.4060, -64.1950),  # Alberdi
    (-31.4173, -64.1830),  # Plaza San Martín (Centro) 🔄 Conexión con Línea A
    (-31.4242, -64.1895),  # Terminal de Ómnibus
    (-31.4501, -64.1972),  # Barrio Aeronáutico
    (-31.4661, -64.1956)   # Av. O’Higgins y Circunvalación
]
folium.PolyLine(subte_b, color="red", weight=5, opacity=0.7, tooltip="Línea B (Norte-Sur)").add_to(m)

# 🏁 Agregar marcadores de estaciones
estaciones = {
    "INFINITO OPEN": (-31.4242, -64.1220),
    "San Vicente": (-31.4250, -64.1632),
    "Plaza San Martín (Centro)": (-31.4173, -64.1830),
    "Nueva Córdoba": (-31.4260, -64.1875),
    "Ciudad Universitaria": (-31.4390, -64.1895),
    "Estadio Kempes": (-31.4175, -64.2205),
    "Fuerza Aérea (Ruta 20)": (-31.4425, -64.2115),
    "Villa El Libertador": (-31.4596, -64.2259),
    "Aeropuerto Pajas Blancas": (-31.3155, -64.2083),
    "Argüello": (-31.3220, -64.2438),
    "Monseñor Pablo Cabrera": (-31.3665, -64.2111),
    "Alta Córdoba": (-31.3972, -64.1878),
    "Alberdi": (-31.4060, -64.1950),
    "Terminal de Ómnibus": (-31.4242, -64.1895),
    "Barrio Aeronáutico": (-31.4501, -64.1972),
    "Av. O’Higgins y Circunvalación": (-31.4661, -64.1956)
}

for nombre, coord in estaciones.items():
    folium.Marker(coord, popup=nombre, icon=folium.Icon(color="black")).add_to(m)

# Guardar mapa como archivo HTML
m.save("subte_cordoba_mejorado.html")

print("✅ Mapa generado: abre 'subte_cordoba_mejorado.html' en tu navegador.")
