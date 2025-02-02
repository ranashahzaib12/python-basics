#SHOULD HAVE THIS saving format
#   project_folder/
    # flask+HTML.py        # Your Flask script
    # templates/
    #     about.html      # about.html file should be here
    #     index.html      # (Optional) If you have this file

from flask import Flask,render_template

#WSGI APPLIICATION
app = Flask(__name__, template_folder='templates')

#These routes are like web PAGES
@app.route("/")
def welcome():
    return "<html><H1>Hello  heading 1</h1></html>"

# @app.route("/index")
# def index():
#     return render_template('index.html') 

@app.route("/about")
def index():
    return render_template("about.html") 

if __name__ == "__main__":#Entry  point of code
    app.run(debug=True)