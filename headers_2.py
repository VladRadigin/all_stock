import requests
import time
from random import choice

url = 'http://httpbin.org'

while line := open('user_agent.txt').read().split('\n'):
    user_agent = {'user-agent': choice(line)}
    response = requests.get(url=url, headers=user_agent)
    time.sleep(10)
    print(response.text)