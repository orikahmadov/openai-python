import chat
import image,essay
import programmer_assistant
from rich.console import Console,Style

console = Console()

while True:
    console.print("Welcome to the Openai chat! (General Chat)",style="bold yellow")
    console.print("1. Chat (Chat with the bot about anything)",style="bold green")
    console.print("2. Create an image (E.g Draw a cat in Dali style)",style="bold cyan")
    console.print("3. Summarize and Simplify text from PDF (Pass pdf as input)",style="bold yellow")
    console.print("4. Create a program (Writes pseudecode and program)",style="bold magenta")
    console.print("5. Exit",style="bold red")
    print("\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        chat.main()
    elif choice == 2:
        image.create_an_image()
    elif choice == 3:
        essay.main()
    elif choice == 4:
        programmer_assistant.main()
    elif choice == 5:
        break
    else:
        console.print("Invalid choice!",style="bold red")


