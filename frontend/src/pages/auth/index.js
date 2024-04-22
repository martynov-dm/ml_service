import { Box } from '@chakra-ui/react';
import React from 'react';
import LoginCard from './components/LoginCard';
import SignupCard from './components/SignupCard';

const AuthPage = () => {
  return (
    <Box>
      <LoginCard />
      <SignupCard />
    </Box>
  );
};

export default AuthPage;