# Discord AI Bot Chat

Discord AI Bot Chat is a LangChain-powered bot that operates on Discord servers. Users can interact with AI using slash commands or by mentioning the bot.

## Features

- Interact with AI using the `/ask` slash command or by mentioning the bot
- Seamless AI integration within Discord servers
- Utilizes Discord.py V2 for modern bot functionality
- Implements LangChain for advanced language model interactions
- Maintains conversation history when mentioning the bot
- Utilizes the GPT-4o AI model
- Displays "typing" indicator while generating responses

## Project Structure

```
discord-aibot/
│
├── bot/
│   ├── __init__.py
│   └── bot.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

- `bot/`: Directory containing the main bot logic
  - `bot.py`: Implements the main bot functionality, slash commands, and event handlers
- `.env`: Stores environment variables (tokens, API keys, etc.)
- `.gitignore`: Specifies files that Git should ignore
- `requirements.txt`: Lists project dependencies
- `README.md`: Provides project description and setup instructions

## Requirements

- Python 3.8+
- Discord Bot Token
- OpenAI API Key

## Setup

1. Clone the repository:

   ```
   git clone [https://github.com/tomato414941/discord-aibotchat.git](https://github.com/tomato414941/discord-aibotchat.git)
   cd discord-aibotchat
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add the following content:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Run the bot:

   ```
   python bot/bot.py
   ```

## Usage

After inviting the bot to your Discord server, you can interact with it in two ways:

1. Using the `/ask` slash command:
   - `/ask message:<your_message>` - Ask the AI a question without considering conversation history.

2. Mentioning the bot:
   - Simply mention the bot followed by your message, e.g., "@AI Bot Chat Hello, how are you?" The bot will consider the conversation history in the channel.

Examples:
```
/ask message:What's the weather like today?
@AI Bot Chat Tell me a joke about programming
```

Note: When you mention the bot or use the `/ask` command, you'll see a "typing" indicator while the AI generates its response.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)