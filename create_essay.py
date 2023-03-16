import os
import openai
from datetime import datetime
from rich.console import Console,Style
from rich.prompt import Prompt

API_KEY =  os.environ["OPENAI_API_KEY"]
openai.api_key = API_KEY
console =  Console()
current_year = datetime.now().strftime("%Y")
user_style =  Style(color="cyan",bold=True)
bot_style =  Style(color="red",bold=False)
waiting_style =  Style(color="yellow",bold=True)
conversation =   [{"role": "system", "content": 
"""
-You are a my scientific advisor and a proffessor 
-You will help to write a scientific paper or an essay based on the given topic
Current year is {}.

""".format(current_year)}]
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    console.log("Welcome to the Openai chat!\nIf you want to quit the chat just type 'exit!'\nIf you want to quit chat and save conversation just press 'ctrl + c' and answer 'y'\n",style="yellow")
    while True:
        try:
            outline_topic = Prompt.ask("Name of topic: E.g 'Nicola Tesla and his contribution to the technology' ")
            if not outline_topic:
                console.log("Please enter a topic!",style="bold red")
                continue
            user_input = f"Create an outline for an essay about {outline_topic}"
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
            essay_command = """Write a long clear, informative, well-structured essay for given outline"""
        except KeyboardInterrupt:
            save_conversationn = input("Do you want to save the conversation? (y/n): ")
            if save_conversationn.lower() == "y":
                save_conversation()
                print("Thanks for chatting with me!")
                break
            else:
                print("Thanks for chatting with me!")
                break

def save_conversation():
    with open("conversation.txt","a") as f:
        f.write(f"{timestamp}\n")
        for i in conversation:
            f.write(f"{i['role']}: {i['content']}\n")
        f.write("\n")

    print("Conversation saved successfully!")



if __name__ == "__main__":
    main()
