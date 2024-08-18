import google.generativeai as genai
#from config.config import API_KEY

genai.configure(api_key="your_api_key")


def initialize_model(model_name="gemini-1.5-flash-latest"):
    model = genai.GenerativeModel(model_name)
    return model

def get_response(model, model_behavior, image, prompt):
    response = model.generate_content([model_behavior, image[0], prompt])
    return response
