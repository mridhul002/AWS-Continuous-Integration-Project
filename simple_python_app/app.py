from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f4;
        }
        form {
            margin-top: 20px;
        }
        input, select, button {
            margin: 5px;
            padding: 10px;
            font-size: 16px;
        }
        h3 {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h2>Simple Calculator</h2>
    <form method="post">
        <input type="number" step="any" name="a" placeholder="Enter first number" required>
        <input type="number" step="any" name="b" placeholder="Enter second number" required>
        <select name="operation">
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select>
        <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% elif error %}
        <h3 style="color:red;">Error: {{ error }}</h3>
    {% endif %}
</body>
</html>
"""

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def calculator():
        result = None
        error = None
        if request.method == "POST":
            try:
                a = float(request.form["a"])
                b = float(request.form["b"])
                op = request.form["operation"]
                if op == "add":
                    result = a + b
                elif op == "subtract":
                    result = a - b
                elif op == "multiply":
                    result = a * b
                elif op == "divide":
                    if b == 0:
                        error = "Division by zero not allowed"
                    else:
                        result = a / b
                else:
                    error = "Invalid operation"
            except Exception as e:
                error = "Invalid input: " + str(e)
        return render_template_string(HTML_TEMPLATE, result=result, error=error)

    return app

# Optional: for local dev
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)





