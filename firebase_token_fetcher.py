import requests
import json
import pyperclip
import sys

# Configurations (These must be set before running the script)
API_KEY = ''  # Your Firebase API key
EMAIL = ''  # User email
PASSWORD = ''  # User password
SHOW_IN_TERMINAL = True  # True: Print token to terminal, False: Do not print
COPY_TO_CLIPBOARD = True  # True: Copy token to clipboard, False: Do not copy


def validate_config():
    if not API_KEY or not EMAIL or not PASSWORD:
        print("Error: API_KEY, EMAIL, and PASSWORD must be set in the configuration.")
        sys.exit(1)


def get_bearer_token(api_key, email, password):
    url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}'
    payload = {
        'email': email,
        'password': password,
        'returnSecureToken': True
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        token = response.json().get('idToken')
        return token
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    try:
        validate_config()
        bearer_token = get_bearer_token(API_KEY, EMAIL, PASSWORD)

        if COPY_TO_CLIPBOARD:
            pyperclip.copy(bearer_token)
            print("Bearer token has been copied to clipboard.")

        if SHOW_IN_TERMINAL:
            print(f"Bearer Token: {bearer_token}")
    except Exception as e:
        print(f"Error: {str(e)}")
