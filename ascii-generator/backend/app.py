from flask import Flask, request, jsonify
from flask_cors import CORS
# Import the necessary functions from the ASCII logic files
from ascii_generators import ascii_generators, img2ascii_1, img2ascii_2, txt2ascii_1

app = Flask(__name__)
CORS(app)

@app.route('/convert-text-to-ascii', methods=['POST'])
def convert_text_to_ascii():
    data = request.json
    text = data.get('text')
    # Use the imported functions to convert the text to ASCII
    # For demonstration, I'm using a placeholder function. Replace it with the actual function.
    ascii_result = txt2ascii_1.convert(text)  # Replace with the actual function
    return jsonify({"result": ascii_result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
