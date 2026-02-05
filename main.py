import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables
load_dotenv()

# Get API key from environment variables
api_key = os.environ.get("GEMINI_API_KEY")

# Stop execution if API key is missing
if api_key is None:
    raise RuntimeError("API key not found")


# Argument parsing (CLI inputs)
parser = argparse.ArgumentParser(description="Chatbot")

# Required positional argument (must be provided)
parser.add_argument(
    "user_prompt",
    type=str,
    help="User prompt"
)

# Optional flag: --verbose
# If present → args.verbose == True
# If absent  → args.verbose == False
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Enable verbose output"
)

# Parse command-line arguments
args = parser.parse_args()


# Create Gemini client
client = genai.Client(api_key=api_key)


# Prepare message for Gemini
# Gemini expects a structured message format
messages = [
    types.Content(
        role="user",
        parts=[types.Part(text=args.user_prompt)]
    )
]
# Send request to Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages
)
# Main execution block

if __name__ == "__main__":

    # Check if token usage metadata exists
    if response.usage_metadata is not None:

        # Extract token usage information
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count

        # Verbose output: show everything
        if args.verbose:
            print("User prompt:", args.user_prompt)
            print("Prompt tokens:", prompt_tokens)
            print("Response tokens:", response_tokens)
            print("\nResponse:\n", response.text)

        # Normal output: just the AI response
        else:
            print(response.text)

    else:
        raise RuntimeError("Failed API request")
