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
    useDisclosure
  } from '@chakra-ui/react'

import RemovePdvModal from './ModalConfirm'
import { useState } from 'react'

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
                <Table variant={"simple"}  > 
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
                            // <Link href="#" 
                            // display={"block"}
                            // _hover={{
                            //     bgColor : "gray.100"
                            // }}>
                                <Tr key={i} >
                                    <Td >{i}</Td>
                                    <Td sx={sxTd}>{data.Lieu}</Td>
                                    <Td sx={sxTd} >{data.identification}</Td>
                                    <Td sx={sxTd}>{data.contact}</Td>
                                    <Td sx={sxTd}> <Button onClick={()=>handleRemove(data.Lieu)}> delete</Button> </Td>
                                </Tr>
                            // </Link>                        
                        )
                        })}
                    </Tbody>
                </Table>
            </TableContainer>
        </Box>

    </>
     )
}