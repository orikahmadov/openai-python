import chat
import image
from rich.console import Console,Style

console = Console()

while True:
    console.print("Welcome to the Openai chat!",style="bold yellow")
    console.print("1. Chat",style="bold green")
    console.print("2. Create an image",style="bold cyan")
    console.log("3. Exit",style="bold red")
    print("\n")
    choices = [1,2,3]
    choice = int(input("Enter your choice: "))
    if choice not in choices:
        continue
    if choice == 1:
        chat.main()
    elif choice == 2:
        image.create_an_image()
    elif choice == 3:
        break
    else:
        print("Invalid choice")

