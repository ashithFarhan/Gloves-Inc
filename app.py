from flask import render_template, Flask, request, redirect, url_for, make_response, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '.\\static\\uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/customize/<model>")
def profile(model):
    return render_template('model1.html')

@app.route("/saveGLB", methods = ['POST'])
def saveGLB():
    print(request.files)
    file = request.files['data']
    filename = secure_filename(file.filename)
    basedir = os.path.abspath(os.path.dirname(__file__))
    file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], 'newGlove.glb'))
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'newGlove.glb'))

    return 'OK'



if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)