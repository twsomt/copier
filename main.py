import os
import time
import logging
from dotenv import load_dotenv
from pyrogram import Client

# Логгинг
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

load_dotenv('.env')

# Загружаем переменные из .env
API_ID = int(os.getenv("MY_API_ID"))
API_HASH = os.getenv("MY_API_HASH_KEY")
MY_ID = int(os.getenv("MY_ID"))
TARGET_ID = int(os.getenv("TARGET_ID"))
RETRY_DELAY = int(os.getenv("RETRY_DELAY"))

# Создаем экземпляр клиента
app = Client(
    "my_account",
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
                    else f"{user.first_name} {user.last_name}")
    except TypeError:
        time.sleep(RETRY_DELAY)

    while True:
        try:
            if user_id == TARGET_ID:
                await (client.send_message(MY_ID,
                                           "Получено сообщение от "
                                           f"@{username}: {message.text}"))
            elif user_id == MY_ID:
                await (client.send_message(MY_ID,
                                           "Отправлено сообщение для "
                                           f"@{username}: {message.text}"))
  
            break  # Выходим если отправили
        except Exception as error:
            logger = logging.getLogger(__name__)
            logger.error(f"Произошла ошибка: {str(error)}")
            logger.info(f"Повторная попытка через {RETRY_DELAY} секунд...")
            time.sleep(RETRY_DELAY)

if __name__ == '__main__':
    app.run()
