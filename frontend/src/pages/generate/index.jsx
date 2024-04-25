import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Heading,
  Input,
  VStack,
  useColorModeValue,
} from "@chakra-ui/react";
import { useEffect, useRef, useState } from "react";
import { useForm } from "react-hook-form";
import GenerateService from "../../services/generate";

const GeneratePage = () => {
  const { handleSubmit, register, reset } = useForm();
  const formBgColor = useColorModeValue("gray.50", "gray.700");
  const inputBgColor = useColorModeValue("white", "gray.600");

  const [status, setStatus] = useState("idle");
  const generateServiceRef = useRef(null);

  useEffect(() => {
    // Clean up the generate service when the component unmounts
    return () => {
      if (generateServiceRef.current) {
        generateServiceRef.current.disconnect();
      }
    };
  }, [generateServiceRef]);

  const onSubmit = (data) => {
    reset();
    const { prompt } = data;
    setStatus("loading");

    const newGenerateService = new GenerateService();
    newGenerateService.connect(prompt, setStatus);
    generateServiceRef.current = newGenerateService;
  };

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
              <Input type="text" {...register("prompt")} bg={inputBgColor} />
            </FormControl>
            <Button mt={4} colorScheme="teal" type="submit">
              Generate Image
            </Button>
          </form>
        </Box>
      </VStack>
      <Heading mb={8} textAlign="center">
        {status}
      </Heading>
    </Box>
  );
};

export default GeneratePage;
