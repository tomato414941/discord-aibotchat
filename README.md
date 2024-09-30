# Discord AI Bot Chat

**Boost your server's engagement with an AI companion!** 🤖

Discord AI Bot Chat is a LangChain-powered bot that seamlessly integrates into your Discord server, providing intelligent and engaging interactions with your community.

[**🔗 Invite the Bot to Your Server**](https://discord.com/oauth2/authorize?client_id=1288885047385915446&permissions=2147551232&integration_type=0&scope=bot)

## Features

* **Intelligent Conversations:** Engage in natural language conversations with the AI using the `/ask` command or simply by mentioning the bot.
* **Contextual Understanding:** The bot maintains conversation history, allowing for more contextually relevant and meaningful responses.
* **Powered by LangChain:** Leverages the power of LangChain for advanced language model interactions and seamless integration with OpenAI's GPT-4o.
* **Easy to Use:** Simple setup and intuitive commands make it easy for anyone to interact with the AI.
* **Always Improving:** We are constantly working to enhance the bot's capabilities and add new features.

## Project Structure

```
discord-aibotchat/
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

* `bot/`: Contains the core bot logic
    * `bot.py`: Implements the main bot functionality, slash commands, and event handlers
* `.env`: Stores environment variables (tokens, API keys, etc.)
* `.gitignore`: Specifies files that Git should ignore
* `requirements.txt`: Lists project dependencies
* `README.md`: This file

## Requirements

* Python 3.8+
* Discord Bot Token
* OpenAI API Key

## Setup

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/tomato414941/discord-aibotchat.git](https://github.com/tomato414941/discord-aibotchat.git)
   cd discord-aibotchat
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file and add the following content:**

   ```bash
   DISCORD_TOKEN=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```

   * Replace `your_discord_bot_token` with your actual Discord Bot Token.
   * Replace `your_openai_api_key` with your actual OpenAI API key.

5. **Run the bot:**

   ```bash
   python bot/bot.py
   ```

## Usage

1. **Using the `/ask` slash command:**
   * `/ask message:<your_message>` - Ask the AI a question without considering conversation history.

2. **Mentioning the bot:**
   * Simply mention the bot followed by your message, e.g., `@AI Bot Chat Hello, how are you?` The bot will consider the conversation history in the channel.

**Examples:**

```
/ask message:What's the weather like today?
@AI Bot Chat Tell me a joke about programming
```

**Note:** When you mention the bot or use the `/ask` command, you'll see a "typing" indicator while the AI generates its response.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please open an issue on this repository or contact [tomato414941@gmail.com](mailto:tomato414941@gmail.com).