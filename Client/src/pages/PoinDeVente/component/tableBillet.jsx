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
    Text,
    Center,
    theme
  } from '@chakra-ui/react'
  import { sxTd, sxTh, sxTableContainer } from '../sytle/tableau'
  
  export default function TableBillet(){
    return(
        <Box p={"20px 20px 10px 20px"} w={"100%"} >
            <Center >
                <Text  as={"b"}  
                        mb={"20px"}     
                >
                     Nombres des billets restants
                </Text>
            </Center>
            <TableContainer sx={sxTableContainer} >
                <Table >
                    <Thead>
                        <Th sx={sxTh}>Gold</Th>
                        <Th sx={sxTh}>Silver</Th>
                        <Th sx={sxTh}>Silver</Th>
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