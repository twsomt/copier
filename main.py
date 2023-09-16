import logging
import os
import time
from dotenv import load_dotenv
from pyrogram import Client
from custom_exceptions import MissingVariable

# Логгинг
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Загружаем переменные из .env
load_dotenv('.env')
API_ID = os.getenv('MY_API_ID')
API_HASH = os.getenv('MY_API_HASH_KEY')
MY_ID = os.getenv('MY_ID')
TARGET_ID = os.getenv('TARGET_ID')
RETRY_DELAY = os.getenv('RETRY_DELAY')

# Проверяем наличие всех необходимых переменных
required_variables = {
    'API_ID': API_ID,
    'API_HASH': API_HASH,
    'MY_ID': MY_ID,
    'TARGET_ID': TARGET_ID,
    'RETRY_DELAY': RETRY_DELAY
}
missing_variable = {
    key for key, value in required_variables.items() if value is None
}
if missing_variable:
    logger.critical(
        'Отсутствуют следующие обязательные переменные в .env:'
        f'{", ".join(missing_variable)}'
    )
    raise MissingVariable(missing_variable)

# Преобразуем переменные в целые числа, если они существуют
API_ID = int(API_ID)
MY_ID = int(MY_ID)
TARGET_ID = int(TARGET_ID)
RETRY_DELAY = int(RETRY_DELAY)

# Создаем экземпляр клиента
app = Client(
    'my_account',
    api_id=API_ID,
    api_hash=API_HASH
)


# Фильтруем все сообщения
@app.on_message()
async def forward_all_messages(client, message):

    try:
        user_id = message.from_user.id
        user = await client.get_users(TARGET_ID)
        username = (user.username
                    if user.username
                    else f'{user.first_name} {user.last_name}')
    except TypeError:
        time.sleep(RETRY_DELAY)

    while True:
        try:
            if user_id == TARGET_ID:
                await (client.send_message(MY_ID,
                                           'Получено сообщение от '
                                           f'@{username}: {message.text}'))
            elif user_id == MY_ID:
                await (client.send_message(MY_ID,
                                           'Отправлено сообщение для '
                                           f'@{username}: {message.text}'))

            break  # Выходим если отправили
        except Exception as error:
            logger.error(f'Произошла ошибка: {str(error)}')
            logger.info(f'Повторная попытка через {RETRY_DELAY} секунд...')
            time.sleep(RETRY_DELAY)

if __name__ == '__main__':
    app.run()
