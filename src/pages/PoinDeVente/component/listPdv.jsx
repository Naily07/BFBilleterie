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
    Button,
    useDisclosure,
    theme,
    Text
  } from '@chakra-ui/react'
import RemovePdvModal from './ModalConfirm'
import { useState } from 'react'
import { GoTrash } from "react-icons/go";
import { Icon } from '@chakra-ui/react'
const data = [
    {
        identification : "Loriance",
        Lieu : "Ankorondrano",
        contact : "+261325899963",
    },
    {
        identification : "Loriance",
        Lieu : "Ivandry",
        contact : "+261325899963",
    },
    {
        identification : "Loriance",
        Lieu : "Ankorondrano",
        contact : "+261325899963",
    },
    {
        identification : "Loriance",
        Lieu : "Ankorondrano",
        contact : "+261325899963",
    },
        {
            identification : "Loriance",
            Lieu : "Analakely",
        contact : "+261325899963",
    },
    {
        identification : "Loriance",
        Lieu : "Analakely",
        contact : "+261325899963",
    },
    {
        identification : "Loriance",
        Lieu : "Ankorondrano",
        contact : "+261325899963",
    },
       {
           identification : "Loriance",
           Lieu : "Analakely",
        contact : "+261325899963",
    },
    {
        identification : "Loriance",
        Lieu : "Ankorondrano",
        contact : "+261325899963",
    },
    {
        identification : "Loriance",
        Lieu : "Ankorondrano",
        contact : "+261325899963",
    }
    ,
    {
        identification : "Loriance",
        Lieu : "Ankorondrano",
        contact : "+261325899963",
    },
    {
        identification : "Loriance",
        Lieu : "Ankorondrano",
        contact : "+261325899963",
    },
    {
        identification : "Loriance",
        Lieu : "Ankorondrano",
        contact : "+261325899963",
    },
]



export default function ListPdv(){
    const {isOpen, onOpen, onClose} = useDisclosure()
    const [state, setState] = useState()
    const sxTd = {
        textAlign : "center",
        border : "1px solid",
        borderColor : "gray.400",
             
    }
    const sxTh = {
        position : "relative",
        bgColor : "blue.800" ,
        color : "white",
        textAlign : "center",
        border : "1px solid white",
        zIndex : 9,
    }
    const handleRemove = (lieu)=>{
        onOpen()
        setState(lieu)
    }
    return(
    <Box  borderRadius={"0.5rem"} shadow={"rgba(149, 157, 165, 0.2) 0px 8px 24px;"}>
        <RemovePdvModal isOpen = {isOpen}  onClose = {onClose} lieu = {state} />
        <Box mr={2} bgColor={"white"} borderRadius={"0.5rem"} >
            {/* <Text p={theme.space[20]}>Liste de tous les points de vente</Text> */}
            <TableContainer h={"xl"} overflowY={"scroll"} borderRadius={"0.5rem"} >
                <Table variant={"simple"} > 
                    <Thead position={"sticky"}  top={"0"} zIndex={8}>
                        <Tr>
                            <Th  sx={sxTh} >id</Th>
                            <Th  sx={sxTh} >identification</Th>
                            <Th  sx={sxTh}>Lieu</Th>
                            <Th  sx={sxTh}>Contact</Th>
                            <Th  sx={sxTh}>Supprimer</Th>
                        </Tr>
                    </Thead>
                    <Tbody zIndex={1}>
                        {data && data.map((data, i)=>{
                        return (                            
                            <Tr key={i} onClick={()=>handleClick} _hover={{bgColor : "gray.200", cursor:"pointer" }}>
                                <Td  >{i + 1}</Td>
                                <Td sx={sxTd}>{data.identification}</Td>
                                <Td sx={sxTd} >{data.Lieu}</Td>
                                <Td sx={sxTd}>{data.contact}</Td>
                                <Td sx={sxTd}> 
                                <Button onClick={()=>handleRemove(data.Lieu)} bgColor={"white"} 
                                    _hover={{bgColor : theme.colors.red[600], color: theme.colors.white}} p={0} m={0}
                                    color={theme.colors.red[600]}
                                >
                                    <Icon as = {GoTrash}  h={"100%"} /> 
                                </Button>
                                </Td>
                            </Tr>
                        )
                        })}
                    </Tbody>
                </Table>
            </TableContainer>
        </Box>

    </Box>
     )
}