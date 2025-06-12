import os
import sys

if len(sys.argv) < 2:
    print("Prompt not provided.")
    sys.exit(1)

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
user_prompt = sys.argv[1]
messages = types.Content(role="user", parts=[types.Part(text=user_prompt)])

client = genai.Client(api_key=api_key)
res = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
print(res.text)
if "--verbose" in sys.argv:
    print(f"User prompt: {user_prompt}")
    print("Prompt tokens:", res.usage_metadata.prompt_token_count)
    print("Response tokens:", res.usage_metadata.candidates_token_count)
