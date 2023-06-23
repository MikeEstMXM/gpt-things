
import os
import openai


AI_KEY = open("../key.txt",'r').read().strip(' \n')
API_ENDPOINT = "https://api.openai.com/v1/chat/gpt4/completions"


def get_chat_number():
    chat_folder = "chats"
    os.makedirs(chat_folder, exist_ok=True)
    files = [f for f in os.listdir(chat_folder) if f.startswith("chat") and f.endswith(".txt")]
    if not files:
        return 0
    latest_chat = max(files, key=lambda x: int(x[4:-4]))
    print(f"Continue chat {int(latest_chat[4:-4])}?\n")
    usr_rsp = input("y/n: ").strip(' esopah.?!').lower()
    if usr_rsp == "y":
        return int(latest_chat[4:-4])
    return int(latest_chat[4:-4])+1

def save_chat_to_file(chat, file_number):
    chat_folder = "chats"
    os.makedirs(chat_folder, exist_ok=True)
    filename = f"{chat_folder}/chat{file_number}.txt"
    with open(filename, "w") as file:
        file.write(chat)

def generate_chat_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."}, 
{"role": "user", "content": user_input}],
        max_tokens=1024
    )
    chatgpt_response = response.choices[0].message.content.strip()
    return chatgpt_response

def emulate_chat_interface():
    chat_number = get_chat_number()
    if os.path.isfile(f"chats/chat{chat_number}.txt"):
        chat = G
    else:
        chat = ""

    print("ChatGPT Emulator")
    print("Type 'end' to quit.\n")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "end":
            break

#        if user_input.startswith("continue"):
#            try:
#                continue_number = int(user_input.split()[1])
#                if continue_number <= latest_chat_number:
#                    filename = f"Chats/chat{continue_number}.txt"
#                    with open(filename, "r") as file:
#                        chat = file.read()
#                        chat_number = continue_number
#                        print(f"Continuing conversation from {filename}\n")
#                        continue
#                else:
#                    print("Invalid conversation number. Starting a new conversation.\n")
#            except (IndexError, ValueError):
#                print("Invalid command. Starting a new conversation.\n")

        chat += f"User: {user_input}\n"
        chatgpt_response = generate_chat_response(chat)
        chat += f"ChatGPT: {chatgpt_response}\n"

        save_chat_to_file(chat, chat_number)

#        chat_number += 1
#        latest_chat_number = max(latest_chat_number, chat_number)

        print(f"ChatGPT: {chatgpt_response}\n")

    save_chat_to_file(chat, chat_number)
    print(f"Chat saved to chats/chat{chat_number}.txt")


openai.api_key = API_KEY
emulate_chat_interface()
