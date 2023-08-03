from flask import Flask,render_template
from sqlalchemy import func
from app.models import db
from flask_sqlalchemy import SQLAlchemy
from app.routes import app as routes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Praveen%40mysql2223@localhost:3306/inventory'  # Connecting db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications for SQLAlchemy

# Create the SQLAlchemy database instance
db.init_app(app)

# Register the Blueprint with the app
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)