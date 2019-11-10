
from flask import Flask, request, Response, jsonify, render_template, flash, redirect
import time
import os
import img_recog
import sys
from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
key=sys.argv[1]
secret_key=sys.argv[2]
app = Flask(__name__)

def allowed_file(filename):
    """
    Function to check for allowed File Extensions
    """
    try:
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    except:
        return 1

@app.route('/photo')
def photo():
    """
    Render Default Page to input user data, data comprises of user face and ID
    """
    return render_template('frontend.html')

@app.route('/upload', methods=['POST'])

def upload_file():
    """
    Function to extract information from Image 
    """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return "Failed to upload, Please try again"
        
        content = request.files['file'].read()
        
        # Returns a dictionary of face and text fields
        s= img_recog.aws_img_recognize(key,secret_key,content)
        return str(s)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
