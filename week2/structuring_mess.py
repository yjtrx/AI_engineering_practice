## Importing the necessary libraries
import os
import json
import dotenv
dotenv.load_dotenv()
import re
from anthropic import AnthropicBedrock
import config
import sys_prompt
from test_signatures import test_signatures

## Importing the required configs
AWS_REGION = config.AWS_REGION
MODEL_NAME = config.MODEL_NAME

## Initializing the Claude API
client = AnthropicBedrock(aws_region=AWS_REGION)


## Defining the tool
tool = {
    "name":"structuring_messy_text",
    "description":"Helps with extraction of important information such as name, email and company",
    "input_schema":{
        "type":"object",
        "properties":{
            "name":{"type":"string","description":"The name of the person who sent the email."},
            "email":{"type":"string","description":"The email address of the person who sent the email."},
            "company":{"type":"string","description":"The name of the company where the person works."}
        },
        "required":["name","email","company"]
    }
}

for idx,tst_signs in enumerate(test_signatures):
    # print(tst_signs)
    # messages = [{"role":"user","content":tst_signs}]
    if idx == 0:
        continue
    messages = [{"role": "user", "content": tst_signs}]
    print(json.dumps(messages, indent=2, default=str))
    print('\n',messages)
    response = client.messages.create(
    model = MODEL_NAME,
    max_tokens = config.max_tokens,
    tools = [tool],
    messages = messages,
    system=sys_prompt.system_prompt
)
    print(f'\n{response.content}')
    if response.stop_reason == 'tool_use':
        print(json.dumps(response.content[-1].input, indent=2, default=str))
        with open("./structured_file.txt",'a+',encoding='utf-8') as fl:
            fl.write(tst_signs)
            fl.write(json.dumps(response.content[-1].input, indent=2, default=str))
            fl.write('\n')
    else:
        print('Only text block recieved.')
