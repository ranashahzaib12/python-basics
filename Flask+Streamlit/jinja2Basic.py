#Jinja2Template 
"""
# {{}} expression to print output in html
{%....%} conditions , for loops
{#...#} For comments

 """ #


from flask import Flask,render_template,request

#WSGI APPLIICATION
app = Flask(__name__, template_folder='templates')

#These routes are like web PAGES
@app.route("/")
def welcome():
    return "<html><H1>Hello Rana Welcome to Home Page!</h1></html>"

@app.route("/index",methods = ['GET']) # 
def index():
    return render_template('index.html') 

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f'{name} just submitted the form'
    return render_template("submit.html") 

#Variable Rule
# @app.route('/succes/<int:score>')#Specifying the score as integer
# def succes(score):
#     #Type this in url to see the output "//127.0.0.1:5000/succes/77"
#     return  "The marks is "+ str(score) #We also need to do this>>OTHERWISE THERE WILL BE ATYPE ERROR

# #Dynamically creating the url Simplr with {{}}
# @app.route('/succes/<int:score>')#Specifying the score as integer
# def succes(score):
#     res =""
#     if score>=50:
#         res ="PASsED"
#     else:
#         res="FaILeD"

#     return render_template("result.html",results=res)

#Dynamically creating the url Simplr with {% %}}
# @app.route('/succesres/<int:score>')#Specifying the score as integer
# def succesfor(score):
#     res =""
#     if score>=50:
#         res ="PASsED"
#     else:
#         res="FaILeD"
#         #It's html has for Loop implimented
#     exp={'score': score , "res":res}
#     return render_template("result1.html",results=exp)


#Dynamically creating the url Simplr with {% %} if condition
@app.route('/succesif/<int:score>')#Specifying the score as integer
def succesif(score):

    return render_template("result2.html",results=score )


#Dynamically creating the url Simplr with 
@app.route('/fail/<int:score>')#Specifying the score as integer
def fail(score):
    return render_template("result.html",results=score)



# def get_results():
#         return render_template("result.html",results=score)
 

if __name__ == "__main__":#Entry  point of code
    app.run(debug=True)

