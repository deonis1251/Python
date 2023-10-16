import asyncio
from telethon.sync import TelegramClient

api_id = 29890909  # Ваш API ID
api_hash = '100cd2494599df5ee2b3f5537b2f1e8e'  # Ваш API Hash
phone_number = '+905067355204'  # Ваш номер телефона, включая код страны

async def get_channel_subscribers(channel_link):
    subscribers = []
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.connect()

        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            await client.sign_in(phone_number, input('Введите код подтверждения: '))

        channel = await client.get_entity(channel_link)
        participants = await client.get_participants(channel)

        for participant in participants:
            if participant.username is not None:
                subscribers.append(participant.username)

    return subscribers

def write_subscribers_to_file(subscribers, file_path):
    with open(file_path, 'w') as file:
        for subscriber in subscribers:
            file.write(f"@{subscriber}\n")

channel_link = 'https://t.me/mplace_wildberries'  # Ссылка на ваш канал     7 705 458 91 51
subscribers = asyncio.run(get_channel_subscribers(channel_link))

file_path = 'subscribers.txt'  # Путь к файлу .txt, куда будут сохранены подписчики
write_subscribers_to_file(subscribers, file_path)

num_subscribers = len(subscribers)
print("Количество подписчиков:", num_subscribers)
print("Подписчики канала сохранены в файле:", file_path)