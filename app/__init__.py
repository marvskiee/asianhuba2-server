from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '7a56c15eee8dffdc716af8121622ec22'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xnvlteueeducsu:683558c7071251628e79e6fd9b0e7dde0ffafb7ee4451b4efb5a86d9ee18c14f@ec2-34-200-94-86.compute-1.amazonaws.com:5432/d3br893nbbpe88'

db = SQLAlchemy(app)

from app import routes