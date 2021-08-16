import os

ENV = '#Enter your API keys here:\ndiscord_api=\nxiv_api=\n'


def main():
    env_path = os.getcwd() + '/.env'
    if not os.path.isfile(env_path):
        print('Dotenv file does not exist, creating...')
        with open(file=env_path, mode='w') as f:
            f.write(ENV)
    else:
        print('Dotenv file already exists.')


if __name__ == '__main__':
    main()
