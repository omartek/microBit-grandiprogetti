# https://italiancoders.it/telepot-python-interface-to-telegram-bot-api/


import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import time

def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)

    username = msg['from']['username']
    user_id = msg['from']['id']
    
    if content_type == 'text':
        text = msg['text']
    


TOKEN = '703938665:AAF8eN9pHGgdQ6qspWNu6yFdVGWCvJc4W5c'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)