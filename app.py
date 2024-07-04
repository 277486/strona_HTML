from flask import Flask, url_for, render_template, request

app = Flask(__name__)

ex_dict = {'zad1': [-1], 'zad2': ['5 - 5i', '5-5i', '-5i + 5', '-5i+5'],
           'zad3': ['-4 - 6i', '-4-6i', '-6i - 4', '-6i-4'],
           'zad4': ['2i'], 'zad5': [4], 'zad6': [13], 'zad7': [6], 'zad8': [4],
           'zad9': ['8 - 8i', '8-8i', '-8i + 8', '-8i+8'],
           'zad10': ['-1/8i', '-1/8 i'], 'zad11': [1]}


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


@app.route("/zadania", methods=["POST", "GET"])
def exercises():
    if request.method == "POST":
        for i in range(1, 12):
            name = f'zad{i}'
            if ex_dict[name] in request.form[name]:
                pass
            if ex_dict[name] not in request.form[name]:
                pass
        return render_template("zadania.html", ex_dict=ex_dict)
    else:
        return render_template("zadania.html")


if __name__ == "__main__":
    app.run(debug=True)
