import discord
import os
import requests
import json

token = os.environ['token']
#Starting the bare minimum
client = discord.Client()

#Helper function
def get_pic():
  response = requests.get("https://api.thecatapi.com/v1/images/search")
  json_data = json.loads(response.text)
  url = json_data[0]['url']
  return url

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

  if message.content.startswith('&carmen'):
    await message.channel.send('hi my name is AUHHHH       winstead im AUGHHHHHH seventeen years old and i am very similar to you did i mention to you that i am AUGGHHHHHH group of girls pushed me down a sewer')
    
  if message.content.startswith('&cat'):
    await message.channel.send(get_pic())
    
  if message.content.startswith(':3'):
    await message.channel.send(':3')

  

#Playback commands
@client.event
async def play(ctx, url : str): 
  #Figure out how to connect to any call
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  await voiceChannel.connect()
client.run(token) #Runs the bot