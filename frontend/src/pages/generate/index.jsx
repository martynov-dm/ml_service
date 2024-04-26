import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Heading,
  Input,
  Text,
  VStack,
  useColorModeValue,
} from "@chakra-ui/react";
import { useEffect, useRef, useState } from "react";
import { useForm } from "react-hook-form";
import WebSocketManager from "../../services/wsManager";

const GeneratePage = () => {
  const { handleSubmit, register, reset } = useForm();
  const formBgColor = useColorModeValue("gray.50", "gray.700");
  const inputBgColor = useColorModeValue("white", "gray.600");
  const [status, setStatus] = useState("idle");
  const wsManagerRef = useRef(null);

  useEffect(() => {
    if (!wsManagerRef.current) {
      wsManagerRef.current = new WebSocketManager(setStatus);
    }
    if (wsManagerRef.current && !wsManagerRef.current.isConnected) {
      wsManagerRef.current.connect();
      setStatus("connecting");
    }

    return () => {
      if (wsManagerRef.current) {
        wsManagerRef.current.disconnect();
        wsManagerRef.current = null;
      }
    };
  }, []);

  const onSubmit = (promptObj) => {
    wsManagerRef.current.sendMessage(promptObj);
  };

  const isConnected = status === "connected";

  return (
    <Box maxW="2xl" mx="auto" py={8}>
      <Heading mb={8} textAlign="center">
        Generate Image
      </Heading>
      <VStack spacing={8} align="stretch">
        <Box bg={formBgColor} p={6} borderRadius="md" boxShadow="md">
          <form onSubmit={handleSubmit(onSubmit)}>
            <FormControl id="prompt">
              <FormLabel>Text Prompt</FormLabel>
              <Input
                type="text"
                {...register("prompt")}
                bg={inputBgColor}
                isDisabled={!isConnected}
              />
            </FormControl>
            <Button
              mt={4}
              colorScheme="teal"
              type="submit"
              isDisabled={!isConnected}
            >
              Generate Image
            </Button>
          </form>
        </Box>
      </VStack>
      <Box mt={4}>
        <Text textAlign="center" fontWeight="bold">
          {status}
        </Text>
      </Box>
    </Box>
  );
};

export default GeneratePage;
