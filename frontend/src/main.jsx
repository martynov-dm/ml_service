import { ChakraProvider, theme } from "@chakra-ui/react";
import { PersistQueryClientProvider } from "@tanstack/react-query-persist-client";
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { persister, queryClient } from "./react-query-client";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <ChakraProvider theme={theme}>
      <PersistQueryClientProvider
        client={queryClient}
        persistOptions={{
          persister,
          maxAge: 1000 * 60 * 60 * 4, // 4 hours
          dehydrateOptions: {
            shouldDehydrateQuery: (query) => {
              return !!query.options.meta.persist;
            },
          },
        }}
      >
        <App />
      </PersistQueryClientProvider>
    </ChakraProvider>
  </React.StrictMode>
);
