from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/select_movies', methods=['POST'])
def pick_movies_to_maximise_profit():
    selected_movies = []
    result = {}
    movie_amount = 10000000
    input_dict = request.json
    movies = input_dict['movies']
    movies.sort(key=lambda movie: datetime.strptime(movie['end_date'], '%d %b %Y'))
    if len(movies) != 0:
        selected_movies.append(movies[0])
        prev_end = movies[0]['end_date']
        for i in range(1, len(movies)):
            curr_start = movies[i]['start_date']
            curr_end = movies[i]['end_date']
            # checking overlapping movies
            if datetime.strptime(curr_start, '%d %b %Y') > datetime.strptime(prev_end, '%d %b %Y'):
                selected_movies.append(movies[i])
                prev_end = curr_end

    result['total_amount'] = len(selected_movies) * movie_amount
    result['selected_movies'] = selected_movies
    return result


if __name__ == '__main__':
    app.run()
