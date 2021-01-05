from flask import Flask
from wtforms import form, Textfield, TextAreaField, validators, StringField, SubmitField
app = Flask(__name__)

@app.route("/", methods=('GET','POST'))
def index():
    form=ReviewForm()
    if form.validate_on_submit():
        return f'''<h1> Welcome {form.name.data} </h1>'''
    return "Hello World!"

class ReviewForm(Form):
    name= Textfield(label=('Enter your name *: '), validators=[validators.DataRequired()])
    item= Textfield(label=('Enter the item being reviewed *: '), validators=[validators.DataRequired()])
    comment= TextAreaField(label=('Enter review *: '), validators=[validators.DataRequired()])
    submit= SubmitField(label=('Submit'))

if __name__ == "__main__":
    app.run()