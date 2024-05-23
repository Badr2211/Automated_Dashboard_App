from dotenv import load_dotenv
import os
import google.generativeai as genai
from pathlib import Path
from helper import get_settings
# Load environment variables
load_dotenv()

# Get the current file path
current_file_path = Path(__file__).resolve()

# Get the directory containing the current file
current_directory = current_file_path.parent

src_directory = current_directory.parent

api_key=os.getenv('GOOGLE_API_KEY')
# Configure API key
genai.configure(api_key=get_settings().GOOGLE_API_KEY)

def generate_text(image, custom_prompt):

    # Set up the model
    generation_config = {
        "temperature": 0.1,
        "top_p": 1,
        "top_k": 32,
        "max_output_tokens": 4096,
    }

    model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                  generation_config=generation_config)
    

    prompt_parts = [
        image,
        custom_prompt,
    ]

    response = model.generate_content(prompt_parts)
    return response.text
