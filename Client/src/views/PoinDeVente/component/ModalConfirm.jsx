import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
    useBoolean,
    theme,
  } from '@chakra-ui/react'
  import { 
    FormControl,
    FormLabel, 
    Input,
    Button
} from '@chakra-ui/react'
import { useCallback, useRef } from 'react'


export default function RemovePdvModal({isOpen, onClose, lieu}){
    const ref = useRef(null)
    const [active, setActive] = useBoolean(true)
    const handleChange = ()=>{
        if(ref.current.value === lieu)
            setActive.off()
        else setActive.on()
    }
    return(
        <>
            <Modal
                isOpen={isOpen}
                onClose={onClose}
                size={"lg"}
            >
                <ModalOverlay/>
                <ModalContent>
                    
                    <ModalHeader>Voulez vous vraiment supprimer le point de vente {lieu}</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                        <FormControl>
                            <FormLabel>Réecriver le Lieu ci-dessous</FormLabel>
                            <Input variant={"outline"} ref={ref} onChange={handleChange} fontWeight={"500"} color={theme.colors.red[600]} focusBorderColor={theme.colors.red[400]}/>
                        </FormControl>
                    </ModalBody>
                    <ModalFooter>
                        <Button colorScheme='blue' mr={3} isDisabled={active}>
                            Supprimer
                        </Button>
                        <Button onClick={onClose}>Retour</Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        
        </>
    )
}