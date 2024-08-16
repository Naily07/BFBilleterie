from django.conf import settings
import requests

def GoogleLoginGetToken(code):
    client_id = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    client_secret = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
    print("CODE", code)
    try:
        token_endpoint = 'https://oauth2.googleapis.com/token'
        token_params = {
        "code" : code,  
        "client_id":client_id,
        "client_secret":client_secret,
        "redirect_uri":"http://localhost:5173/accueil",
        "grant_type":"authorization_code"
        } 
        response = requests.post(token_endpoint, token_params)
        print("responseBack", response.json())
        return response.json()
    except Exception as e:
        return {"error": "Erreur de connexion", "details": str(e)}

def GoogleGetUserInfo(token):
    endpoint = "https://openidconnect.googleapis.com/v1/userinfo"
    print("TOKEN", token)
    hearder = {
        "Authorization" : f"Bearer {str(token)}"
    }
    userinfo = requests.get(endpoint, headers=hearder)
    print("INFO", userinfo.json())
    return userinfo.json()