import.meta.env.PROD;

const isProduction = () => {
  return import.meta.env.PROD ? true : false;
};

export default isProduction