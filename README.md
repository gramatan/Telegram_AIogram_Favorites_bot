# Telegram Extended Favorites bot
This project is a Telegram bot built with the Aiogram library. The bot manages user messages and allows them to save, forward, and categorize messages in different channels.

## Getting Started

Before running the bot, you need to create a config.py file with sensitive information such as tokens, database connection details, and chat IDs.

1. Create a new file in the project root directory called config.py.
2. Add the following variables to the file:
    ```
    BOT_TOKEN = "your_telegram_bot_token"
    
    LOCAL = your_chat_id
    NOTES = your_first_channel_id
    SAVED2 = your_second_channel_id
    LEARNING = your_third_channel_id
    SAVED3 = your_fourth_channel_id
    LAZADA = your_fifth_id
    FAMILY1 = your_sixth_channel_id
   
    HELP = "Bot help text"
    ```
3. Replace the placeholder values with your own Telegram bot token, and chat/channel IDs.

With the config.py file in place, you can now follow the How to Run instructions to build and run the bot and database services using Docker Compose.

## How to Run

1. Make sure Docker is installed on your system.
2. Open a terminal and navigate to the project root directory.
3. Run docker build -> docker run

The bot should now be running and connected to the specified chat/channel IDs.