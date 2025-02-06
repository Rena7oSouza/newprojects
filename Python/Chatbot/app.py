import openai
import os

print("Please, paste your API_KEY or just press enter to use a key saved on your system")
api_key = input()
if api_key == "":
    api_key = os.getenv("API_KEY") 


client = openai.OpenAI(api_key=api_key, base_url="https://api.mistral.ai/v1")

def send_message(message):
    response = client.chat.completions.create(
        model="mistral-medium",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content
print(send_message("crie um resumo de toda a saga Dragon Ball Super"))