"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi862m4dadc9vm53oqg-a.oregon-postgres.render.com",
        database="todo_si3w",
        user="root",
        password="7WP5pdZFUhi8u4XcJUhvfyWJec099XYN")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
