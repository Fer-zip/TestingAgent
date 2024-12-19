import requests

API_URL = "https://replikers-922839482240.us-central1.run.app/query"  # Reemplaza <tu-url-cloud-run> con tu URL pública

def consumir_api(input_text):
    try:
        payload = {"input_text": input_text}
        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 200:
            print("Respuesta de la API:", response.text)  # Mostramos el texto sin intentar convertirlo
        else:
            print("Error en la API:", response.text)

    except Exception as e:
        print(f"Error: {e}")

# Llamada de ejemplo
if __name__ == "__main__":
    input_text = "hola"
    consumir_api(input_text)