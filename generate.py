from flask import Flask, render_template, request, Blueprint
import google.generativeai as genai
import requests


generate_blueprint = Blueprint('generate', __name__)
app = Flask(__name__)

genai.configure(api_key="AIzaSyCxI3OaN_BxkcGYPIl62Xo0OW6PhhEj01I")
model = genai.GenerativeModel('gemini-pro')
openai_api_key = 'sk-proj-0BsX4FVEL9G8zn2nTFpmT3BlbkFJh9sKTwHooD0aU1mNq2Vz'
url = 'https://api.openai.com/v1/images/generations'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {openai_api_key}'
}

@generate_blueprint.route('/')
def index():
    return render_template('generate.html')

@generate_blueprint.route('/TomTat', methods=['POST'])
def TomTat():
    input_text = request.form['input_text']
    response = model.generate_content("Vui lòng từ đoạn văn bản trên, hãy tạo các promt cho mô hình sinh ảnh,chỉ giữ lại các thông tin có giá trị,loại bỏ các văn bản liên quan đến cách dùng từ hoa mỹ văn học, cách nhau bởi dấu phẩy hoặc dấy chấm phẩy"+input_text)
    data = response.candidates[0].content.parts[0].text
    return data

@generate_blueprint.route('/CreatePromt', methods=['POST'])
def CreatePromt():
    input_text = request.form['input_text']
  #  response = model.generate_content("Your prompt here" + input_text)
    response = model.generate_content("Sinh ngẫu nhiên promt cần có cho mô hình sinh ảnh, chỉ giữ lại các từ mô tả cảnh vật, cách nhau bởi dấu phẩy, tôi chỉ cần hiển promt mô hình sinh ảnh, không cần hiển thị gì khác"+input_text)
    data = response.candidates[0].content.parts[0].text
    return data

@generate_blueprint.route('/Copy', methods=['POST'])
def Copy():
    input_text = request.form['output']
    response = model.generate_content("Dịch sang tiếng anh: "+input_text)
    data = response.candidates[0].content.parts[0].text
    return data




if __name__ == '__main__':
    app.run(debug=True)
