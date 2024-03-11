import requests
import json
from io import BytesIO
# URL de l'API
url = "http://127.0.0.1:7500/api/event/create-list-event/"

# Paramètres de la requête
nom = "Smatchin"
lieu = "Tana"

# Fichier à envoyer
# image = {"filename": "bloc-notes-avec-stylo-ouvert-mje7yb.jpg"}
# image_spoons = [{"filename":"bloc-notes-avec-stylo-ouvert-mje7yb.jpg"},]
# Encapsuler les données dans un objet JSON
data = {    
    "nom": nom,
    "lieu": lieu
    # 'image_sponsors' : image_spoons,
}
image_path = "C:/Users/Leo/Pictures/Pictures/NodeJs.png"
image_spons_path = ["C:/Users/Leo/Pictures/Pictures/react.png", "C:/Users/Leo/Pictures/Pictures/logos3.png" ]
files = []

# Ouvrir le fichier image et stocker les données binaires dans la mémoire
with open(image_path, 'rb') as file:
    image_data = BytesIO(file.read())
    files.append(('image', (image_path, image_data, 'image/jpeg')))

# Ouvrir les fichiers sponsors et stocker les données binaires dans la mémoire
for i, path in enumerate(image_spons_path):
    with open(path, 'rb') as fileSponsors:
        key = f"sponsor_image"
        sponsor_data = BytesIO(fileSponsors.read())
        files.append((key, (path, sponsor_data, 'image/jpeg')))

# Formater la requête
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMDYwMjI2LCJpYXQiOjE3MTAwNTkzMjYsImp0aSI6ImI1ZDQ0ODZlMTJlODQ5NjZhZWVmNjNhZjA0OWU4MTViIiwidXNlcl9pZCI6MywidXNlcm5hbWUiOiJhZWYiLCJlbWFpbCI6Imxlb25AZ21haWwuY28ifQ.qtVsYTafIGAw5AaiA3K9p90OdzOI0jK8GdsnisNhxg4"
Hearders = {
    "Authorization" : f"Bearer {token}"
} 
response = requests.post(url, data=data, files=files, headers = Hearders)

# Vérifier le code de statut
if response.status_code == 200 | response.status_code == 201 :
    print("Données envoyées avec succès !")
else:
    print(f"Erreur : {response.status_code} {response.json()}")