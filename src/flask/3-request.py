from flask import Flask, redirect, url_for
from flask import request, jsonify
from collections import namedtuple
import json

Fish = namedtuple('Fish', ['name', 'size'])
FishDB = {
    'tetra': Fish(name='тетра', size='small'),
    'плекостомус': Fish(name='парчовый сом', size='big')
}

app = Flask(__name__)

@app.route('/api/fish/<name>')
def fish_api_fetch(name):
    as_json = json.loads(
        request.args.get('as_json', 'false')
    )
    fish = FishDB.get(name)
    if not fish:
        fish = {'error': 'Нет такой рыбы'}

    if as_json:
        fish = jsonify(fish)

    return fish

@app.route('/api/fish', methods=['GET', 'POST'])
def fish_api():
    if request.method == 'GET':
        return jsonify([fish for fish in FishDB.values()])

    elif request.method == 'POST':
        try:
            name = request.form.get('name')
            size = request.form.get('size')
            FishDB[name] = fish = Fish(name=name, size=size)
            return jsonify(fish)

        except KeyError:
            return jsonify(error='Параметры: name, size')

if __name__ == '__main__':
    app.run()
