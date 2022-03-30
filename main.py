import discord
import os
token = os.environ['token']
#Starting the bare minimum
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))  

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('&hello'):
    await message.channel.send('Hello! AUGHHH')

client.run(token)