from g4f.client import Client
from g4f.cookies import set_cookies
import re

set_cookies(".bing.com", {
  "_U": "cookie value"
})

set_cookies(".google.com", {
  "__Secure-1PSID": "cookie value"
})
client = Client()


def generate(prompt):
    while True:
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt + '\nYour answer must contain less than 510 and more than 25 characters.'}])
        c = response.choices[0].message.content
        if len(c) >= 1:
            break
    return re.sub(r'[^а-яА-ЯёЁ0-9 ,.!?-]', '', c)
