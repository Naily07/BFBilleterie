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
  
  
  export default function TableBillet(){
    const sxTh = {
        textAlign : "center",
        border :"1px solid",
        borderColor : "gray.500",
        color : theme.colors.teal[800],
        fontWeight : "800"
    }
    const sxTd = {
        textAlign : "center",
        border :"1px solid",
        borderColor : "gray.500",
        color : theme.colors.teal[800],
        }
    return(
        <Box p={"20px 20px 10px 20px"} w={"100%"} >
            <Center >
                <Text  as={"b"}  
                        mb={"20px"}     
                >
                     Nombres des billets restants
                </Text>
            </Center>
            <TableContainer >
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