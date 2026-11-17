import pytest

from employee_manager.config import Settings


def test_default_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in ("ENVIRONMENT", "LOG_LEVEL", "DATABASE_URL"):
        monkeypatch.delenv(name, raising=False)

    settings = Settings(_env_file=None)

    assert settings.environment == "development"
    assert settings.log_level == "INFO"
    assert settings.database_url == "sqlite:///employees.db"


def test_settings_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ENVIRONMENT", "production")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("DATABASE_URL", "sqlite:////app/data/employees.db")

    settings = Settings(_env_file=None)

    assert settings.environment == "production"
    assert settings.log_level == "DEBUG"
    assert settings.database_url == "sqlite:////app/data/employees.db"
