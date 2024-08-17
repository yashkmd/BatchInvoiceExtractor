import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment variables
API_KEY = os.getenv("API_KEY")

# Define the directory path containing the invoice images
DIRECTORY_PATH = r"C:\Users\Yash.Patidar\OneDrive - Nitor Infotech Pvt. Ltd\Pictures\Invoices"

# Define the output file name for the Excel file
OUTPUT_FILE = "invoice_data.xlsx"
