import { Box, Heading, Text } from "@chakra-ui/react";
import { Link } from "react-router-dom";

const GeneratePage = () => {
  return (
    <Box>
      <Heading>Generate</Heading>
      <Text>This is the generate page.</Text>
      <Link to={"/profile"}>Profile</Link>
    </Box>
  );
};

export default GeneratePage;
