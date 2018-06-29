import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API = os.environ.get("API_TOKEN") # 環境変数の値をAPに代入