import {
  ChakraProvider,
  Flex,
  theme,
  useColorModeValue
} from '@chakra-ui/react';
import Router from './router/Router';

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Flex textAlign="center" justifyContent={'center'} width='100%' height='100%' fontSize="xl" p={3} bg={useColorModeValue('gray.100', 'gray.800')}>
          <Flex
            align={'center'}
            justify={'center'}
          >
            <Router />
          </Flex>
      </Flex>
    </ChakraProvider>
  );
}
export default App;