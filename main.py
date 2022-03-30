import discord
import os
token = os.environ['token']
#Starting the bare minimum
client = discord.Client()

#Ready function
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))  

#Hello!
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('&hello'):
    await message.channel.send('Hello! AUGHHH')

client.run(token) #Runs the bot