import discord
from project_blue import discord_entry

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Determine whether the message is from the internal or a user

    # parse message

    # Validate message

    # Enqueue message request

