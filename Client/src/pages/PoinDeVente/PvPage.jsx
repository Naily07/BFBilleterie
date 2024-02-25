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
        <Box m={"20px 80px 80px 80px"} borderRadius={"2.5 rem"} >
                {/* <Text>Créer un point de vente</Text> */}
                <ModalCreatePdv />
            <Flex >
                <ListPdv />
                <AboutPdv />
            </Flex>
        </Box>   
    )
}