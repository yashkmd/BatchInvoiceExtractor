import os
import pandas as pd
from config.config import DIRECTORY_PATH, OUTPUT_FILE
from utils.image_processing import get_image_bytes
from utils.model import initialize_model, get_response

# Initialize the model
model = initialize_model("gemini-1.5-flash-latest")

# Hardcoded prompt and model behavior
prompt = "Extract the restaurant name, address, and total amount from the invoice and share it in '|' separated values."
model_behavior = """
You are an expert who understands invoice overall structures and has deep knowledge on it.
We will upload the invoice image and you have to answer the question based on information 
present in the invoice image.
"""

# Create an empty list to store responses
responses = []

# Process each image in the directory
for filename in os.listdir(DIRECTORY_PATH):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        image_path = os.path.join(DIRECTORY_PATH, filename)
        image_info = get_image_bytes(image_path)
        response = get_response(model, model_behavior, image_info, prompt)
        print(response)
        # Extract required attributes from response
        response_parts = response.split("|")
        response_parts.insert(0, filename)  # Insert filename at the beginning
        responses.append(response_parts)

# Create a DataFrame from the responses
df = pd.DataFrame(responses, columns=["Filename", "Restaurant Name", "Address", "Total Amount"])

# Write the DataFrame to an Excel file
df.to_excel(OUTPUT_FILE, index=False)

print(f"Data has been written to {OUTPUT_FILE}")
