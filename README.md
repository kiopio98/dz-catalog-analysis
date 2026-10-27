# Аналитика каталога стримингового сервиса

ДЗ №1. Python 3.12, uv; единственная зависимость разработки — Ruff.

```console
uv sync --locked
uv run catalog_analysis.py
uv run ruff check .
```

Исходный каталог находится в начале `catalog_analysis.py`. При импорте модуль
ничего не печатает. Единственная точка входа отчёта — `build_report(movies)`.
Все вычисления выполняются стандартными средствами Python, без pandas/numpy.
