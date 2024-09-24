# Firebase Token Fetcher

A simple Python script to retrieve a Firebase Bearer Token using email and password authentication. The script allows
configuration to either print the token to the terminal or copy it directly to the clipboard.

## Features

- Retrieve Firebase Bearer Token via Firebase REST API.
- Option to print the token to the terminal.
- Option to copy the token to the clipboard.
- Configurable via the script's variables.

## Requirements

- Python 3.x
- `requests` library
- `pyperclip` library

You can install the required libraries using the following commands:

  ```bash
  pip install requests
  pip install pyperclip
  ```

## Configuration

Before running the script, you need to configure the following variables at the top of the script. Make sure to properly
set each one:

- `API_KEY`:
    - **Description**: Your Firebase project's Web API Key.
    - **Example**: `'AIzaSyBEXAMPLEKEYqwerty123456'`

- `EMAIL`:
    - **Description**: The email address of the Firebase user you wish to authenticate.
    - **Example**: `'user@example.com'`

- `PASSWORD`:
    - **Description**: The password for the Firebase user you want to authenticate.
    - **Example**: `'yourpassword123'`

- `SHOW_IN_TERMINAL`:
    - **Description**: Controls whether the Bearer Token should be printed to the terminal.
    - **Values**: Set to `True` to print the token to the terminal, or `False` to suppress terminal output.
    - **Example**: `True`

- `COPY_TO_CLIPBOARD`:
    - **Description**: Determines whether the Bearer Token should be copied to your system clipboard.
    - **Values**: Set to `True` to copy the token to the clipboard, or `False` to disable this functionality.
    - **Example**: `True`

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/GTRows/firebase-token-fetcher.git
   ```

2. Configure the script by setting the required variables in the script itself.

3. Run the script:
   ```bash
   python3 firebase_token_fetcher.py
   ```

## License

This project is licensed under the MIT License.
