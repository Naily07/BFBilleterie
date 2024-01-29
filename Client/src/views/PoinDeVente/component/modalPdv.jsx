import { useRef } from "react"
import { useDisclosure } from "@chakra-ui/react"
import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
  } from '@chakra-ui/react'
import { 
    FormControl,
    FormLabel,
    Input,
    Button,
    Box,
    VStack,
    Flex
} from "@chakra-ui/react"

import {
    Accordion,
    AccordionItem,
    AccordionButton,
    AccordionPanel,
    AccordionIcon,
  } from '@chakra-ui/react'

import { CheckboxGroup, Checkbox } from "@chakra-ui/react"
export default function ModalCreatePdv(){
    const { isOpen, onOpen, onClose } = useDisclosure()
    const initialRef = useRef(null)
    const finalRef = useRef(null)

    return(
        <>
            <Button onClick={onOpen}>Créer un point de vente</Button>
            {/* <Input ml={4} ref={finalRef} /> */}

            <Modal
                    initialFocusRef={initialRef}
                    finalFocusRef={finalRef}
                    isOpen={isOpen}
                    onClose={onClose}
                    size={"2xl"}
            >
                <ModalOverlay />
                <ModalContent >
                    <ModalHeader>Créer un point de vente</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody pb={6}>
                        <Flex flexDir={"row"} flexWrap={"nowrap"} justifyContent={"space-between"}>
                            <Box w={"40%"}>
                                <FormControl>
                                    <FormLabel>Lieu</FormLabel>
                                    <Input ref={initialRef} placeholder='Ivandry' />
                                </FormControl>

                                <FormControl mt={4}>
                                    <FormLabel>Ajouter un compte</FormLabel>
                                    <Input placeholder='Compte Befiana' />
                                </FormControl>
                            </Box>
                            {/* <Box ml={"20px"}> */}
                            <Accordion allowToggle ml={"20px"} w={"60%"} mt={"30px"} >
                                <AccordionItem>
                                    <h2>
                                        <AccordionButton _expanded={{ bg: 'blue.800', color: 'white' }}>
                                            <Box as="span" flex='1' textAlign='left'>
                                                Click me to see Event
                                            </Box>
                                            <AccordionIcon />
                                        </AccordionButton>
                                    </h2>
                                    <AccordionPanel>
                                        <CheckboxGroup >
                                            <VStack alignItems={"left"} h={'60px'} overflowY={"scroll"}>
                                                <Checkbox>Box1Box1Box1</Checkbox>
                                                <Checkbox>Box1</Checkbox>
                                                <Checkbox>Box1</Checkbox>
                                                <Checkbox>Box1</Checkbox>
                                                <Checkbox>Box1</Checkbox>
                                            </VStack>
                                        </CheckboxGroup>
                                    </AccordionPanel>
                                </AccordionItem>
                                </Accordion>
                            {/* </Box> */}
                        </Flex>
                    </ModalBody>
                    <ModalFooter>
                        <Button colorScheme='blue' mr={3}>
                            Save
                        </Button>
                        <Button onClick={onClose}>Cancel</Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </>
    )
}