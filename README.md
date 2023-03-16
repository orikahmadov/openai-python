# openai-python
Openai Chat.py

Main.py
I have created each scripts are doing different things.
Main.py is the main menu of the program, which inports other scripts.

1.Chat.py
2.Image.py
3.Summarize_text.py
4.Programmer Assistant
5.essay_outliner.py
6.generate_essay_from_outline
7.Exit

1.Chat.py is a chat completion model of OpenAI which is trained on large collected
Dataset called WebText. So chat.py here is doing nothing than just talking with the chatbot.


2.Image.py this script is sending requests to the DALL-E which
Is an AI model trained and used for creating images.
When the script is called, user is required to give a description of an image 
E.g "Flying cat in the galaxy in pixels" the more descriptive, precise Input
You give, the better results will be. 

3.Summarize_text.py essay py is the clone of Chat.py, added a feature that extracts the text from pdf file and
splits this huge text into chunks of words then passes all these as input to the bot. Also on behalf of user
It asks to summarize, simplify the paragraph for each extracted text.
It also saves the summarized paragraph by bot.

4. Programmer Assistant is nothing than a cloned Chat but with
different specified instructions provided to the bot to 
break the large complex problem into smaller tasks and  write pseudo code
E.g 'a program that scraps the Hackernews for latest news and 
displays them to the user' 

5.Essay Outliner writes concise outlines for given essay topic

6.generate_essay_from_outline will write essay based on generated essay outline in 5th section

