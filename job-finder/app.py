import os
import json
from dotenv import load_dotenv
from flask import Flask, Config, render_template, url_for, jsonify

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

try:
    with open("data.json", encoding="utf-8") as file:
        data = json.load(file)
except Exception as e:
    print("error: ", e)
    data = []

@app.route('/', methods=["GET", "POST"])
def home():
    print(f"data: {data}")
    return render_template("home.html.jinja", jobs=data["jobs"])

@app.route('/jobs', methods=["GET"])
def get_jobs():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
