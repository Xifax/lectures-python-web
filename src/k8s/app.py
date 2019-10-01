from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Poet(Resource):
    def get(self):
        return { 'poets': [
            'John Keats',
            'Emily Dickinson',
            'William Wordsworth',
            'Vladimir Nabokov',
        ]}
api.add_resource(Poet, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
