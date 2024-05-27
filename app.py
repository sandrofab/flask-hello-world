from flask import Flask, request, render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! dajeee'


