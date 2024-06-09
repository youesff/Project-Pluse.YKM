import os

def get_current_username():
    return os.getenv("USERNAME")

current_username = get_current_username()
x = print(f"Current Windows username: {current_username}")