from flask import Flask, request, render_template
import os

app = Flask(__name__, static_url_path='/static')

# Define the folder where uploaded APK files will be stored
UPLOAD_FOLDER = 'uploads/bin'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_apk():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        # Make sure the folder exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        # Save the uploaded APK file to the UPLOAD_FOLDER
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return "File uploaded successfully."


@app.route('/expanding_button')
def expanding():
    return render_template('Expanding_button.html')


if __name__ == '__main__':
    app.run(debug=True)
