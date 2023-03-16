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
conversation =   [{"role": "system", "content": """
-You will write a scientific paper or an essay based on the given topic and outline
-You will write concisely and clearly, and you will use correct grammar and spelling
-You will use the outline to write the essay
-You will write essay for the given number of words
"""
                   .format(current_year)}]
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    console.log("Welcome to the Openai chat!\nIf you want to quit the chat just type 'exit!'\nIf you want to quit chat and save conversation just press 'ctrl + c' and answer 'y'\n",style="yellow")
    console.log("This bot will write essay based on the outline provided by in given text file in essay_outlines folder\n",style="yellow")
    while True:
        try:
            file_input =  Prompt.ask("Enter the filaname for essay outline the program will read the file in essay_outlines folder: E.g 'tesla.txt' ")
            if file_input == "exit!":
                break
            #check if file exists
            elif not os.path.exists(f"essay_outlines/{file_input}"):
                #raise error if file does not exist
                raise FileNotFoundError
            else:
                #read the file and append the content to conversation
                with open(f"essay_outlines/{file_input}","r") as f:
                    outline = f.read()
                    words = int(input("Enter the number of words you want the essay to be: "))
                    conversation.append({"role": "user", "content": f"Write a precise,concise, clear essay based on the outline {outline} \nAnd write essay for {words} words"})
                    seperator  =  "*"*100 #Seperator for better readability
                    console.print("Please wait while I am thinking...",style=waiting_style)
                    response = openai.ChatCompletion.create( #Openai API call
                    model = "gpt-3.5-turbo", #Model used for completion
                    messages=conversation #Conversation history
                    )#End of API call
                    console.print(seperator,style="red")
                    bot_reply =  response.choices[0]["message"]["content"]
                    conversation.append({"role": "bot", "content": bot_reply})
                    #print the bot reply
                    console.print("Bot: {}".format(bot_reply),style="green")
                    
        except FileNotFoundError:
            console.print("File does not exist!",style="red")
            continue

        except Exception():
            console.print("Invalid input!",style="red")
            continue


if __name__ == "__main__":
    main()
