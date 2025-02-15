import logging

from flask import Flask, flash, jsonify, render_template, request

app = Flask(__name__)
app.secret_key = "supersecretkey"

logging.basicConfig(level=logging.ERROR)


ex_dict = {
    "zad1": ["-1"],
    "zad2": ["5-5i", "-5i+5"],
    "zad3": ["-4-6i", "-6i-4"],
    "zad4": ["2i"],
    "zad5": ["4"],
    "zad6": ["13"],
    "zad7": ["6"],
    "zad8": ["4"],
    "zad9": ["8-8i", "-8i+8"],
    "zad10": ["-1/8i", "-0.125i"],
    "zad11": ["1"],
}


@app.route("/")
def home():
    return render_template("strona_glowna.html")


@app.route("/bibliografia")
def bibliography():
    return render_template("bibliografia.html")


@app.route("/liczby_zespolone")
def imaginary_numbers():
    return render_template("liczby_zespolone.html")


@app.route("/o_autorach")
def about_authors():
    return render_template("o_autorach.html")


@app.route("/send_complex", methods=["POST"])
def send_complex():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        real_part = float(data["realPart"])
        imaginary_part = float(data["imaginaryPart"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid data"}), 400

    response = {
        "realPart": real_part,
        "imaginaryPart": imaginary_part,
    }
    return jsonify(response)


@app.route("/zadania", methods=["POST", "GET"])
def exercises():
    user_answer = {}
    if request.method == "POST":
        task_number = request.form.get("task_number")
        name = f"zad{task_number}"
        data = request.form.get(name)
        user_answer[name] = data.replace(" ", "")

        if user_answer[name]:
            correct_answer = ex_dict[name]
            if user_answer[name] in correct_answer:
                flash(f"{name}:Dobra odpowiedź!", "success")
            else:
                flash(f"{name}:Zła odpowiedź!", "error")
    return render_template("zadania.html", ex_dict=ex_dict, user_answer=user_answer)


@app.errorhandler(404)
def page_not_found(e):
    logging.error(f"Błąd 404: Strona nie została znaleziona: {request.url}")
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
