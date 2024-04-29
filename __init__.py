from flask import Flask, render_template, redirect, url_for
from generate import generate_blueprint
from predict import predict_blueprint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/generate')
def goto_generate():
    return render_template('generation.html')

@app.route('/predict')
def goto_predict():
    return render_template('predict.html')

@app.route('/img2img')
def goto_img2img():
    return render_template('sd.html')

app.register_blueprint(generate_blueprint)
app.register_blueprint(predict_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
