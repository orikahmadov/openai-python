import chat
import image
import essay
import programmer_assistant
import create_essay
from rich.console import Console

#console is used to print the text in a better way
console = Console()

while True:
    console.print("Welcome to the Openai chat!",style="bold yellow")
    console.print("1. Chat (Chat with the bot about anything)",style="bold green")
    console.print("2. Create an image",style="bold cyan")
    console.print("3. Summarize given text from given PDF Pages (Must have pdf)",style="bold yellow")
    console.print("4. Programmer Assistant  (Describe what program does)",style="bold magenta")
    console.print("5. Write a research paper or an essay on a given topic")
    console.print("6. Exit",style="bold red")
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
        create_essay.main()
    elif choice == 6:
        print("Thank you for the chat! See you again")
        break
    else:
        print("Invalid choice")

