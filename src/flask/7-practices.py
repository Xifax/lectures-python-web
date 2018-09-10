# factory app initialization
from flask import Flask, render_template, session, redirect

def create_app():
    app = Flask(__name__)
    # api & blueprints & database & so on
    return app

app = create_app()

# flask configuration
def get_config_variables():
    from flask import current_app

    current_app.config['ALL_YOUR_BASE']
    print(current_app.root_path)
    # ../src/flask


# context injection
@app.context_processor
def chupacabra_injector():
    return {
        'chupacabra': 'chilling in Puerto Rico'
    }

@app.route('/')
def somewhere():
    return render_template('san-juan.html')


# custom decorators
from functools import wraps
def increment_views(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'views' not in session:
            session['views'] = 1
        else:
            session['views'] += 1
        if session['views'] > 10:
            session['views'] = 0
            return redirect('/')
        return func(*args, **kwargs)

    return decorated_function

@app.route('/search')
@increment_views
def search_for_chupacabra():
    return render_template('san-juan.html',
        views=session.get('views'))



# run this example
if __name__ == "__main__":
    app.secret_key = 'me-is-very-quite-so-secret'
    app.run()
