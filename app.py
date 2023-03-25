# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/static/index.html")
def home():

    name = "" # write your name
    age = "" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/static/father.html")
def home():

    fathername = "" # write your name
    fatherage = "" # write your age

    return render_template('father.html' , fathername = name , fatherage = age)

# define the route to mother webpage
@app.route("/static/mother.html")
def home():

    momname = "" # write your name
    momage = "" # write your age

    return render_template('mother.html' , momname = name , momage = age)

# define the route to friends webpage
@app.route("/static/friends.html")
def home():

    friendname = "" # write your name
    friendage = "" # write your age

    return render_template('friend.html' , friendname = name , friendage = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
