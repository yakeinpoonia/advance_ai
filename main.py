from openai import OpenAI
from dotenv import load_dotenv
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

    # Chat history + curretn query
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages = messages
    )

    # Adding the response in chat history
    messages.append(
        {
            "role": "assistant",
            "content": response.choices[0].message.content
        }
    )

    print("Asisstant: "+ response.choices[0].message.content)
