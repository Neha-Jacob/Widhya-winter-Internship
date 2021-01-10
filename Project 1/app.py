from flask import Flask, escape, request, render_template, url_for, redirect
import csv

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets import TextArea
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

class ReviewForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    item = StringField('Item', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Send')

@app.route("/", methods=["GET"])
def review():
    form=ReviewForm()
    form.name.data=""
    form.item.data=""
    form.review.data=""
    with open('reviews.csv') as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        reviewlist=[]
        for row in csvreader:
            reviewlist.append({"Name":row[0],"Item":row[1],"Review":row[2]})
    return render_template('index.html', form=form, reviewlist=reviewlist)

@app.route("/", methods=["POST"])
def fill():
    if request.method == "POST":
        data=dict(request.form)
        Name=data["name"]
        Item=data["item"]
        Review=data["review"]
        fieldnames=['Name','Item','Review']
        with open('reviews.csv',mode='a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow([Name,Item,Review])
    return review()

if __name__ == "__main__":
    app.run(debug=True)

