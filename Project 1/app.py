from flask import Flask, render_template
from flask import request
from wtforms import form, TextField, TextAreaField, validators, StringField, SubmitField
import csv
app = Flask(__name__)

#@app.route("/", methods=('GET'))
#def review():
#    form=ReviewForm()
 #   form.name.data=""
   # form.item.data=""
  #  form.review.data=""
    #return "Hello World!"

@app.route("/")
def fill():
    if request.method == "POST":
        Name=request.form.get("name")
        Item=request.form.get("item")
        Review=request.form.get("comment")
        rows=[Name,Item,Review]
        fieldnames=['Name','Item','Review']
        with open('reviews.csv','w') as csvfile:
            csvwriter = csv.writer(csvFile)
            csvwriter.writerow(rows)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()