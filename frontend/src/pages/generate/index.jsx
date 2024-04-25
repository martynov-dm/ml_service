import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Heading,
  Image,
  Input,
  Spinner,
  VStack,
  useColorModeValue,
} from "@chakra-ui/react";
import { useMutation } from "@tanstack/react-query";
import { useForm } from "react-hook-form";
import generateService from "../../services/generate";

const GeneratePage = () => {
  const { handleSubmit, register, reset } = useForm();
  const formBgColor = useColorModeValue("gray.50", "gray.700");
  const inputBgColor = useColorModeValue("white", "gray.600");

  const {
    mutate,
    data: imageUrl,
    isPending,
  } = useMutation({
    mutationFn: generateService.generate,
    onSuccess: () => {
      reset();
    },
    onError: (err) => {
      alert(err.message);
    },
  });

  const onSubmit = (data) => {
    mutate(data);
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
        {isPending ? (
          <Box textAlign="center">
            <Spinner size="xl" />
            <Box mt={4}>Generating image...</Box>
          </Box>
        ) : imageUrl ? (
          <Box mt={8} borderRadius="md" overflow="hidden" boxShadow="md">
            <Image src={imageUrl} alt="Generated" objectFit="cover" />
          </Box>
        ) : null}
      </VStack>
    </Box>
  );
};

export default GeneratePage;
