from bottle import route, run, template
import requests

@route('/')
def index():
    poets = []
    r = requests.get('http://api/')
    if r.ok:
        poets = r.json().get('poets', [])
    return template('poets', poets=poets)

run(host='0.0.0.0', port=8080)
