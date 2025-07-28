from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Simple Calculator</h2>
    <form action="/calculate" method="get">
        <input name="x" type="number" step="any" required>
        <select name="op">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input name="y" type="number" step="any" required>
        <button type="submit">Calculate</button>
    </form>
    """

@app.route("/calculate")
def calculate():
    try:
        x = float(request.args.get("x", 0))
        y = float(request.args.get("y", 0))
        op = request.args.get("op")
        if op == "add":
            result = x + y
        elif op == "subtract":
            result = x - y
        elif op == "multiply":
            result = x * y
        elif op == "divide":
            if y == 0:
                return "Error: Cannot divide by zero."
            result = x / y
        else:
            return "Invalid operation."
        return f"Result: {result} <br><a href='/'>Back</a>"
    except Exception as e:
        return f"Error: {e} <br><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
