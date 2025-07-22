from flask import Flask, render_template, jsonify
import random
import json
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# Load fun facts
with open(os.path.join("app", "facts.json")) as f:
    FUN_FACTS = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fact")
def fact():
    return jsonify({"fun_fact": random.choice(FUN_FACTS)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
