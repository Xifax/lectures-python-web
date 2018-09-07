from uuid import uuid4
from collections import namedtuple

from flask import (Flask, request, abort,
    render_template, send_from_directory)
from flask_restful import Resource, Api, reqparse


def get_id():
    return str(uuid4())[:8]


entry = namedtuple("Opinion", ["id", "group", "text"])
OPINIONS = [
    entry(id=get_id(), group="pro",
        text="Виджеты классные"),
    entry(id=get_id(), group="pro",
        text="Обновляются асинхронно"),
    entry(id=get_id(), group="contra",
        text="Хитрое взаимодействие с сервером"),
]

app = Flask(__name__)
api = Api(app,
    errors={ "StopIteration":
        { "message": "Не нашлось", "status": 404 }})

parser = reqparse.RequestParser()
parser.add_argument("group", type=str, required=True,
    help="Мнение: pro et contra")
parser.add_argument("text", type=str, required=True,
    help="Надо указать сам текст")


@app.route("/")
def widget():
    return render_template("widget.html")


class OpinionList(Resource):
    def get(self):
        return OPINIONS

    def post(self):
        args = parser.parse_args()
        if args["group"] not in ["pro", "contra"]:
            return abort(400)
        opinion = entry(
            id=get_id(),
            group=args["group"],
            text=args["text"])
        OPINIONS.append(opinion)
        return opinion, 201


class Opinion(Resource):
    def get(self, id):
        return next(filter(
            lambda e: e.id == id, OPINIONS)), 200

    def delete(self, id):
        OPINIONS[:] = [e for e in OPINIONS if e.id != id]
        return "", 204


api.add_resource(OpinionList, "/opinions")
api.add_resource(Opinion, "/opinions/<string:id>")


@app.route('/static/<path:path>')
def js(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()
