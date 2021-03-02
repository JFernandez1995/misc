from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"about":"Hello world!"})

@app.route('/test')
def hello_test():
    return jsonify({"test":"test!"})

@app.route('/v1/test')
def hello_v1test():
    return jsonify({"test v1":"test v1!"})


@app.route('/v1/mult/<int:num1>/<int:num2>', methods=['GET','POST'])
def multiply(num1,num2):
    val = num1 * num2
    return jsonify({"multiplied_value":val})