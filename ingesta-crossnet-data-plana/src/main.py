from flask import Flask, request
from utils import process_data

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    data = request.get_json()
    response = process_data(data)
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)