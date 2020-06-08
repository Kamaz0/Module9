from flask import Flask, jsonify, abort
from models import kinofil

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/filmoteka/", methods=["GET"])
def cala_filmoteka():
    return jsonify(filmy.all())

@app.route("/filmoteka/<int:film_id>", methods=["GET"])
def get_film(film_id):
    film = filmy.get(film_id)
    if not film:
        abort(404)
    return jsonify({"film": film})


if __name__ == "__main__":
    app.run(debug=True)