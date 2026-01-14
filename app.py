from flask import Flask, render_template, jsonify

app = Flask(__name__)

cliques = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/click", methods=["POST"])
def click():
    global cliques
    cliques += 1
    return jsonify({"cliques": cliques})

if __name__ == "__main__":
    app.run(debug=True)
