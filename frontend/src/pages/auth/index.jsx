import { Box, Link, Text } from '@chakra-ui/react';
import { useState } from 'react';
import LoginCard from './components/LoginCard';
import SignupCard from './components/SignupCard';


const AuthPage = () => {
  const [isLogin, setIsLogin] = useState(true);

  const toggleAuthMode = () => {
    setIsLogin(!isLogin);
  };

  return (
    <Box>
      {isLogin ? <LoginCard /> : <SignupCard />}
      <Box mt={4} textAlign="center">
        <Text>
          {isLogin ? "Don't have an account?" : 'Already have an account?'}
          <Link variant="link" color={'blue.400'} onClick={toggleAuthMode} ml={2}>
            {isLogin ? 'Sign up' : 'Log in'}
          </Link>
        </Text>
      </Box>
    </Box>
  );
};

export default AuthPage;