## Описание
Проект QRKot - сервис благотворительного фонда поддержки котиков QRKot собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
## Запуск сервиса

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/Ogyrecheg/QRkot_spreadsheets.git
```

```bash
cd QRkot_spreadsheets
```

Создать файл .env

* Если у вас Linux/MacOS
    ```bash
    touch .env
    ```

* Если у вас Windows

    ```bash
    type nul > .env
    ```

Заполнить файл .env:

```
APP_TITLE=Пожертвование в благотворительный фонд поддержки котиков QRKot
DESCRIPTION=Пожертвования на цели связанные с поддержкой кошачьей популяции.
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=your_secret
FIRST_SUPERUSER_EMAIL=admin@test.com
FIRST_SUPERUSER_PASSWORD=your_password
# Переменные Google API
DATABASE_URL=
FIRST_SUPERUSER_EMAIL=
FIRST_SUPERUSER_PASSWORD=
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
EMAIL=
```

Создать и активировать виртуальное окружение:

```bash
python -3.9 -m venv venv
```

* Если у вас Linux/MacOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Создать базу данных:
```bash
alembic upgrade head
```

Выполнить запуск сервиса:

```bash
uvicorn app.main:app --reload
```

---

## Доступ к спецификаций API сервиса
```http
http://127.0.0.1:5000/docs
```

**Технологии:**
- Python
- FastAPI
- SQLAlchemy
- Google API

### Автор проекта:
[Шевченко Александр](https://github.com/Ogyrecheg)
