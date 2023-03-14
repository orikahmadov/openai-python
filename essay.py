import os
import time
import PyPDF2
import openai
from rich.prompt import Prompt
from rich.console import Console, Style
from datetime import datetime
API_KEY = os.environ["OPENAI_API_KEY"]
openai.api_key = API_KEY
console = Console()
current_year = datetime.now().strftime("%Y")
user_style = Style(color="cyan", bold=True)
bot_style = Style(color="green", bold=False)
waiting_style = Style(color="yellow", bold=True)
conversation = [{"role": "system", "content": f"You are my smart bot assistant and you help me with scientific research. Current year is {current_year}."}]
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    # ask for file name and page numbers
    language = Prompt.ask("For turkish type TR for English type EN: ").casefold()
    user_prompt = ""
    if language == "tr":
        user_prompt = ".Bu paragrafı TÜRKCE özetle! ve basitleştir! İyi yazılmış ve anlaşılır olmalıdır!"
    else:
        user_prompt = ".Summarize this paragraph and simplify it! It should be well written and easy to understand!"
    file_name = Prompt.ask("Enter the file name (including .pdf extension): ")
    start_page = int(Prompt.ask("Enter the start page: "))
    end_page = int(Prompt.ask("Enter the end page: "))
    pdf_file = open(file_name, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # extract text from pdf file
    page_range = range(start_page - 1, end_page)
    text = ''
    for page_number in page_range:
        page = pdf_reader.pages[page_number]
        text += page.extract_text()
    # split text into 500 word chunks
    text_chunks = text.split() # split text into words
    text_chunks = [' '.join(text_chunks[i:i+300]) for i in range(0, len(text_chunks), 300)] # split text into 500 word chunks
    for chunk in text_chunks: # loop through each chunk
        conversation.append({"role": "user", "content": chunk  + " " + user_prompt}) # add user input to conversation
        console.log("[bold red]User Input:[/bold red]", chunk + " " + user_prompt) # show user input
        print("\n") # add a new line
        response = openai.ChatCompletion.create( # get bot reply
           model = "gpt-3.5-turbo", 
           messages=conversation
        )
        reply_bot = response["choices"][0]["message"]["content"] # get bot reply
        console.log("[bold white]Bot Reply: ", reply_bot, style=bot_style) # show bot reply
        print("\n")
        conversation.append({"role": "system", "content": reply_bot})
    print(f"Finished summarizing text from {file_name} from page {start_page} to page {end_page}.\nIf you want to keep the conversation start program again and give new 6 pages\n E.g lets say you set the start page 1 and end page 6.\nYou must now set the start page 7 and end page 13 and so on.")

        
                
            

if __name__ == "__main__":
    main() # run the main function
