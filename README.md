# copier - Бот для сохранения истории переписки в Telegram


Этот бот разработан с целью создания копии истории переписки. Может быть особенно полезен при случайном удалении диалога в Telegram (безопасная страховка от потери важных данных). Бот использует библиотеку Pyrogram для взаимодействия с Telegram API и обеспечивает испровизированную архивацию сообщений.

## Как это работает

Бот подключается к вашему аккаунту в Telegram с помощью предоставленных API ID и хеш-ключа. Он перенаправляет Вам в избранное все сообщения между Вами и указанным целевым пользователем в режиме реального времени. Если происходит удаление сообщения в диалоге, копия сообщения сохраняется в избранном.
## Установка и настройка

1. Убедитесь, что у вас установлен Python 3.
2. Клонируйте этот репозиторий или скачайте файлы.
3. Создайте файл `.env` в корневой папке и добавьте следующие переменные:
    - `MY_API_ID`: Ваш API ID, полученный при создании приложения в Telegram.
    - `MY_API_HASH_KEY`: Ваш хеш-ключ API.
    - `MY_ID`: Ваш идентификатор пользователя в Telegram.
    - `TARGET_ID`: Идентификатор целевого пользователя или чата, переписку с которым Вы хотите сохранить.
    - `RETRY_DELAY`: Задержка (в секундах) перед повторной отправкой, если что-то пойдет не так.

    `MY_API_ID` и `MY_API_HASH_KEY` можно получить, авторизовавшись на https://my.telegram.org/ и создав там приложение.<br>
    `MY_ID` и `TARGET_ID` можно получить через бота @userinfobot, отправив ему с целевого аккаунта команду /start.
   
5. Установите зависимости, запустив `pip install -r requirements.txt`.
6. Запустите бота с помощью команды `python3 main.py` (или `python3 main.py`, если Вы используете Windows).

## Важно

Бот сохраняет только простые текстовые сообщения.<br>
Бот не сохраняет сообщения, отправленные и полученные вне его времени работы.<br>
Бот не заменяет официальную архивацию или резервное копирование Ваших данных.<br>
Будьте осторожны с доступом к вашим API ключам и личным данным.<br>
Никогда не публикуйте файл `.env` в открытом доступе.

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для подробностей.

## Кстати

Еще бота можно использовать для скрытого прочтения сообщений, просто читайте их в Избранном! Пересылка не оставляет следов :)<br>

![Упс, тут был скриншот. Но ничего, он также добавлен в код example.png](https://github.com/twsomt/copier/blob/main/example.png)


