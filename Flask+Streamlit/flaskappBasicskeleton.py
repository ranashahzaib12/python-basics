
from flask import Flask
"""
It creates an instance of the flask 
which will be our WSGI application
"""
#WSGI APPLIICATION
app = Flask(__name__)

#These routes are like web PAGES
@app.route("/")
def welcome():
    return "Welcom to new FUNCTION,updated with debugger"

@app.route("/index")# just type /index in the url in browser see the routes magic
def new():
    return "This is Hello! from index."


if __name__ == "__main__":#Entry point of code
    app.run(debug=True)#No need to run again and again the code 
    # it will auto make changes in the output/web whenever we refresh the page