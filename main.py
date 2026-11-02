from openai import OpenAI
from dotenv import load_dotenv
from tools import *
import json
import os

load_dotenv() # load .env into environment variables

client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

# Global conversation array to maintain chat history
messages = []

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Assistant: See you soon Kuchu Puchu\n")
        break

    # Chat history + current query
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # 1st LLM call
    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages = messages,
        tools = TOOLS
    )

    msg = response.choices[0].message

    # In case of tool calling
    if msg.tool_calls:
        messages.append(msg)

        for tool_call in msg.tool_calls:
            func_name = tool_call.function.name
            func_args = json.loads(tool_call.function.arguments or "{}")

            fn = FUNCTION_NAME_TO_FUNCTION_MAP[func_name]
            result = fn(**func_args)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            )

        # 2nd LLM call in case of tool calling
        response = client.chat.completions.create(
            model = os.getenv("MODEL"),
            messages = messages,
            tools = TOOLS
        )

    # Adding the response in chat history
    messages.append(
        {
            "role": "assistant",
            "content": response.choices[0].message.content
        }
    )

    print("Asisstant: "+ response.choices[0].message.content)
