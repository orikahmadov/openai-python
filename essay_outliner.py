import os
import openai
from datetime import datetime
from rich.console import Console,Style

API_KEY =  os.environ["OPENAI_API_KEY"]
openai.api_key = API_KEY
console =  Console()
current_year = datetime.now().strftime("%Y")
user_style =  Style(color="cyan",bold=True)
bot_style =  Style(color="green",bold=False)
waiting_style =  Style(color="yellow",bold=True)
essay_topic = ""
conversation =   [{"role": "system", "content": 
"""
-You are a my scientific advisor and a proffessor 
-You will help to write a scientific paper or an essay based on the given topic
Current year is {}.

""".format(current_year)}] #Conversation history


timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    global essay_topic
    console.print("Welcome to the Openai chat!\nIf you want to quit the chat just type 'exit!'\nIf you want to quit chat and save conversation just press 'ctrl + c' and answer 'y'\n",style="yellow")
    while True:
        try:
            outline_topic =  input("Enter the topic of the essay: E.g 'Tesla and Edison' ")
            if outline_topic == "exit!":
                break
            elif not outline_topic:
                console.print("Please enter a topic!",style="red")
                continue
            else:
                essay_topic += outline_topic
                conversation.append({"role": "user", "content": "Write an essay outline about {}".format(outline_topic)})
        except Exception():
            console.print("Invalid input!",style="red")
            continue
        console.print("Please wait while I am thinking...",style=waiting_style)
        response = openai.ChatCompletion.create( #Openai API call
                model = "gpt-3.5-turbo", #Model used for completion
                messages=conversation #Conversation history
            )#End of API call
        seperator  =  "*"*100 #Seperator for better readability
        console.print(seperator,style="red")
        bot_reply =  response.choices[0]["message"]["content"]
        conversation.append({"role": "bot", "content": bot_reply})
        console.print("Bot: {}".format(bot_reply),style="green")
        save =  input("Do you want to save the conversation? (y/n): ")
        if save == "y":
            save_conversation(essay_topic,bot_reply)
            break
        elif save == "n":
            break
        else:
            console.print("Invalid input!",style="red")
            continue

def save_conversation(essay_topic, bot_reply):
    if not os.path.exists("essay_outlines"):
        os.mkdir("essay_outlines")
    
    with open(f"essay_outlines/{essay_topic}_outline.txt", "w", encoding="utf-8")as file:
        if " "in essay_topic:
            essay_topic = essay_topic.replace(" ", "_")
            file.write(f"Topic: {essay_topic}\n")
            file.write(f"{bot_reply}\n")
        else:
            file.write(f"Topic: {essay_topic}\n")
            file.write(f"{bot_reply}\n")
            

if __name__ == "__main__":
    main()
