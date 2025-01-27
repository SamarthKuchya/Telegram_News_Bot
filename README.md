# Telegram News Bot

This project is a Telegram bot built using Python, Flask, and Dialogflow. The bot fetches and delivers news articles to users based on their queries or selected topics. It also supports small talk and custom intents defined in Dialogflow.

## Features

- Fetch news articles by category (e.g., World, Technology, Entertainment, etc.).
- Respond to user messages with small talk or other custom replies using Dialogflow.
- Interactive news topic selection with a keyboard interface.
- Handles text messages, commands, and stickers.

---

## Project Structure

### Files:
1. **`Bot.py`**
   - Handles the core functionality for fetching news and integrating with Dialogflow.
   - Functions:
     - `detect_intent_from_text`: Queries Dialogflow for intent detection.
     - `fetch_news`: Fetches news articles using the `gnewsclient` library.
     - `get_reply`: Processes user queries and fetches appropriate responses based on intent.

2. **`utils.py`**
   - Contains helper functions for fetching news and parsing user queries.

3. **`app.py`**
   - Manages the Telegram bot’s webhook and command handlers.
   - Implements Flask routes to handle webhook updates from Telegram.
   - Defines handlers for commands (`/start`, `/help`, `/news`) and messages (text and stickers).

4. **`requirements.txt`**
   - Lists the dependencies required to run the bot (e.g., Flask, python-telegram-bot, google-cloud-dialogflow).

---

## Prerequisites

1. **Python**: Make sure Python 3.7+ is installed on your system.
2. **Google Cloud Account**:
   - Create a Dialogflow agent in Google Cloud Platform.
3. **Telegram Bot Token**:
   - Create a bot using [BotFather](https://core.telegram.org/bots#botfather) on Telegram.
   - Obtain the bot token.

---

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SamarthKuchya/Telegram_News_Bot
   cd Telegram_News_Bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file or export the variables directly:
   ```
   export url_link="<your_ngrok_or_server_url>"
   export token="<your_telegram_bot_token>"
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Set up webhook**:
   The webhook is automatically configured to:
   ```
   <url_link>/<token>
   ```

---

## Usage

1. Start the bot on Telegram using the `/start` command.
2. Use `/news` to fetch news articles by selecting a category.
3. Send text messages to interact with the bot (e.g., "Tell me about sports" or "What's happening in tech?").
4. Use `/help` for guidance on using the bot.
5. Send stickers for fun interactions.

---

## Bot Commands

- `/start` - Greet the user and start the bot.
- `/help` - Display help text.
- `/news` - Prompt the user to choose a news category.

---

## Dependencies

- **Flask**: For setting up the webhook.
- **python-telegram-bot**: For handling Telegram bot interactions.
- **google-cloud-dialogflow**: For natural language processing with Dialogflow.
- **gnewsclient**: For fetching news articles.
- **os**: For managing environment variables.

---

## Troubleshooting

1. **Webhook Issues**:
   - Ensure your server or ngrok URL is accessible and the webhook is properly configured.
   - Verify the bot token and `url_link` are correctly set.

2. **Dialogflow Errors**:
   - Confirm your Dialogflow agent is active and configured with intents.

3. **Dependency Errors**:
   - Ensure all dependencies are installed by running `pip install -r requirements.txt`.

---

## Future Enhancements

- Add support for more languages and locations for fetching news.
- Enable inline query support for quick news access.
- Implement user authentication for personalized news preferences.
- Improve error handling and logging.

---

## License
This project is open-source and available under the MIT License.

---

## Author
Created by **Samarth**. Feel free to contribute or provide feedback!

