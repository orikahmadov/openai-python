# openai-python
Openai Chat.py

Main.py
I have created each scripts are doing different things.
Main.py is the main menu of the program, which inports other scripts.

Main.py: I have created scripts that perform different functions. Main.py is the main menu of the program, which imports other scripts.

1. Chat.py
2. Image.py
3. Summarize_text.py
4. Programmer Assistant
5. Essay Outliner.py
6. Generate Essay from Outline
7. Exit

1. Chat.py is a chat completion model of OpenAI, which is trained on a large collected dataset called WebText. So, Chat.py is just talking with the chatbot.

2. Image.py sends requests to DALL-E, which is an AI model trained and used for creating images. When the script is called, the user is required to give a description of an image, for example, "Flying cat in the galaxy in pixels." The more descriptive and precise input you give, the better the results will be.

3. Summarize_text.py is a clone of Chat.py with an added feature that extracts text from a PDF file and splits it into chunks of words. It then passes all of these as input to the bot. On behalf of the user, it asks to summarize and simplify the paragraph for each extracted text. It also saves the summarized paragraph by the bot.

4. Programmer Assistant is a cloned chat but with different specified instructions provided to the bot to break down the large complex problem into smaller tasks and write pseudo code. For example, "a program that scrapes Hacker News for the latest news and displays them to the user."

5. Essay Outliner writes concise outlines for a given essay topic.

6. Generate_essay_from_outline will write an essay based on the generated essay outline in the fifth section.
