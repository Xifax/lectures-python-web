from flask import render_template, Flask, jsonify, request, abort
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, validators

app = Flask(__name__)
app.secret_key = 'qwerty'
csrf = CSRFProtect(app)

class SepulkariiForm(FlaskForm):
    sepulki = StringField('sepulki',  [validators.Length(min=2, max=50)])

@app.route('/')
def index():
    form = SepulkariiForm()
    return render_template('form.html', form=form)

@app.route('/sepulenie/', methods=['post'])
def sepulenie():
    form = SepulkariiForm()
    if form.validate_on_submit():
        return jsonify(
            message=f'Sepulated {form.sepulki.data}')
        return jsonify(data=form.errors)
    return abort(400)

if __name__ == '__main__':
    app.run()
