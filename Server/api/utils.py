import base64
import json


def decodeToken(token):
    header, payload, signature = token.split(".")

    # Décoder la deuxième partie (payload)
    payload_bytes = base64.b64decode(payload + "===")  # Ajoute des '=' pour combler le padding
    payload_json = payload_bytes.decode("utf-8")
    # Convertir la chaîne JSON en objet

    payload_obj = json.loads(payload_json)
    
    print(payload_obj)  # Affiche l'objet JSON décodé
    return payload_obj