from flask import Flask, request

app = Flask(__name__)

@app.route('/select_movies', methods=['POST'])
def pick_movies_to_maximise_profit():
    input_dict = request.json
    print(input_dict)
    """
    TODO: To add core logic for the api
    """
    return input_dict


if __name__ == '__main__':
    app.run()
