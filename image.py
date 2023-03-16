import openai
import requests
import os

""" This is a simple chatbot that uses the OpenAI API to generate an image"""

API_KEY = os.environ["OPENAI_API_KEY"]

url =  "https://api.openai.com/v1/images/variations"
def create_an_image():
    while True:
        try:
            print("Welcome to the image creator!")
            user_input = input("Describe an image: ")
            if user_input == "exit!":
                print("Bye!")
                break
            n_times =  int(input("How many images do you want to create? "))
            number_of_images = 0
            if n_times > 1:
                number_of_images = n_times
            elif n_times > 10:
                print("Sorry, you can only create 10 images at a time.")
                number_of_images = 10
            else:
                number_of_images = 1
            response =  openai.Image.create(
                prompt=user_input,
                n=number_of_images,
                size = "1024x1024"
            )
            if response:
                #download the image and save it
                for i in range(number_of_images):
                    image_url = response["data"][i]["url"]
                    image_data = requests.get(image_url).content
                    name_of_image =  hash(user_input) + i
                    if not os.path.exists("images"):
                        os.mkdir("images")
                    with open(f"images/{name_of_image}.jpg", "wb") as handler:
                        handler.write(image_data)
                print(f"Image created {os.path.abspath('images')}")
            else:
                print("Sorry, I couldn't create an image for you.")
        except KeyboardInterrupt:
            print("Bye!")
            break
        except Exception as e:
            print("Sorry, I couldn't create an image for you.")
            print(e)




if __name__ == "__main__":
    create_an_image()





    


