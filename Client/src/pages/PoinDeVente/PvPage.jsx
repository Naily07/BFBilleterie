import { Flex, Box, Center, Text, theme} from "@chakra-ui/react"
import ListPdv from "./component/listPdv"
import AboutPdv from "./component/aboutPdv"
import ModalCreatePdv from "./component/modalPdv"
import Layout from "./layout"
export default function PointDeVente(){
    return(
        <Layout>
            <Child/>
        </Layout>
    )
}

function Child(){
    return(
        <Box m={"20px 80px 0px 80px"} borderRadius={"2.5 rem"} >
                {/* <Text>Créer un point de vente</Text> */}
                <ModalCreatePdv />
            <Center 
                flexWrap={{base:"wrap", sm: "wrap", md:'wrap', lg : "nowrap", xl :"nowrap", "2xl":"nowrap"}} 
                flexDir={{base : 'row'}}
                justifyContent={"center"}
                gap={2}
            >
                <ListPdv />
                <AboutPdv />
            </Center >
        </Box>   
    )
}