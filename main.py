import chat
import image
import summarize_text
import programmer_assistant
import essay_outliner
import generate_essay_from_outline
from rich.console import Console

console = Console()

while True: #Main menu
    console.print("Welcome to the Openai chat! (General Chat)",style="bold yellow")
    console.print("1.(GPT-3.4 Turbo) Chat (Chat with the bot about anything)",style="bold green")
    console.print("2. Create an image (E.g Draw a cat in Dali style)",style="bold cyan")
    console.print("3. Summarize and Simplify text from PDF (Pass pdf as input)",style="bold yellow")
    console.print("4. Create a program (Writes pseudecode and program)",style="bold magenta")
    console.print("5. Create an essay (Writes an essay outline)",style="bold blue")
    console.print("6. Write essay based on outline file",style="bold purple")
    console.print("7. Exit",style="bold red")
    print("\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        chat.main()
    elif choice == 2:
        image.main()
    elif choice == 3:
        summarize_text.main()
    elif choice == 4:
        programmer_assistant.main()
    elif choice == 5:
        essay_outliner.main()
    elif choice == 6:
        generate_essay_from_outline.main()
    elif choice == 7:
        console.print("Thank you for using the Openai chat!",style="bold green")
        break


    else:
        console.print("Invalid choice!",style="bold red")


