import requests

generate_url = "http://localhost:11434/api/generate"
chat_url = "http://localhost:11434/api/chat"

response = requests.post(generate_url,json={"model":"llama3.2:3b-instruct-q8_0"})
print(response.status_code)

if response.status_code != 200:
    quit(0)

response= requests.post(chat_url,json={"model":"llama3.2:3b-instruct-q8_0",
                                       "messages":[{"role":"user",
                                                    "content":"Say hello to me please!" }
                                                   ]})
print(response.text)
