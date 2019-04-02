"""
The flask application package.
Name:Rohan Aanand
Date:2018-11-10
"""

import os
from flask import Flask


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.basename('Uploads')

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.debug = True

import FinalProject.views
