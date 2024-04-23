import { Box, Heading, Text } from "@chakra-ui/react";
import { Link } from "react-router-dom";

const ProfilePage = () => {
  return (
    <Box>
      <Heading>Profile</Heading>
      <Text>This is the profile page.</Text>
      <Link to={"/generate"}>Generate</Link>
    </Box>
  );
};

export default ProfilePage;
