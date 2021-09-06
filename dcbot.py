import discord
import requests
import json
import random

client = discord.Client()

sad_words = ["üzüldüm", "sıkıldım", "bunaldım", "bok", "hay", "of", "off", ":("]

start_enco = ["Sıkma canını değmez bro", "Kanka neşelen az", "Sen harikasın",
              "Deme öyle be"]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('sa'):
        await message.channel.send('as')
    if msg.startswith('as'):
        await  message.channel.send('nE')
    if msg.startswith('aga be'):
        await  message.channel.send('yak yak yak')
    if msg.startswith('inspire'):
        quote = get_quote()
        await  message.channel.send(quote)
    if any(word in msg for word in sad_words):
        quote = get_quote()
        await  message.channel.send(random.choice(start_enco))

client.run('ODg0MTk2MjI5OTQ3NDkwMzU0.YTU96A.iShA_dATjFSJ_TAh9EsZBsuM5qQ')
