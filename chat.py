# Importing libraries
import os
from dotenv import load_dotenv
from google import genai


load_dotenv() # Calling for env variables

# The API request for call and recieve from google's gemini-3.7-flash
client = genai.Client(api_key=os.environ["api_key"])
temp = input('Enter the temperature: ')
interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input="Explain how AI works in a few words",
    generation_config={
        "temperature":temp
        }
)
print(interaction.output_text) # Printing the output
# Saving the outputs to the file
with open('output.txt',"a",encoding='utf-8') as f:
    f.write(f'Temperature:{temp}\nResponse:{interaction.output_text}\n')
    f.write('*'*100)
    f.write('\n')