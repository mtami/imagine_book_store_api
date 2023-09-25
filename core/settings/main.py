import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if os.environ.get("DJANGO_ENV") == "production":
    from .prod import *  # noqa
else:
    from .local import *  # noqa
