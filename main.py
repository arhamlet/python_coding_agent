import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

from functions.get_files_info import get_files_info


def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    if len(sys.argv) < 2:
        print("I need a prompt")
        sys.exit(1)
    prompt = sys.argv[1]
    verbose_flag=False
    if len(sys.argv) == 3 and sys.argv[2]=="--verbose":
        verbose_flag = True


    messages = []

    user_input = prompt

    if user_input.lower() in {"exit", "quit"}:
        sys.exit(0)

    # Add user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Send full conversation
    response = client.responses.create(
        model="gpt-4o-mini",
        input=messages,
    )
    print(response.output_text)

    # Save assistant reply
    messages.append({
        "role": "assistant",
        "content": response.output_text
    })

    if verbose_flag:
        print(f"User Prompt: {prompt}")
        print(f"Input: {response.usage.input_tokens}")
        print(f"Output: {response.usage.output_tokens}")
        print(f"Total: {response.usage.total_tokens}")


# print(get_files_info("calculator"))
main()