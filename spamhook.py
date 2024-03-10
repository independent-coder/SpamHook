from discord_webhook import DiscordWebhook
import random
import os
from dotenv import load_dotenv
import colorama
import time

# Initialize colorama for cross-platform colored terminal text
colorama.init()

# Load environment variables from .env file
load_dotenv()

os.system('title SpamHook - Config - Made by P1NGU!')
done = 1

# Get values from environment variables
webhook_url = os.getenv('WEBHOOK_URL')
webhook_name = os.getenv('WEBHOOK_NAME', 'Default Webhook Name')
message = os.getenv('MESSAGE', 'Default Message')

# Use the retrieved values for the DiscordWebhook object
webhook = DiscordWebhook(url=webhook_url, username=webhook_name)

print(f'{colorama.Fore.BLUE}MADE BY {colorama.Fore.RED}P1NGU!')
time.sleep(2)


print(f"Checking values in .env:\n")
print(f"Current set webhook: {webhook_url}\n")
print(f"Current set webhook username: {webhook_name}\n")
print(f"Current set message: {message}\n")

os.system('title SpamHook - Enter number of messages to be sent! - Made by P1NGU!')
times = input(
    f'{colorama.Fore.GREEN}(Enter a NUMBER) {colorama.Fore.YELLOW}How many times do you want to spam with the webhook? {colorama.Style.RESET_ALL}>>> {colorama.Fore.YELLOW}') or 69

try:
    times = int(times)
except ValueError:
    print(
        f'{colorama.Fore.RED}Failed! {colorama.Fore.YELLOW}You did not enter a valid number!{colorama.Style.RESET_ALL}')

os.system('title SpamHook - Ready')
print(f'{colorama.Fore.GREEN}Ready! {colorama.Fore.YELLOW}The webhook "{webhook_name}" will spam {times} times! Starting in 5 seconds. CTRL+C to stop.{colorama.Style.RESET_ALL}\n')
time.sleep(5)

while done <= times:
    webhook.content = message
    webhook.execute()

    os.system(f'title SpamHook - Spamming! (#{done}) - Made by P1NGU!')
    print(
        f'{colorama.Fore.GREEN}Success! {colorama.Fore.YELLOW}Message sent "{message}"! (#{done}){colorama.Style.RESET_ALL}')
    done += 1


print(f'{colorama.Fore.GREEN}Report: {colorama.Fore.YELLOW}The webhook spammed {times} times!{colorama.Style.RESET_ALL}\n')
print(f'{colorama.Fore.BLUE}MADE BY {colorama.Fore.RED} P1NGU!')
os.system('PAUSE >nul')
