from flask import Flask, request, jsonify, Blueprint
import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template

predict_blueprint = Blueprint('predict', __name__)
app = Flask(__name__)

# Load model
model = tf.keras.models.load_model(r'C:\Users\LiZi\Desktop\LV\CODE\keras-flask-deploy-webapp\models\model_lenet.h5')
categories = ['1', '2', '3', '4', '5']

@predict_blueprint.route('/')
def index():
    return render_template('predict.html')

@predict_blueprint.route('/predict', methods=['POST'])
def predict():
    # Nhận ảnh từ yêu cầu POST
    file = request.files['image']
    
    # Đọc và xử lý ảnh
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    image_width = 64
    image_height = 64
    image = cv2.resize(img, (image_width, image_height))
    image = np.array(image, dtype="float") / 255.0
    image = np.expand_dims(image, axis=0)

    # Dự đoán
    pred = model.predict(image)
    predicted_class = categories[np.argmax(pred)]

    # Trả về kết quả
    return jsonify({'predicted_class': predicted_class})

import os

@predict_blueprint.route('/upload_from_folder')
def upload_from_folder():
    image_folder = r'static/save'
    image_list = []

    try:
        for filename in os.listdir(image_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                image_path = os.path.join(image_folder, filename)
                image_list.append(image_path)
        
        return jsonify({'success': True, 'image_list': image_list})
    except Exception as e:
        print(e)
        return jsonify({'success': False})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
