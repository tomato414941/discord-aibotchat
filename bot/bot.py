import logging
import os

import discord
from discord import app_commands
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
intents.message_content = True  # Enable message content intent
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Fetch conversation history from the channel
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


# Process user message and generate AI response
async def process_message(channel, user_message, use_history=True):
    current_model = "GPT-4o"  # Currently only supports GPT-4o

    try:
        if use_history:
            # Fetch conversation history and append the new user message
            history = await fetch_conversation_history(channel)
            history.append(HumanMessage(content=user_message))
        else:
            # If not using history, only use the current user message
            history = [HumanMessage(content=user_message)]

        # Initialize the language model
        llm = ChatOpenAI(
            temperature=0.7,
            openai_api_key=OPENAI_API_KEY,
            model_name=AVAILABLE_MODELS[current_model],
        )

        # Generate AI response
        ai_response = await llm.ainvoke(history)

        return ai_response.content

    except Exception as e:
        # Log any errors that occur during message processing
        logger.error(f"An error occurred while processing message: {str(e)}")
        return f"An error occurred: {str(e)}"


# Event handler for when the bot is ready
@client.event
async def on_ready():
    await tree.sync()
    logger.info(f"{client.user} has connected to Discord!")


# Event handler for when a message is received
@client.event
async def on_message(message):
    if message.author == client.user:  # Ignore messages from the bot itself
        return

    if client.user.mentioned_in(message):
        # Extract the content of the message after the mention
        content = message.content.replace(f"<@!{client.user.id}>", "").strip()

        if content:
            # Display typing indicator while generating response
            async with message.channel.typing():
                response = await process_message(message.channel, content)
            await message.channel.send(f"{message.author.mention} {response}")
        else:
            # If no content after the mention, send a greeting
            await message.channel.send(
                f"{message.author.mention} Hello! How can I assist you today?"
            )


# Slash command to ask the AI a question without conversation history
@tree.command(name="ask", description="Ask the AI assistant a question")
async def ask(interaction: discord.Interaction, message: str):
    await interaction.response.defer()  # Defer the response while processing
    response = await process_message(interaction.channel, message, use_history=False)
    await interaction.followup.send(f"{response}")


# Run the bot
client.run(DISCORD_TOKEN)
