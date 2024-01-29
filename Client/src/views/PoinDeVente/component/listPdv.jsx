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
    // Link
  } from '@chakra-ui/react'
import RemovePdvModal from './ModalConfirm'
import { useState } from 'react'
import { Link as ReactRouterLink } from 'react-router-dom'
import { Link as ChakraLink } from '@chakra-ui/react'
import { GoTrash } from "react-icons/go";
import { Icon } from '@chakra-ui/react'
const data = [
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
        {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
       {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    }
    ,
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
    {
        Lieu : "Ankorondrano",
        identification : "Loriance",
        contact : "+261325899963"
    },
]



export default function ListPdv(){
    const {isOpen, onOpen, onClose} = useDisclosure()
    const [state, setState] = useState()
    const sxTd = {
        textAlign : "center",
        border : "1px solid",
        borderColor : "gray.400"        
    }
    const sxTh = {
        bgColor : "blue.800" ,
        color : "white",
        textAlign : "center",
        border : "1px solid",
    }
    const handleRemove = (lieu)=>{
        onOpen()
        setState(lieu)
    }
    return(
    <>
        <RemovePdvModal isOpen = {isOpen}  onClose = {onClose} lieu = {state} />
        <Box mr={2} >
            <TableContainer h={"xl"} overflowY={"scroll"} >
                <Table variant={"simple"} display={"inline-block"}> 
                    <Thead >
                        <Tr>
                            <Th></Th>
                            <Th  sx={sxTh} >Lieu</Th>
                            <Th  sx={sxTh}>Identification</Th>
                            <Th  sx={sxTh}>Contact</Th>
                            <Th  sx={sxTh}>Supprimer</Th>
                        </Tr>
                    </Thead>
                    <Tbody >
                        {data && data.map((data, i)=>{
                        return (                            
                            <Tr key={i} >
                                <ChakraLink href="#" 
                                    as={ReactRouterLink}
                                    display={"block"}
                                    _hover={{
                                        bgColor : "gray.100"
                                    }}
                                    > 
                                    <Td >{i}</Td>
                                    <Td sx={sxTd}>{data.Lieu}</Td>
                                    <Td sx={sxTd} >{data.identification}</Td>
                                    <Td sx={sxTd}>{data.contact}</Td>
                                    <Td sx={sxTd}> <Button onClick={()=>handleRemove(data.Lieu)}><Icon as = {GoTrash} color={"red"}/></Button> </Td>
                             </ChakraLink>                        
                                </Tr>
                        )
                        })}
                    </Tbody>
                </Table>
            </TableContainer>
        </Box>

    </>
     )
}