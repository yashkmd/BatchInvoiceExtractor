# import dependencies
import os
import google.generativeai as genai
from PIL import Image
import csv

import pandas as pd

# configure API by loading key from .env file
# load environment variables
genai.configure(api_key="AIzaSyDYJljqtTyxsity7sonew9GbNMkZZ6jSjo")

def initialize_model(model_name="gemini-1.5-flash-latest"):
    model = genai.GenerativeModel(model_name)
    return model

def get_image_bytes(image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        image_info = [
            {
                "mime_type": "image/jpeg",  # Adjust this if your image is not JPEG
                "data": image_bytes
            }
        ]
        return image_info

def get_response(model, model_behavior, image, prompt):
    response = model.generate_content([model_behavior, image[0], prompt])
    return response.text

# initialize the gemini-pro-vision
model = initialize_model("gemini-1.5-flash-latest")

# specify the directory containing the images and the hardcoded prompt
directory_path = r"C:\Users\Yash.Patidar\OneDrive - Nitor Infotech Pvt. Ltd\Pictures\Invoices"  # Replace with your directory path
prompt = """Extract the Buisness name, Bunsiness Domain like Restaurant/Super Marketetc.,  address,invoice number,invoice date,
 total amount from the invoice and share it in '|' 
seperated values. Make sure to display amount without any currency. Parse dates in 'DD/MM/YYYY' format. 
Also write NULL if any of the columns are not present.Make sure to limit to only 5 columns"""

# set the model behavior
model_behavior = """
You are an expert who understands invoice overall structures and has deep knowledge on it.
We will upload the invoice image and you have to answer the question based on information 
present in the invoice image. Try to find the business domain based on the details in the invoice.
"""

# Create an empty list to store responses
responses = []


# process each image in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        image_path = os.path.join(directory_path, filename)
        image_info = get_image_bytes(image_path)
        response = get_response(model, model_behavior, image_info, prompt)
        print(response)
        # Extract required attributes from response (assuming response is a string with values separated by commas)
        response_parts = response.split("|")
        response_parts.insert(0,filename)
        responses.append(response_parts)

# Create a DataFrame from the responses
df = pd.DataFrame(responses, columns=["Filename","Business Name", "Business Domain" ,"Address", "Invoice Number", "Invoice Date" ,"Total Amount"])

# Write the DataFrame to an Excel file
output_file = "invoice_data.xlsx"
df.to_excel(output_file, index=False)

print(f"Data has been written to {output_file}")


