import {
  Box,
  ChakraProvider,
  Flex,
  Grid,
  theme,
  useColorModeValue,
} from '@chakra-ui/react';
import Router from 'router/Router';

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Box textAlign="center" fontSize="xl">
        <Grid minH="100vh" p={3}>
          <Flex
            minH={'100vh'}
            align={'center'}
            justify={'center'}
            bg={useColorModeValue('gray.50', 'gray.800')}
          >
            <Router />
          </Flex>
        </Grid>
      </Box>
    </ChakraProvider>
  );
}
export default App;
