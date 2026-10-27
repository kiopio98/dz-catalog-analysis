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

## Как устроено решение

| Этап | Задачи | Основные функции и конструкции |
| --- | --- | --- |
| 1 | 1–3 | `average_rating`, `catalog_age_stats`, `duration_in_hours`: `round`, `math.ceil`, `//`, `%` |
| 2 | 4–5 | `rating_tier`: `if/elif` и тернарный оператор; `decade_label`: `match` с guards |
| 3 | 6–8 | `print_non_comedies`: `continue`; `find_first_masterpiece`: `while/break/else`; `count_long_movies`: счётчик |
| 4 | 9–11 | `normalize_title`: срезы слов; `make_slug`: `lower/replace`; `format_report_line`: f-строки |
| 5 | 12–13 | `titles_sorted_by_rating`, `top_n_by_rating`: `sorted(key=..., reverse=True)` и кортежи |
| 6 | 14–16 | `count_by_genre`, `actor_filmography`: `dict.get`; `ratings_above_average`: генератор словаря |
| 7 | 17–19 | `all_genres`: `update`; `common_actors`: `&`; `genres_only_in_one`: `-` |
| 8 | 20–21 | `iter_high_rated`: `yield`; `print_high_rated`: демонстрация; `total_duration_above_seven`: `sum` генератора |
| 9 | 22 | `build_report`: общий отчёт, топ-3, число фильмов по жанрам, все жанры |

`normalize_title` сохраняет оставшуюся часть каждого слова, как предписано
выражением `word[0].upper() + word[1:]`. Исходные названия не изменяются:
нормализация применяется при форматировании строк отчёта.

`find_first_masterpiece` ищет рейтинг **строго выше 9.0**, как требует этап 3.
При отсутствии такого фильма печатает `Шедевров не найдено` и возвращает `None`.
Категория `шедевр` в этапе 2 начинается с **9.0** — это отдельное условие задачи.

Жанры в отчёте упорядочены по убыванию количества, а при равенстве — по алфавиту,
чтобы результат не зависел от порядка элементов множеств.

Для пустого каталога средний рейтинг равен `0.0`, статистика возраста — `(0, 0, 0)`.
При `n <= 0` топ пуст. В обычном задании используется исходный каталог из 10 фильмов.

## Проверка

Проверено на Python 3.12.14 и Ruff 0.17.3, закреплённом в `uv.lock`:

- Создано отдельное новое виртуальное окружение и выполнен `uv sync --locked`.
- `uv run catalog_analysis.py` выводит полный отчёт без ошибок.
- `uv run ruff check .` возвращает `All checks passed!`.
- Проверены результаты всех 22 задач, границы категорий/годов, ветка отсутствия
  шедевра, генератор, неизменность каталога и обязательные конструкции языка.

Контрольные результаты: средний рейтинг `7.2`, возраст `(15, 2, 8)`,
4 фильма длиннее 120 минут, 713 минут для рейтингов строго выше 7.

## Примеры отдельных задач

После импорта модуля в Python можно вызвать:

```python
from catalog_analysis import (
    find_first_masterpiece,
    movies,
    print_high_rated,
    print_non_comedies,
    total_duration_above_seven,
)

print_non_comedies(movies)
print(find_first_masterpiece(movies)["title"])
print_high_rated(movies)
print(total_duration_above_seven(movies))  # 713
```

История Git содержит отдельные коммиты по этапам 1–9 и завершающий коммит
форматирования, фиксации зависимостей и документации. `.venv` не включается в Git.
Ссылка для сдачи появится после публикации репозитория в выбранном Git-сервисе.
Работа в Практикум не отправлена.
