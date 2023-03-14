import chat
import image,essay
from rich.console import Console,Style
from pyarmor.pyarmor import main_entry
from pyarmor import __version__ 

console = Console()

while True:
    console.print("Welcome to the Openai chat!",style="bold yellow")
    console.print("1. Chat",style="bold green")
    console.print("2. Create an image",style="bold cyan")
    console.log("3. Create Essay",style="bold yellow")
    console.print("4. Exit",style="bold red")
    print("\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        chat.main()
    elif choice == 2:
        image.create_an_image()
    elif choice == 3:
        essay.main()
    elif choice == 4:
        print("Thank you for using our program!")
        break
    else:
        print("Invalid choice")

