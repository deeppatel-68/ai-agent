import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():

    # Check if prompt was provided
    if len(sys.argv) < 2:
        print("Error: Please provide a prompt")
        sys.exit(1)

    # Get Prompt
    user_prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv

    # Create messages list with user role
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # generate response using messages
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

    print(response.text)

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(
            f'Response tokens: {response.usage_metadata.candidates_token_count}')


if __name__ == "__main__":
    main()
