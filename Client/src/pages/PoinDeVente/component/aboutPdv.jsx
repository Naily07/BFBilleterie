import { Box, Text, Flex, Center, theme, VStack  } from "@chakra-ui/react"
import TableBillet from "./tableBillet"
import TableEditBillet from "./tableEditBillet"
import { Select } from '@chakra-ui/react'
import Example from "./Chart"
import { useEffect, useState } from "react"

const donne = [
    {
        type_ticket : "gold",
        nb_ticket : 70
    },
    {
        type_ticket : "silver",
        nb_ticket : 5
    },
    {
        type_ticket : "cooper",
        nb_ticket : 2
    }
]

export default function AboutPdv(){
    return(
        <Flex borderRadius={"0.5rem"} bgColor={"white"} shadow={"rgba(149, 157, 165, 0.2) 0px 8px 24px;"} >
            <Flex w={"auto"} minW={"70%"} flexWrap={"wrap"} flexDir={"column"} p={"20px"} justifyContent={"center"} >
                <Flex ml={"20px"}>
                    <Text as={"b"} _after={{content:"''", height:"2px", w:"100%", bgColor:theme.colors.gray[600], display:"block"}} >Identifiant : </Text>
                    <Text as={"i"} ml={"10px"}> Loriance</Text>
                </Flex>
                <Box  p={"20px 20px 10px 20px"}>
                    <Select>
                        <option value="event1"> evenement1</option>
                        <option value="event1"> evenement2</option>
                        <option value="event1"> evenement3</option>
                    </Select> 
                </Box>
                <TableBillet />
                <TableEditBillet />
            </Flex>
            <VStack 
             borderLeft={"3px solid"} borderColor={"gray.100"}
            >
                {/* <Statistic title = {"Billets"} /> */}
                <Statistic title = {"Vendus"}/>
            </VStack>
        </Flex>
    )
}

function Statistic({title}){
    const [datas, setData] = useState(donne)
    const total = ()=>{
        let t = 0
        t = t + datas.map((data)=>{
            return data.nb_ticket
        }).reduce((acc, curr) => acc + curr, 0);
        return t
    }
    return(
        <VStack spacing={3} p={"20px 10px 10px 10px"} 
            >
                <Box fontSize={"xl"} as={"b"} _after={{content:"''", height:"2px", w:"100%", bgColor:"black", display:"block"}} >
                    {title}
                </Box>
                <Flex  flexDir={"column"} alignItems={"center"} justifyContent={"space-around"}>
                    <Flex w={"100%"}   p={"10px"} flexDir={"column"} alignItems={"center"} > 
                        {datas && datas.map((data)=>{
                            return(
                                <Flex  w={"100%"}  justifyContent={"center"} m={"5px"} key={data.type_ticket}>
                                    <Text color={theme.colors.teal[800]} fontSize={"lg"} fontWeight={"600"} as={"i"} >{data.type_ticket} :</Text>
                                    <Text fontSize={"lg"} color={theme.colors.yellow[500]} ml={"10px"}> {data.nb_ticket} </Text>
                                </Flex>
                            )
                        })}
                    </Flex>
                    <Flex  w={"100%"}  justifyContent={"center"}>
                            <Text color={theme.colors.teal[800]} fontSize={"lg"} fontWeight={"600"} as={"i"} >Total : </Text>
                            <Text fontSize={"lg"} color={theme.colors.yellow[500]} ml={"10px"}> {total()} </Text>
                    </Flex>
                </Flex>
        </VStack> 
    )
}