import secrets
import click
from dotenv import load_dotenv, set_key
import os

@click.command()
@click.option('--length', type=int, default=32, help='Length of the secret key')
@click.option('--env-file', type=str, default='.env', help='Path to the .env file')
@click.option('--key-name', type=str, default='SECRET_KEY', help='Name of the secret key in the .env file')
def generate_secret_key(length, env_file, key_name):
    try:
        secret_key = secrets.token_urlsafe(length)

        if os.path.exists(env_file):
            load_dotenv(env_file)
            set_key(env_file, key_name, secret_key)
        else:
            set_key(env_file, key_name, secret_key)

        print('Secret key generated and stored in', env_file)
    except Exception as e:
        print('An error occurred:', str(e))

if __name__ == '__main__':
    generate_secret_key()