from os import getenv
from flask import Flask

app = Flask(__name__)

@app.route('/')
def boo():
    return 'Boo! {}'.format(getenv('HOSTNAME'))
