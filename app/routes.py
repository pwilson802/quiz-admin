from app import app
from flask import Flask, render_template, request


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('index.html')