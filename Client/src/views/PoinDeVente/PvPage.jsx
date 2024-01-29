import { Flex, Box, Center} from "@chakra-ui/react"
import ListPdv from "./component/listPdv"
import AboutPdv from "./component/aboutPdv"
import ModalCreatePdv from "./component/modalPdv"
export default function PointDeVente(){
    
    return(
        <Box>
            <Center>
                <ModalCreatePdv />
            </Center>
            <Flex m={20} >
                <ListPdv />
                <AboutPdv />
            </Flex>
        </Box>
    )
}