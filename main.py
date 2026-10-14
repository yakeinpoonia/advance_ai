from openai import OpenAI

client = OpenAI(
    base_url = "http://127.0.0.1:11434/v1", # openai compatible api provided by ollama
    api_key = "dummy_key"
)

response = client.chat.completions.create(
    model = "qwen3:4b",
    messages = [
        {
            "role":"user",
            "content":"Hey!! How are you ?"
        }
    ]
)

print("LLM Response: ")
print(response.choices[0].message.content)
