"""ДЗ №1: анализ каталога средствами Python, этапы 1–9."""

import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021,
     "genres": {"sci-fi", "drama"}, "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019,
     "genres": {"comedy", "drama"}, "rating": 7.1, "duration_min": 98,
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "Silent hours", "year": 2016,
     "genres": {"thriller", "drama"}, "rating": 6.4, "duration_min": 112,
     "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023,
     "genres": {"sci-fi", "action"}, "rating": 5.9, "duration_min": 101,
     "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014,
     "genres": {"comedy"}, "rating": 7.8, "duration_min": 89,
     "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020,
     "genres": {"thriller", "mystery"}, "rating": 8.9, "duration_min": 124,
     "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022,
     "genres": {"drama"}, "rating": 4.8, "duration_min": 137,
     "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024,
     "genres": {"sci-fi", "drama"}, "rating": 9.2, "duration_min": 118,
     "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011,
     "genres": {"comedy"}, "rating": 6.0, "duration_min": 95,
     "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018,
     "genres": {"action", "thriller"}, "rating": 7.3, "duration_min": 129,
     "actors": ["P. Diaz", "T. Chalamet"]},
]


# Этап 1. Числа и math (задачи 1–3).
def average_rating(movies):
    """Средний рейтинг, округлённый до одного десятичного знака."""
    if not movies:
        return 0.0
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возраст самого старого, нового фильма и средний возраст вверх."""
    if not movies:
        return (0, 0, 0)
    ages = [current_year - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    """Представление минут в виде '2ч 35м'."""
    return f"{minutes // 60}ч {minutes % 60}м"


# Этап 2. Условия и match (задачи 4–5).
def rating_tier(rating):
    """Категория рейтинга с тернарным оператором."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Группа года выпуска, определённая через match с охранными условиями."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# Этап 3. Циклы (задачи 6–8).
def print_non_comedies(movies):
    """Напечатать названия фильмов, исключив комедии через continue."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    """Найти первый рейтинг строго выше 9.0; сообщить, если его нет."""
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            break
        index += 1
    else:
        print("Шедевров не найдено")
        return None
    return movies[index]


def count_long_movies(movies, threshold=120):
    """Количество фильмов строго длиннее порога, накоплением в цикле."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count
