import { Box, Button, FormControl, FormErrorMessage, FormLabel, Heading, Input, Stack, useColorModeValue } from '@chakra-ui/react';
import { useForm } from 'react-hook-form';

export default function LoginCard() {
  const {
    handleSubmit,
    register,
    formState: { errors, isSubmitting },
  } = useForm();

  function onSubmit(values) {
    return new Promise((resolve) => {
      setTimeout(() => {
        alert(JSON.stringify(values, null, 2));
        resolve();
      }, 3000);
    });
  }

  return (
    <Stack spacing={8} mx={'auto'} maxW={'lg'} py={12} px={6}>
      <Stack align={'center'}>
        <Heading fontSize={'4xl'}>Sign in</Heading>
      </Stack>
      <Box rounded={'lg'} bg={useColorModeValue('white', 'gray.700')} boxShadow={'lg'} p={8}>
        <form onSubmit={handleSubmit(onSubmit)}>
          <Stack spacing={4}>
            <FormControl id="email" isInvalid={!!errors.email}>
              <FormLabel>Email address</FormLabel>
              <Input
                type="email"
                {...register('email', {
                  required: 'Email is required',
                  pattern: {
                    value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                    message: 'Invalid email address',
                  },
                })}
              />
              <FormErrorMessage><>{errors.email && errors.email.message}</></FormErrorMessage>
            </FormControl>
            <FormControl id="password" isInvalid={!!errors.password}>
              <FormLabel>Password</FormLabel>
              <Input
                type="password"
                {...register('password', {
                  required: 'Password is required',
                  minLength: { value: 6, message: 'Password must be at least 6 characters' },
                })}
              />
              <FormErrorMessage><>{errors.password && errors.password.message}</></FormErrorMessage>
            </FormControl>
            <Stack spacing={10}>
              <Button
                type="submit"
                bg={'blue.400'}
                color={'white'}
                _hover={{
                  bg: 'blue.500',
                }}
                isLoading={isSubmitting}
              >
                Sign in
              </Button>
            </Stack>
          </Stack>
        </form>
      </Box>
    </Stack>
  );
}