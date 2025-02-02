
from flask import Flask,render_template,request

#WSGI APPLIICATION
app = Flask(__name__, template_folder='templates')

#These routes are like web PAGES
@app.route("/")
def welcome():
    return "<html><H1>Hello Rana Welcome to Home Page!</h1></html>"

@app.route("/index",methods = ['GET']) #  "/index"  type this in the url in the Browser it opens up a new page
def index():
    return render_template('index.html') 

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f'{name} just submitted the form'
    return render_template("form.html") 

if __name__ == "__main__":#Entry  point of code
    app.run(debug=True)


