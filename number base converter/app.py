from flask import Flask, render_template, request

app = Flask(__name__)

def convert_base(num_str, from_base, to_base):
    try:
        decimal = int(num_str, from_base)
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if decimal == 0:
            return "0"
        result = ""
        while decimal > 0:
            result = digits[decimal % to_base] + result
            decimal //= to_base
        return result
    except ValueError:
        return "Invalid input for base {}".format(from_base)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        from_base = int(request.form["from_base"])
        to_base = int(request.form["to_base"])
        number = request.form["number"].strip().upper()
        result = convert_base(number, from_base, to_base)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)