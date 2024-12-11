import json

# Cargar el archivo GeoJSON
input_file = "indie.geojson"
output_file = "indie_fixed.geojson"

# Leer el archivo de entrada
with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Recorrer cada feature para corregir la geometría
for feature in data.get("features", []):
    if feature["geometry"] is None and "Geometría en GeoJSON" in feature["properties"]:
        # Mover la geometría de las propiedades al campo geometry
        feature["geometry"] = feature["properties"].pop("Geometría en GeoJSON")

# Guardar el archivo corregido
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Archivo corregido guardado en: {output_file}")
