import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

#basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH= 'uploads/',
	DROPZONE_ALLOWED_FILE_CUSTOM  = True,
	DROPZONE_ALLOWED_FILE_TYPE='image/*, .json',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=30,
)

dropzone = Dropzone(app)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)