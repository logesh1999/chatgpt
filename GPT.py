import openai

openai.api_key = 'your api key'
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

while True:
    message = input("You : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"Bot: {reply}")
    messages.append({"role": "assistant", "content": reply})