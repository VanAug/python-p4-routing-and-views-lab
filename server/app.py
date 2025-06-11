#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string>")
def print_string(string):
    print(string)
    return Response(string, mimetype='text/plain')

@app.route("/count/<int:num>")
def count(num):
    lines = [str(i) for i in range(num)]
    return Response("\n".join(lines) + "\n", mimetype='text/plain')

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        else:
            return Response("Invalid operation", mimetype='text/plain')

        return Response(str(result), mimetype='text/plain')
    except ZeroDivisionError:
        return Response("Cannot divide or modulo by zero", mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
