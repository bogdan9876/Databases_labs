import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_routes(app)
    create_database()
    create_tables(app)
    return app


def create_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='bogda765',
        database='mysql'
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS booking")
    cursor.close()
    connection.close()


def create_tables(app):
    with app.app_context():
        db.create_all()
