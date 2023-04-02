from flask import Flask, request
app = Flask(__name__)

@app.route('/add')
def add():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 and num2:
        result = str(float(num1) + float(num2))
        return result
    else:
        return "Error: provide both numbers as query parameters"

@app.route('/subtract')
def subtract():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 and num2:
        result = str(float(num1) - float(num2))
        return result
    else:
        return "Error: provide both numbers as query parameters"

@app.route('/multiply')
def multiply():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 and num2:
        result = str(float(num1) * float(num2))
        return result
    else:
        return "Error: provide both numbers as query parameters"

@app.route('/divide')
def divide():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 and num2:
        if float(num2) == 0:
            return "Error: division by zero"
        result = str(float(num1) / float(num2))
        return result
    else:
        return "Error: provide both numbers as query parameters"

if __name__ == '__main__':
    app.run(debug=True)
