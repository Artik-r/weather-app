from flask import flask

app = Flask(_name_)

@app.route("/")
def home():

    return "Hello Welcome to Flask !"

if name == "_main_":

    app.run(debug=True)

