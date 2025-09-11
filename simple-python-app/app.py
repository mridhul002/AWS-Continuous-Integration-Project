from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Calculator API! Use /add, /subtract, /multiply, /divide"

@app.route("/add")
def add():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"operation": "add", "a": a, "b": b, "result": a + b})
    except:
        return jsonify({"error": "Please provide numbers a and b"}), 400

@app.route("/subtract")
def subtract():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"operation": "subtract", "a": a, "b": b, "result": a - b})
    except:
        return jsonify({"error": "Please provide numbers a and b"}), 400

@app.route("/multiply")
def multiply():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"operation": "multiply", "a": a, "b": b, "result": a * b})
    except:
        return jsonify({"error": "Please provide numbers a and b"}), 400

@app.route("/divide")
def divide():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        if b == 0:
            return jsonify({"error": "Division by zero not allowed"}), 400
        return jsonify({"operation": "divide", "a": a, "b": b, "result": a / b})
    except:
        return jsonify({"error": "Please provide numbers a and b"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




