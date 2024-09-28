import os

import discord
from discord import app_commands
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Discord Bot Token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Available models
AVAILABLE_MODELS = {
    "GPT-4o": "gpt-4o",
}

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


async def fetch_conversation_history(channel, limit=10):
    messages = []
    async for message in channel.history(limit=limit):
        if message.author == client.user:
            messages.append(AIMessage(content=message.content))
        else:
            messages.append(
                HumanMessage(content=f"{message.author.name}: {message.content}")
            )
    return list(reversed(messages))


async def process_message(channel, user_message, use_history=True):
    current_model = "GPT-4o"

    try:
        if use_history:
            history = await fetch_conversation_history(channel)
            history.append(HumanMessage(content=user_message))
        else:
            history = [HumanMessage(content=user_message)]

        llm = ChatOpenAI(
            temperature=0.7,
            openai_api_key=OPENAI_API_KEY,
            model_name=AVAILABLE_MODELS[current_model],
        )
        ai_response = await llm.ainvoke(history)

        return ai_response.content

    except Exception as e:
        return f"An error occurred: {str(e)}"


@client.event
async def on_ready():
    await tree.sync()
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        content = message.content.replace(f"<@!{client.user.id}>", "").strip()
        if content:
            async with message.channel.typing():
                response = await process_message(message.channel, content)
            await message.channel.send(f"{message.author.mention} {response}")
        else:
            await message.channel.send(
                f"{message.author.mention} Hello! How can I assist you today?"
            )


@tree.command(name="ask", description="Ask the AI assistant a question")
async def ask(interaction: discord.Interaction, message: str):
    await interaction.response.defer()
    response = await process_message(interaction.channel, message, use_history=False)
    await interaction.followup.send(f"{response}")


# Run the bot
client.run(DISCORD_TOKEN)
