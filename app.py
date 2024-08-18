from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model('model/model.h5')

def prepare_image(image):
    # Preprocess the image according to your model requirements
    image = image.resize((150, 150))  # Example resizing
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    image = Image.open(io.BytesIO(file.read()))
    processed_image = prepare_image(image)
    
    predictions = model.predict(processed_image)
    class_names = ['normal', 'pneumonia']  # Adjust based on your model's output
    prediction = class_names[np.argmax(predictions)]

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
