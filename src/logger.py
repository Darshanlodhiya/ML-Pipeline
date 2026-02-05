import logging
import os
from datetime import datetime

# Safe timestamp (no slashes)
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# logs directory only
LOG_PATH = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_PATH, exist_ok=True)

# full file path
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
