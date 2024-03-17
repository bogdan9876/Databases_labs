import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_routes(app)
    create_database()
    create_tables(app)
    populate_data()
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


def populate_data():
    if os.path.exists('data.sql'):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='bogda765',
            database='booking'
        )
        cursor = connection.cursor()
        with open('data.sql', 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        connection.rollback()
        cursor.close()
        connection.close()
