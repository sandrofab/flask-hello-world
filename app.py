from flask import Flask, request, render_template
import pandas as pdapp = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! dajeee'


