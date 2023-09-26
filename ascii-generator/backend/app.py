from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image  # Import Pillow for image handling

# Import the necessary functions from the ASCII logic files
from ascii_generators import txt2ascii_1, img2ascii_1, img2ascii_2


app = Flask(__name__)
CORS(app)

@app.route('/convert-text-to-ascii', methods=['POST'])
def convert_text_to_ascii():
    data = request.json
    text = data.get('text')
    
    # Use the imported function to convert text to ASCII
    # Replace with the actual function from your ascii_generators module
    ascii_result = txt2ascii_1.text_to_ascii_generator(text)  # Replace with actual function
    return jsonify({"result": ascii_result})

@app.route('/convert-image-to-ascii', methods=['POST'])
def convert_image_to_ascii():
    # Get the image data from the request
    image_data = request.files['image']

    # Check if an image file was provided
    if image_data and allowed_file(image_data.filename):
        # Open the image using Pillow
        img = Image.open(image_data)

        # Perform image-to-ASCII conversion using your chosen method
        # Replace with the actual function from your ascii_generators module
        ascii_result = img2ascii_1.image_to_ascii(img)  # Replace with actual function

        return jsonify({"result": ascii_result})
    else:
        return jsonify({"error": "Invalid or missing image file"})

# Add a function to check if the file extension is allowed
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
