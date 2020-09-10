import dotenv

from server.config.config import Config


# Load env vars from file
dotenv.load_dotenv(verbose=True)
cfg = Config()