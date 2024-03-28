# SpamHook

SpamHook is a simple Python script for spamming a defined message in a Discord server using a webhook.

## Features

- Sends repetitive messages to a Discord server using a webhook.
- Easy configuration through environment variables.

## Prerequisites

Before using SpamHook, make sure you have the following:

- Python installed on your machine with python.exe added to PATH.
- Required Python packages installed. You can install them using the following command:
  ```bash
  pip install discord-webhook python-dotenv colorama
  ```

## Setup

1. **Clone the repository to your local machine.**
   ```bash
   git clone https://github.com/independent-coder/SpamHook.git
   ```
2. Navigate to the project directory.
   ```bash
   cd SpamHook
   ```
3. Create a .env file in the project directory with the following information:

   ```env
   WEBHOOK_URL=<your_discord_webhook_urls_separated_by_semicolon>
   WEBHOOK_NAME=<your_webhook_name>
   MESSAGE=<your_spam_message>
   ```

## Usage

1. **Run the script by executing the following command:**
   ```bash
   python spamhook.py
   ```
2. Follow the on-screen instructions to set the number of messages to be sent and other configurations.
3. The script will start spamming the specified message to the Discord server using the configured webhooks.

## Disclaimer

This script is intended for educational purposes only. Use it responsibly and respect Discord's [Terms of Service](https://discord.com/terms).

**Author:**

- Independent-Coder(P1NGU!)
  - GitHub: [Independent-coder](https://github.com/independent-coder/)

Please be aware of the potential consequences of using this script inappropriately. I and contributors are not responsible for any misuse or violation of terms.
