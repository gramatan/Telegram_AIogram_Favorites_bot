# Telegram Extended Favorites bot
This project is a Telegram bot built with the Aiogram library. The bot manages user messages and allows them to save, forward, and categorize messages in different channels. It uses PostgreSQL as its database to store user and bot activity logs.

## Getting Started

Before running the bot, you need to create a config.py file with sensitive information such as tokens, database connection details, and chat IDs.

1. Create a new file in the project root directory called config.py.
2. Add the following variables to the file:
    ```
    BOT_TOKEN = "your_telegram_bot_token"
    DB_CONNECTION = "postgres://user:password@localhost/dbname"
    
    LOCAL = your_chat_id
    NOTES = your_first_channel_id
    SAVED2 = your_second_channel_id
    LEARNING = your_third_channel_id
    SAVED3 = your_fourth_channel_id
    LAZADA = your_fifth_id
    FAMILY1 = your_sixth_channel_id
   
    HELP = "Bot help text"
    ```
3. Replace the placeholder values with your own Telegram bot token, PostgreSQL connection strings, and chat/channel IDs.

With the config.py file in place, you can now follow the How to Run instructions to build and run the bot and database services using Docker Compose.

## How to Run

1. Make sure Docker and Docker Compose are installed on your system.
2. Open a terminal and navigate to the project root directory.
3. Run docker-compose up -d to build and start the bot and database services.

The bot should now be running and connected to the specified chat/channel IDs.