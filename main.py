import os
from dotenv import load_dotenv
from google import genai
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
if api_key == None:
    raise RuntimeError("API key not found")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(model = 'gemini-2.5-flash',contents = args.user_prompt)

if __name__ == "__main__":
    if response.usage_metadata is not None:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count 
        print(response.text,"\n Prompt tokens:", prompt_tokens, " \n Response tokens: ", response_tokens)
    else:
        raise RuntimeError("Failed API request")