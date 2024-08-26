import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Heading,
  Image,
  Input,
  Text,
  VStack,
  useColorModeValue,
} from "@chakra-ui/react";
import { useEffect, useRef, useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import useAuth from "../../hooks/useAuth";
import { connectionStatuses, wsManager } from "../../services/wsManager";

const GeneratePage = () => {
  const { user } = useAuth();
  const navigate = useNavigate();

  const { handleSubmit, register, reset } = useForm();
  const formBgColor = useColorModeValue("gray.50", "gray.700");
  const inputBgColor = useColorModeValue("white", "gray.600");
  const [status, setStatus] = useState(connectionStatuses.idle);
  const [imageUrl, setImageUrl] = useState("");
  const wsManagerRef = useRef(null);
  console.log(user);
  if (!user) navigate("/");

  useEffect(() => {
    if (!wsManagerRef.current) {
      wsManagerRef.current = wsManager;
    }
    if (wsManagerRef.current && !wsManagerRef.current.isConnected) {
      wsManagerRef.current.connect(setStatus, setImageUrl);
    }
    return () => {
      if (wsManagerRef.current) {
        wsManagerRef.current.disconnect(setStatus);
        wsManagerRef.current = null;
      }
    };
  }, []);

  const onSubmit = (promptObj) => {
    wsManagerRef.current.sendMessage(promptObj, setStatus);
    reset();
  };

  const isConnected = status === connectionStatuses.connected;

  return (
    <Box mt={"35px"} minW={"35vw"} mx="auto" py={8}>
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
                w="100%"
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
          Connection Status: {status}
        </Text>
      </Box>
      {imageUrl && (
        <Box mt={8}>
          <Image
            src={imageUrl}
            alt="Generated Image"
            borderRadius="md"
            boxShadow="md"
            objectFit="cover"
            w="100%"
            h="auto"
            maxH="400px"
          />
        </Box>
      )}
    </Box>
  );
};

export default GeneratePage;
