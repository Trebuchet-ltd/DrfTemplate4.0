from dotenv import load_dotenv
import os

load_dotenv(".env")
settings = os.getenv('SETTINGS')
debug = os.getenv('DEBUG')


if settings == "dev":
    print("DEVELOPMENT SERVER")
    from .development_settings import *

else:
    print("PRODUCTION SERVER")
    from .production_settings import *
