import logging
import sys

fastapi_logger = logging.getLogger()
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
fastapi_logger.handlers.append(stream_handler)
fastapi_logger.setLevel(logging.INFO)
