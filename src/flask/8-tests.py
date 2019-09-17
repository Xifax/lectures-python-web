from flask import Flask, jsonify, url_for
import pytest


def create_app(env=None):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return jsonify({'message': 'Hi!'})

    @app.route('/quad/<int:number>')
    def quad(number: int):
        return jsonify({'quad': pow(number, 4)})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()


@pytest.fixture
def app():
    return create_app()

def test_app_works(app, client):
    result = client.get(url_for('index'))
    assert result.status_code == 200

def test_may_quad(client):
    result = client.get(url_for('quad', number=2))
    assert result.status_code == 200
    assert 'quad' in result.json
    assert result.json['quad'] == pow(2, 4)

def test_may_not_quad_negative(client):
    # Yes, <int:argument> is only for positive integers
    result = client.get(url_for('quad', number=-1))
    assert result.status_code == 404
