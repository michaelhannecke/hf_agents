import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv


# Load Huggingface token from secrets file
load_dotenv("secrets/.env")
os.getenv("HF_TOKEN")
