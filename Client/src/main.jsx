import React from 'react'
import App from './App.jsx'
import { ChakraProvider } from '@chakra-ui/react'
import { extendTheme } from '@chakra-ui/react'
import ReactDOM from 'react-dom/client'
import { mode } from '@chakra-ui/theme-tools'
import './index.css'

const colors = {
  brand: {
    900: '#1a365d',
    800: '#153e75',
    700: '#2a69ac',
  },
}


const styles = {
  global: (props) => ({
    body: {
      fontFamily: 'body',
      bg: mode('gray.50', 'black')(props),
    },
    '*::placeholder': {
      color: mode('gray.400', 'whiteAlpha.800')(props),
    },
    '*, *::before, &::after': {
      borderColor: mode('gray.200', 'whiteAlpha.300')(props),
      wordWrap: 'break-word',
    },
  }),
}

const theme = extendTheme({ colors, styles })


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ChakraProvider theme={theme} >
      {/* AA */}
      <App />
    </ChakraProvider>
  </React.StrictMode>,
)
