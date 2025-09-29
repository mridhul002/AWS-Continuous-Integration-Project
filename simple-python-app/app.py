from flask import Flask, request, render_template_string
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# -----------------------
# Prometheus Metrics
# -----------------------
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Request latency in seconds")

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    latency = time.time() - request.start_time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
    REQUEST_LATENCY.observe(latency)
    return response

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

# -----------------------
# Your Calculator Code
# -----------------------
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Calculator</title></head>
<body>
    <h2>Simple Calculator</h2>
    <form method="post">
        <input type="number" step="any" name="a" required>
        <input type="number" step="any" name="b" required>
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
