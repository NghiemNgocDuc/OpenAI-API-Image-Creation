import openai
import requests
from PIL import Image
from io import BytesIO

openai.api_key= "API Key"



def generate_image(prompt):
    response = openai.Image.create(
        prompt = prompt,
        n=1,
        size = "1024x1024"
    )
    image_url = response["data"][0]["url"]
    return image_url

def show_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content)) # Transferring from binary data to real image
    img.show()


prompt = input("Enter a prompt")
image_url = generate_image(prompt)
show_image(image_url)
