from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

@app.route('/')
def student():
    form = ReusableForm(request.form)
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        print("posting")
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')

    #return render_template('student.html')
    return render_template('student.html', form=form)

def wordcount(find_word):
    return len(find_word.split())

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      email = request.form.get('Word')
      print(wordcount(email))
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)