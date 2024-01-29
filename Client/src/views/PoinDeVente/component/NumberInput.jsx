  
  import {
    NumberInput,
    NumberInputField,
    NumberInputStepper,
    NumberIncrementStepper,
    NumberDecrementStepper,
  } from '@chakra-ui/react'
  import { useMemo, useReducer, useState } from 'react'


export default function InputField() {
    const ref = useReducer(null)
    const [state, setState] = useState(0)
    
    const isDecrement = useMemo(()=>{
        if(state>0)
            return <NumberDecrementStepper  />
        return null
    }, [state])
    const handlClick = (e)=>{
        console.log(e);
        setState(()=>{
            return ref.current.value
        })
    }
    return(
    <NumberInput onClick={handlClick} defaultValue={0} min={"0"} >
        <NumberInputField ref={ref} />
        <NumberInputStepper >
            <NumberIncrementStepper />
            {isDecrement}
        </NumberInputStepper>
    </NumberInput>
    )
}