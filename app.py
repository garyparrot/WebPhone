import numpy as np
import subprocess
from flask import Flask, render_template, send_file, request
from io import BytesIO

app = Flask( __name__, static_url_path='', static_folder='template' , template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/phone/display')
def phone_display():

    # Taking a picture 
    output = subprocess.check_output(['adb', 'exec-out', 'screencap', '-p'])
    image_io = BytesIO(output)
    image_io.seek(0)
    return send_file(image_io, mimetype='image/png')

@app.route('/api/phone/click', methods=['POST'])
def phone_click():
    print(request.json)
    X, Y = request.json.get('X', None), request.json.get('Y', None)
    if isinstance(X, (int, float)) and isinstance(Y, (int, float)):
        subprocess.check_output(['adb', 'shell', 'input', 'tap', str(int(X)), str(int(Y))], close_fds=True)
        return { "status": "OK" }

    return {"status": "incorrect payload"}


if __name__ == "__main__":
    app.run(debug=True)
