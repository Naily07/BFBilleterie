import { Box, Text, Flex, Center  } from "@chakra-ui/react"
import TableBillet from "./tableBillet"
import TableEditBillet from "./tableEditBillet"
import { Select } from '@chakra-ui/react'

export default function AboutPdv(){
    return(
        // bg={"rgba(199,250,255,1)"}
        <Flex   borderRadius={"0.5rem"} w={"100%"} border={'1px solid black'} >
            <Flex w={"80%"}  flexWrap={"wrap"} flexDir={"column"} p={"20px"} justifyContent={"space-evenly"} >
                <Flex ml={"20px"}>
                    <Text >Identifiant : </Text>
                    <Text as={"i"} ml={"10px"}> Loriance</Text>
                </Flex>
                <Box  p={"20px"}>
                    <Select>
                        <option value="event1"> evenement1</option>
                        <option value="event1"> evenement2</option>
                        <option value="event1"> evenement3</option>
                    </Select> 
                </Box>
                <TableBillet />
                <TableEditBillet />
            </Flex>
            <Flex flexDir={"column"} alignItems={"center"} w={"20%"} p={"20px"} borderLeft={"1px solid black"} >
                <Text fontSize={"xl"} as={"b"}  >Vendus</Text>
                <Flex  h={"100%"} flexDir={"column"} alignItems={"center"} justifyContent={"space-evenly"} >
                    <Box w={"auto"} p={"10px"}> 
                        <Text color={"cyan.900"} fontSize={"lg"} as={"i"} >Gold</Text>
                        <Center >55</Center>
                    </Box>
                    <Box w={"auto"} p={"10px"}> 
                        <Text color={"cyan.900"} fontSize={"lg"} as={"i"} >Gold</Text>
                        <Center >55</Center>
                    </Box>
                    <Box w={"auto"} p={"10px"}> 
                        <Text color={"cyan.900"} fontSize={"lg"} as={"i"} >Gold</Text>
                        <Center >55</Center>
                    </Box>
                    <Box w={"auto"} p={"10px"}> 
                        <Text color={"cyan.900"}  fontSize={"lg"} fontWeight={"600"} as={"i"} >Total</Text>
                        <Center >55</Center>
                    </Box>
                </Flex>
            </Flex> 
        </Flex>
    )
}