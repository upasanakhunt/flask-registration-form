from flask import Flask

app=Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "<h1>My Name Is Upasana...</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h3>This Is Main Index Page In Flask...</h3>"
#variable rule
@app.route("/success/<score>")
def success(score):
    return "The Person Is Passed In 12th Exammination:..."+score

if __name__=="__main__":
    app.run(debug=True)