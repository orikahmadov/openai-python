import os
import openai
from datetime import datetime
from rich.console import Console,Style

API_KEY =  os.environ["OPENAI_API_KEY"]
openai.api_key = API_KEY
console =  Console()
current_year = datetime.now().strftime("%Y")
user_style =  Style(color="cyan",bold=True)
bot_style =  Style(color="red",bold=False)
waiting_style =  Style(color="yellow",bold=True)
conversation =   [{"role": "system", "content": """
You are an AI Programming Assistant 
- Follow user's requirements carefully & to the letter.
- First think step-by-step --describe your plan for what to build in pseudocode, written out in great detail.
- Then output the code in single block.
- Minimize any other prose.   
Current year is {}. 
""".format(current_year)}]
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    console.log("Welcome to the Openai chat!\nIf you want to quit the chat just type 'exit!'\nIf you want to quit chat and save conversation just press 'ctrl + c' and answer 'y'\n",style="yellow")
    while True:
        try:
            user_input = input("User: ")
            if user_input == "exit!":
                break
            conversation.append({"role": "user", "content": user_input})
            console.log(f"Bot is thinking...", style=waiting_style)
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages=conversation
            )
            seperator  =  "*"*100
            console.log(seperator, style="bold magenta")
            reply_bot = response["choices"][0]["message"]["content"]
            conversation.append({"role": "system", "content": reply_bot})
            console.log(f"Bot: {reply_bot}", style="bold green")
        except KeyboardInterrupt:
            save_conversationn = input("Do you want to save the conversation? (y/n): ")
            if save_conversationn.lower() == "y":
                save_conversation(name =hash(user_input), conversation=conversation)
                print("Thanks for chatting with me!")
                break
            else:
                print("Thanks for chatting with me!")
                break

def save_conversation(name,conversation):
    if os.path.exists("programmer_assitant_conversations"):
        pass
    else:
        os.mkdir("programmer_assitant_conversations")
    with open(f"programmer_assitant_conversations/{name}.txt","w") as f:
        f.write(f"Conversation started at {timestamp}\n")
        for i in conversation:
            f.write(f"{i['role']}: {i['content']}\n")

        print("Conversation saved successfully!")
        
if __name__ == "__main__":
    main()
