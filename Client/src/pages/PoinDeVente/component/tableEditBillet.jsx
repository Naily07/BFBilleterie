import {
    Table,
    Thead,
    Tbody,
    Tfoot,
    Tr,
    Th,
    Td,
    TableCaption,
    TableContainer,
    Input,
    Box,
    Button,
    Center,
    Text,
    theme
  } from '@chakra-ui/react'
import InputField from './NumberInput'
import { sxTableContainer, sxTd, sxTh } from '../sytle/tableau'

export default function TableEditBillet(){
    const handleSubmit = function(e){
        e.preventDefault()
        console.log("retour")
    }
   
    return(
        <Box p={"20px 20px 0px 20px"} w={"100%"}>
            <form  >
                <Center>
                    <Text mb={"20px"} as={"b"}> Ajouter des nouveaux billets</Text>
                </Center>
                <TableContainer sx={sxTableContainer} >
                    <Table >
                        <Thead >
                            <Th sx={sxTh}>Gold</Th>
                            <Th sx={sxTh}>Silver</Th>
                            <Th sx={sxTh}>Silver</Th>
                        </Thead>
                        <Tbody>
                            <Tr>
                                <Td sx={sxTd} >
                                    <InputField />
                                </Td>
                                <Td sx={sxTd}>
                                    <InputField/>
                                </Td>
                                <Td sx={sxTd}>
                                    <InputField/>
                                </Td>
                            </Tr>
                        </Tbody>
                    </Table>
                </TableContainer>
                <Center mt={"40px"}>
                    <Button type='submit' variant={"solid"} colorScheme={"blue"} onClick={handleSubmit} >Valider</Button>
                </Center>
            </form>
        </Box>
        
    )
}