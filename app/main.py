from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template
from flask_cors import CORS
from api import routes

app = Flask(__name__)
CORS(app, origins="*")
app.register_blueprint(routes.mod, url_prefix="/api/v1")

@app.route("/")
def landing_page():
    return render_template("index.html")


if __name__ == '__main__':
    Flask.run(app, debug=True, port=8000)
