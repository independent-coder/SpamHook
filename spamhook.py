import os
import time
from dotenv import load_dotenv
import colorama
import threading
from discord_webhook import DiscordWebhook

colorama.init()
load_dotenv()

os.system('title SpamHook - Config - Made by P1NGU!')
done = 1

# Access webhook URLs
webhook_urls = os.getenv('WEBHOOK_URL')
webhooks = [url.strip() for url in webhook_urls.split(';')]

# Access single message
message = os.getenv('MESSAGE')

# Access single webhook name
webhook_name = os.getenv('WEBHOOK_NAME')

print(f'{colorama.Fore.BLUE}MADE BY {colorama.Fore.RED}P1NGU!\n')

# Print webhook URLs
if len(webhooks) > 1:
    print(f'{colorama.Fore.LIGHTMAGENTA_EX}Multiple webhooks detected:\n')
    for index, webhook_url in enumerate(webhooks, start=1):
        print(f"#{index} webhook: {webhook_url}\n")
else:
    print("Current set webhook(s):")
    for index, webhook_url in enumerate(webhooks, start=1):
        print(f"Webhook: {webhook_url}\n")

# Print single message
print(f"Current set message:\n{message}\n")

# Print single webhook name
print(f"Webhook Name: {webhook_name}\n")

# Function to send message
def send_message(webhook_url, webhook_index):
    global done
    webhook = DiscordWebhook(url=webhook_url, username=webhook_name)
    for _ in range(10):
        webhook.content = message
        webhook.execute()
        os.system(f'title SpamHook - Spamming! (#{done}) - Made by P1NGU!')
        print(
            f'{colorama.Fore.GREEN}Success! {colorama.Fore.YELLOW}Message sent "{message}"! (#{done}) by webhook #{webhook_index}{colorama.Style.RESET_ALL}')
        done += 1


# Get number of times to send message per webhook
os.system('title SpamHook - Enter number of messages to be sent per webhook! - Made by P1NGU!')
times_per_webhook = input(
    f'{colorama.Fore.GREEN}(Enter a NUMBER) {colorama.Fore.YELLOW}How many times do you want to spam with each webhook? {colorama.Style.RESET_ALL}>>> {colorama.Fore.YELLOW}') or 10
try:
    times_per_webhook = int(times_per_webhook)
except ValueError:
    print(
        f'{colorama.Fore.RED}Failed! {colorama.Fore.YELLOW}You did not enter a valid number!{colorama.Style.RESET_ALL}')

os.system('title SpamHook - Ready')
print(f'{colorama.Fore.GREEN}Ready! {colorama.Fore.YELLOW}Each webhook will spam {times_per_webhook} times with message "{message}"! Starting in 5 seconds. CTRL+C to stop.{colorama.Style.RESET_ALL}\n')
time.sleep(5)

# Send messages to all webhooks simultaneously using threading
threads = []
for index, webhook_url in enumerate(webhooks, start=1):
    thread = threading.Thread(target=send_message, args=(webhook_url, index))
    threads.append(thread)
    thread.start()


# Wait for all threads to finish
for thread in threads:
    thread.join()

total_messages_sent = len(webhooks) * times_per_webhook
print(f'{colorama.Fore.GREEN}Report: {colorama.Fore.YELLOW}Each webhook spammed {times_per_webhook} times! Total messages sent: {total_messages_sent}{colorama.Style.RESET_ALL}\n')

print(f'{colorama.Fore.BLUE}MADE BY {colorama.Fore.RED} P1NGU!')
os.system('PAUSE')
