
export default async  function authGoogle(){
    const res = await fetch("https://accounts.google.com/o/oauth2/v2/auth?scope=https://www.googleapis.com/auth/drive.metadata.readonly&access_type=online  redirect_uri=http://127.0.0.1:8000/api/point-de-vente/create-list-pointdevente/client_id=302579460-rni4mhlau2fodrepb2s9gtsq9qeptup2.apps.googleusercontent.com")
    const code = await res.json()
    return url
}   