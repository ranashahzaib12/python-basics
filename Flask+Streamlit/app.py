from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('new.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieving form data
    name = request.form['name']
    subject1 = int(request.form['subject1'])
    subject2 = int(request.form['subject2'])
    subject3 = int(request.form['subject3'])

    # Calculate total and average
    total = subject1 + subject2 + subject3
    average = total / 3

    # Determine result status
    result = "Pass" if average >= 50 else "Fail"

    # Displaying results dynamically
    return f"""
    <h1>Results for {name}</h1>
    <p>Total Marks: {total}</p>
    <p>Average Marks: {average:.2f}</p>
    <p>Result: {result}</p>
    <a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
