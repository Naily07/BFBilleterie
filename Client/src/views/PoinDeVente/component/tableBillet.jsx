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
    Box,
    theme,
  } from '@chakra-ui/react'
import { color } from 'framer-motion'
  
  
  export default function TableBillet(){
    const sxTd = {
        textAlign : "center",
        border :"1px solid",
        borderColor : "black"
    }
    return(
        <Box p={"20px"} >
            <TableContainer >
                <Table >
                    <Thead>
                        <Th sx={sxTd}>Gold</Th>
                        <Th sx={sxTd}>Silver</Th>
                        <Th sx={sxTd}>Silver</Th>
                    </Thead>
                    <Tbody>
                        <Tr>
                            <Td sx={sxTd}>70</Td>
                            <Td sx={sxTd}>70</Td>
                            <Td sx={sxTd}>70</Td>
                        </Tr>
                    </Tbody>
                </Table>
            </TableContainer>
        </Box>
        
    )
}