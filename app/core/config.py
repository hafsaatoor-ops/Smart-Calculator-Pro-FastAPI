from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Application Configuration
APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL")

# JWT Configuration
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)