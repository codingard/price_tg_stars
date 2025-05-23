# TG Stars Converter Bot

Простой Telegram-бот для конвертации между валютами: TON, USDT и Telegram Stars. Показывает стоимость указанного количества валюты в Stars или обратно.

---

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Создайте виртуальное окружение и активируйте его:

```bash
python3 -m venv venv
source venv/bin/activate      # для Unix/macOS
venv\\Scripts\\activate         # для Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` в корне проекта и добавьте туда токен своего Telegram-бота:

```
BOT_TOKEN=ваш_токен_бота
```

---

## Запуск

```bash
python bot.py
```

---

## Формат сообщений боту

Сообщения должны содержать **сначала сумму**, затем **валюту** (через пробел). Например:

```
10 TON
5 usdt
120 старс
```

Бот вернёт стоимость, рассчитанную по текущему курсу.

---

## Поддерживаемые валюты

Поддерживаемые обозначения валют перечислены в `config.py` в переменной `CURRENCY_ALIASES`.

---

## Примечание

Если бот не отвечает, возможно, необходимо обновить hash. В будущем будет реализована автоматическая загрузка цен или добавлен отдельный гайд.
