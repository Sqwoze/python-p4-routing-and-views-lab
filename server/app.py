#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

# Index view
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Print string view
@app.route('/print/<string_param>')
def print_string(string_param):
    print(string_param)  # Prints to the console
    return f'<h1>{string_param}</h1>'  # Displays in the browser

# Count view
@app.route('/count/<int:count_to>')
def count(count_to):
    numbers = ""
    for i in range(1, count_to + 1):
        numbers += f'<p>{i}</p>'  # Create a new <p> tag for each number
    return numbers

# Math view
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return '<h1>Error: Cannot divide by zero!</h1>'
        result = num1 / num2
    elif operation == 'mod':
        result = num1 % num2
    else:
        return '<h1>Invalid operation!</h1>'
    
    return f'<h1>{num1} {operation} {num2} = {result}</h1>'

# Run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
