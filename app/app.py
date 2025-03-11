from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Connected to PostgreSQL!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)