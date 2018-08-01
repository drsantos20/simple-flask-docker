from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = False
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class WordCountForm(Form):
    name = TextField('Name:', validators=[validators.required()])
 
def wordcount(find_word):
    return len(find_word.split())

@app.route("/", methods=['GET', 'POST'])
def count():
    form = WordCountForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        name=request.form['name']

        if form.validate():
            flash('We have ' + str(wordcount(name)) + ' words')
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('count.html', form=form)
 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')