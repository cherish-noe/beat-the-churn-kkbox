import kaggle
import os
from dotenv import load_dotenv
import zipfile

load_dotenv() # Load environment variables from .env file

kaggle_username = os.getenv('KAGGLE_USERNAME')
kaggle_key = os.getenv('KAGGLE_KEY')

kaggle.api.authenticate() # use the Kaggle API


competition_name = "kkbox-churn-prediction-challenge"
download_dir = "../data"

# Create destination folder if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Download the dataset
kaggle.api.competition_download_files(competition_name, path= download_dir, force=True)

# Unzip files 
for filename in os.listdir(download_dir):
    if filename.endswith(".zip"):
        filepath = os.path.join(download_dir, filename)
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(download_dir)

# Remove the zip file after extracting
os.remove(filepath)


