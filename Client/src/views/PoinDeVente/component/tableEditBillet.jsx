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
    Center
  } from '@chakra-ui/react'
import InputField from './NumberInput'

  export default function TableEditBillet(){

    const sxTd = {
        textAlign : "center",
        border :"1px solid",
        borderColor : "gray.500"
    }
    const handleSubmit = function(e){
        e.preventDefault()
        console.log("retour")
    }
   
    return(
        <form  >
            <Box p={"20px"}>
                <TableContainer >
                    <Table >
                        <Thead>
                            <Th sx={sxTd}>Gold</Th>
                            <Th sx={sxTd}>Silver</Th>
                            <Th sx={sxTd}>Silver</Th>
                        </Thead>
                        <Tbody>
                            <Tr>
                                <Td sx={sxTd}>
                                    <InputField/>
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
                    <Button type='submit' variant={"outline"} onClick={handleSubmit} >Valider</Button>
                </Center>
            </Box>
        </form>
        
    )
}