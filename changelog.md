# Changelog

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
