import requests

# URL de la API

def obtenerFrases():    
    url = 'https://zenquotes.io/api/quotes'  # Reemplaza con la URL real
# Hacer la petición GET
    response = requests.get(url)
# Verificar el estado

    if response.status_code == 200:
       data = response.json()
       frases = [item["q"] for item in data]
       return frases
    else:
        print("Error:", response.status_code)
        return []
       
