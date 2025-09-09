import requests

# URL de la API
url = 'https://zenquotes.io/api/quotes'  # Reemplaza con la URL real

# Hacer la petición GET
response = requests.get(url)

# Verificar el estado
if response.status_code == 200:
    data = response.json()
    frases = [item["q"] for item in data]  # Extraer el campo "q" de cada objeto
    print(frases)
else:
    print("Error:", response.status_code)
