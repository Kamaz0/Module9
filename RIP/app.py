from flask import Flask, jsonify, abort
from models import kinofil
from forms import FilmForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/filmoteka/", methods=["GET"])
def cala_filmoteka():
    return jsonify(kinofil.all())

@app.route("/filmoteka/<int:film_id>", methods=["GET"])
def get_film(film_id):
    film = kinofil.get(film_id)
    if not film:
        abort(404)
    return jsonify({"film": film})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


@app.route("/filmoteka/", methods=["POST"])
def create_film():
    if not request.json or not 'title' in request.json:
        abort(400)
    film = {
        'id': todos.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'year': request.json['year'],
        'director':request.json['director'],
        'description': request.json.get('description', ""),
    }
    todos.create(todo)
    return jsonify({'todo': todo}), 201

@app.route("/filmoteka/<int:film_id>", methods=['DELETE'])
def delete_film(film_id):
    result = kinofil.delete(film_id)
    if not result:
        abort(404)
    return jsonify({'result': result})


if __name__ == "__main__":
    app.run(debug=True)