# Employee Manager

REST API для обліку працівників і відділів (варіант 6).

## Features

- CRUD працівників і відділів
- Статистика зарплат по відділах
- SQLite + SQLAlchemy 2.0, міграції Alembic
- FastAPI, Swagger UI
- Паралельна аналітика (ThreadPool / ProcessPool / NumPy)
- Тести pytest
- Docker
- CI/CD (GitHub Actions)

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Configuration

```bash
cp .env.example .env
```

| Змінна | За замовчуванням | Опис |
|---|---|---|
| `APP_NAME` | `Employee Manager` | назва застосунку |
| `ENVIRONMENT` | `development` | `development` / `test` / `production` |
| `DATABASE_URL` | `sqlite:///employees.db` | адреса БД |
| `LOG_LEVEL` | `INFO` | рівень логування |

Файл `.env` не комітиться (є в `.gitignore`), у репозиторії лише `.env.example`.

## Run locally

```bash
alembic upgrade head
python -m uvicorn employee_manager.api:app --reload
```

## Docker

```bash
docker build -t employee-manager:1.0 .
docker run --rm -p 8000:8000 -e ENVIRONMENT=production employee-manager:1.0
```

З volume для SQLite:

```bash
docker run --rm -p 8000:8000 -v employee_data:/app/data employee-manager:1.0
```

## Tests and checks

```bash
pytest -v
ruff check .
ruff format --check .
mypy src
python -m build
```

## API docs

- http://localhost:8000/docs
- http://localhost:8000/health

## License

MIT