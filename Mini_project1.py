books = [
    {"title": "Думай и богатей", "year": 1937, "rating": 4.69, "genre": "психология", 'author': 'Napoleon Hill'},
    {"title": "Психология влияния", "year": 1984, "rating": 4.8, "genre": "психология", 'author': 'Robert Chaldini'},
    {'title': 'Изучаем Python', 'year': 2016, 'rating': 4.9, 'genre': 'Наука', 'author': 'Mark Lutz'},
    {'title': 'Атомные привычки', 'year': 2014, 'rating': 4.95, 'genre': 'психология', 'author': 'James Cleer'},
    {'title': '7 навыков высокоэффективных людей', 'year': 2018, 'rating': 4.6, 'genre': 'психология', 'author': 'Stiven Kovi'},
    {'title': 'Политика', 'year': 273, 'rating': 3.9, 'genre': 'Наука', 'author': 'Aristotel'}
]

# 1. Фильтр по жанру
def genre_func(books_list, genre):
    filtered_books = list(filter(lambda product: product['genre'] == genre, books_list))
    return filtered_books
genres = ['Наука', 'психология']
for cat in genres:
    filtered = genre_func(books, cat)
    print(f"{cat}: {len(filtered)}")

# 2. Фильтр по году (после 2000)
def year_func(books_list):
    filtered_year = list(filter(lambda product: product['year'] >= 2000, books_list))
    return filtered_year
years = year_func(books)
for m in years:
    print(f"{m['title']}: {m['year']}")

# 3. Сортировка по рейтингу
def rate_func(books_list, reverse=False):
    sorted_ratings = sorted(books_list, key=lambda product: product['rating'], reverse=reverse)
    return sorted_ratings
ratings_tothebest = rate_func(books, reverse=True)
for n in ratings_tothebest:
    print(f"{n['title']}: {n['rating']}")

# 4. Поиск по названию
def title_func(books_list, name):
    namelower = name.lower()
    find_book = list(filter(lambda product: product['title'].lower() == namelower, books_list))
    return find_book
result = title_func(books, 'политика')
for m in result:
    print(f"Найдено по вашему запросу: {m['title']}")


# 5. Поиску по автору
def author_func(books_list, author):
    filtered_author = list(filter(lambda product: product['author'] == author, books_list))
    return filtered_author

james_k = author_func(books, 'James Cleer')
for i in james_k:
    print(f"Книги по вашему запросу: {i['title']}")


