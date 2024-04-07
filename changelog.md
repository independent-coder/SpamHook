# Changelog

## Version V2 to V3

### Added

- **Environment Variable Validation:** Added validation checks for environment variables (`WEBHOOK_URL`, `MESSAGE`, `WEBHOOK_NAME`) to ensure they are present in the `.env` file. Raises a `ValueError` if any of them are missing.

### Modified

- **Library Update:** Updated the `discord_webhook` library import statement to match the library name.
- **Console Output:** Adjusted console output messages for better readability and user understanding.
- **Webhook Printing:** Changed the printing of webhook URLs to handle both single and multiple webhook scenarios.
- **Error Handling:** Enhanced error handling within the `send_message` function to handle rate limiting errors (HTTP 429) and other webhook exceptions.

### Removed

- **Single Message Loop:** Removed the redundant loop for sending messages within the `send_message` function, as the loop now runs based on the `times_per_webhook` variable outside the function.

### Miscellaneous

- **Thread Starting:** Corrected the logic for starting threads to avoid duplicated starting of threads.
- **Thread Joining:** Adjusted the logic for joining threads to ensure all threads finish before proceeding with the report.
- **Console Output:** Improved console output messages for better user feedback and clarity during execution.

## Version V1 to V2

### Added

- **Multiple Webhook Support:** The ability to use multiple webhook URLs separated by semicolons.
- **Threading:** Threads are used to send messages to all webhooks simultaneously, improving efficiency.
- **Configurability:** Users can now specify the number of times to send a message per webhook.

### Modified

- **Message Sending Logic:** Refactored the message sending logic to use a function for better readability and scalability.
- **Console Output:** Improved console output messages for better user feedback during execution.
- **Environment Variable Handling:** Changed environment variable names for clarity and consistency.

### Removed

- **Single Webhook Restriction:** Removed the restriction of using only a single webhook URL.
- **Static Number of Messages:** Users are no longer restricted to a static number of messages; they can now configure the number of messages per webhook.

### Miscellaneous

- **Code Refactoring:** Improved code structure and readability.
- **Error Handling:** Added error handling for invalid user inputs.
