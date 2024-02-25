import { useEffect, useState } from "react"
import { useLocation } from "react-router-dom"
import { Box, Text, Container } from "@chakra-ui/react"
export default function Layout({children}){
    const location = useLocation()
    const [isconnecte, setConected] = useState(false)
    const [loadign, setLoading] = useState(true)
    //Traitement Erreur
    useEffect(()=>{
        const fetchData = async () => {
            const req = location.search;
            const value = new URLSearchParams(req);
            const code = value.get('code');
            if (code) {
              console.log("Code obtenu", code);
      
              try {
                console.log("Appel");
                const res = await fetch('http://127.0.0.1:8000/api/point-de-vente/login/google/', {
                  method: 'POST',
                  headers: {
                    'Content-Type': 'application/json',
                  },
                  body: JSON.stringify({ code: code }),
                })

                if(res.status == 200 || res.status == 201)
                  setConected((c)=> c = true)
                console.log(res);
                if (res.ok) {
                  const result = await res.json();
                  console.log("Résultat", result);
                } else {
                  console.error('Échec de la requête', res.status);
                }
              } catch (error) {
                console.error('Erreur lors de la requête', error);
              }
              finally{
                setLoading(false)
              }
            } else {
              console.log("Pas de code");
            }
          }
      fetchData()
    }, [location])
    if (loadign) {
      return(
        <Container>
          .........Chargement
        </Container>
      )
    } 
    return(
        <>
            {isconnecte == true ? children : ErrorLogin()}
        </>
    )
}

function ErrorLogin(){
    return(
        <>
            Login required
        </>
    )
}