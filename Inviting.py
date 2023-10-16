import requests
import time

def invite_to_group(username, group_id, bot_token):

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    
    params = {
        'chat_id': group_id,
        'text': f'/invite {username}'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(f'Пользователь {username} приглашен в группу.')
        time.sleep(864)                                 #   1728 - 50       864 - 100       576 - 150       432 - 200
    except requests.exceptions.HTTPError as err:
        print(f'Ошибка HTTP: {err}')
    except Exception as err:
        print(f'Ошибка при выполнении запроса: {err}')

with open('База.txt', 'r') as file:
    usernames = file.read().splitlines()

group_id = '5811779051'
bot_token = '6093538980:AAH1GhrsxreOGhJ1ZSRoX_xv_ERnPAP4wLE'

for username in usernames:
    invite_to_group(username, group_id, bot_token)