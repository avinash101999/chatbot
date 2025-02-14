from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup

# Replace these with your own values
api_id = '20525228'
api_hash = 'c4c7ee1cdcdd5c4dab2c35b65e13985d'
bot_token = 'Y7389963665:AAGRkRSYdfN36FkHYq3U09Hyna74v5_gKGA'

client = TelegramClient('bot', 20525228, c4c7ee1cdcdd5c4dab2c35b65e13985d).start(bot_token=Y7389963665:AAGRkRSYdfN36FkHYq3U09Hyna74v5_gKGA)

@client.on(events.NewMessage)
async def handler(event):
    message = event.message.message

    if message.startswith('/search'):
        query = message[len('/search '):]
        results = search_web(query)
        await event.reply(results)
    else:
        await event.reply(f'You said: {message}')

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for g in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
        results.append(g.get_text())
    return '\n'.join(results)

client.run_until_disconnected()
