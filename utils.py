import sqlite3


def get_movie_by_title(title):  # Поиск фильма по заданному названию
    tt = title
    con = sqlite3.connect('data/netflix.db')
    cur = con.cursor()
    sqlite_query = (f"""
                    SELECT title, country, release_year, listed_in, description
                    FROM netflix
                    WHERE title LIKE '%{tt}%'
                    ORDER BY release_year DESC
                    LIMIT 1""")
    cur.execute(sqlite_query)
    data = cur.fetchall()
    con.close()
    if len(data) == 0:
        return "По вашему запросу ничего не найдено"
    data = data[0]
    data = {"title": data[0],
		"country": data[1],
		"release_year": data[2],
		"genre": data[3],
		"description": data[4]}
    return data

def get_movie_by_year(from_, to):  # Поиск фильма по заданному диапазону лет выпуска
    con = sqlite3.connect('data/netflix.db')
    cur = con.cursor()
    sqlite_query = (f"""
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN {from_} AND {to}
                    ORDER BY release_year ASC
                    LIMIT 100""")
    cur.execute(sqlite_query)
    data = cur.fetchall()
    con.close()
    if len(data) == 0:
        return "По вашему запросу ничего не найдено"
    data_movies = []
    for f in data:
        f = {"title": f[0],
             "release_year": f[1]}
        data_movies.append(f)
    return data_movies

def get_movie_by_rating(rating):  # Поиск фильмов по заданному диапазону рейтинга
    try:
        with sqlite3.connect('data/netflix.db') as con:
            cur = con.cursor()
            sqlite_query = (f"""
                            SELECT title, rating, description
                            FROM netflix
                            WHERE rating = ?
                            LIMIT 10
            					""")
            result = []
            for r in rating:
                cur.execute(sqlite_query, (r,))
                executed_query = cur.fetchall()
                for i in range(len(executed_query)):
                    result.append({
                        "title": executed_query[i][0],
                        "rating": executed_query[i][1],
                        "description": executed_query[i][2]
                    })
            return result
    except:
        raise ValueError("По вашему запросу ничего не найдено")

def get_movie_by_genre(genre): # Поиск фильмов по жанру
    with sqlite3.connect('data/netflix.db') as con:
        cur = con.cursor()
        sqlite_query = (f"""
                        SELECT title, description
                        FROM netflix
                        WHERE listed_in LIKE '%{genre}%'
                        ORDER BY release_year DESC
                        LIMIT 10
    					""")
        result = []
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
        for i in range(len(executed_query)):
            result.append({
			    "title": executed_query[i][0],
			    "description": executed_query[i][1],
		    })
        if len(result) == 0:
            return "По вашему запросу ничего не найдено"
        return result

def get_actors_by_other_actors(actor1, actor2):  # Поиск актеров игравших вместе с заданными актерами
    with sqlite3.connect('data/netflix.db') as con:
        cur = con.cursor()
        sqlite_query = (f"""
                        SELECT [cast]
                        FROM netflix
                        WHERE [cast] LIKE '%{actor1}%'
                        AND [cast] LIKE '%{actor2}%'
        				""")
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
        mentioned_actors = {}
        for i in executed_query:
            data = (str(i[0])).split(", ")
            for d in data:
                if d not in mentioned_actors.keys():
                    mentioned_actors[d] = 0
                else:
                    mentioned_actors[d] += 1
        result = []
        for k, v in mentioned_actors.items():
            if k != actor1 and k != actor2 and v > 1:
                result.append(k)
        return result

def get_movie_by_param(type_of_f, year_of_f, genre_of_f):
    with sqlite3.connect('data/netflix.db') as con:
        cur = con.cursor()
        sqlite_query = (f"""
                        SELECT title, description
                        FROM netflix
                        WHERE type = '{type_of_f}'
                        AND release_year = '{year_of_f}'
                        AND listed_in = '{genre_of_f}'
        				""")
        cur.execute(sqlite_query)
        executed_query = cur.fetchall()
        result = []
        for i in range(len(executed_query)):
            result.append({
                "title": executed_query[i][0],
                "description": executed_query[i][1]
            })
        if len(result) == 0:
            return "По вашему запросу ничего не найдено"
        return result


q = get_movie_by_param('Movie', 1986, 'Dramas')
print(q)
