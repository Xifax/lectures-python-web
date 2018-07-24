from flask import Flask, render_template

app = Flask(__name__)

FISH = ['гуппи', 'lionfish', 'featherfin squeaker', 'неон']

@app.route('/')
def home():
    return render_template('fish.html', fish=FISH)

if __name__ == '__main__':
    app.run()
