import { ViewIcon, ViewOffIcon } from '@chakra-ui/icons';
import { Box, Button, FormControl, FormErrorMessage, FormLabel, Heading, Input, InputGroup, InputRightElement, Link, Stack, Text, useColorModeValue } from '@chakra-ui/react';
import { useState } from 'react';
import { useForm } from 'react-hook-form';

export default function SignupCard() {
  const [showPassword, setShowPassword] = useState(false);
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
        <Heading fontSize={'4xl'} textAlign={'center'}>
          Sign up
        </Heading>
      </Stack>
      <Box rounded={'lg'} bg={useColorModeValue('white', 'gray.700')} boxShadow={'lg'} p={8}>
        <form onSubmit={handleSubmit(onSubmit)}>
          <Stack spacing={4}>
            <FormControl id="username" isInvalid={!!errors.username}>
              <FormLabel>Username</FormLabel>
              <Input
                type="text"
                {...register('username', {
                  required: 'Username is required',
                  minLength: { value: 4, message: 'Username must be at least 4 characters' },
                })}
              />
              <FormErrorMessage><>{errors.username && errors.username.message}</></FormErrorMessage>
            </FormControl>
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
              <InputGroup>
                <Input
                  type={showPassword ? 'text' : 'password'}
                  {...register('password', {
                    required: 'Password is required',
                    minLength: { value: 6, message: 'Password must be at least 6 characters' },
                  })}
                />
                <InputRightElement h={'full'}>
                  <Button variant={'ghost'} onClick={() => setShowPassword((showPassword) => !showPassword)}>
                    {showPassword ? <ViewIcon /> : <ViewOffIcon />}
                  </Button>
                </InputRightElement>
              </InputGroup>
              <FormErrorMessage><>{errors.password && errors.password.message}</></FormErrorMessage>
            </FormControl>
            <Stack spacing={10} pt={2}>
              <Button
                type="submit"
                loadingText="Submitting"
                size="lg"
                bg={'blue.400'}
                color={'white'}
                _hover={{
                  bg: 'blue.500',
                }}
                isLoading={isSubmitting}
              >
                Sign up
              </Button>
            </Stack>
          </Stack>
        </form>
      
      </Box>
    </Stack>
  );
}