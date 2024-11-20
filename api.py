from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data with image URLs and text
data = [
  {
    "id": 1,
    "image_url": "https://example.com/image1.jpg",
    "description": "This is the first image description."
  },
  {
    "id": 2,
    "image_url": "https://example.com/image2.jpg",
    "description": "This is the second image description."
  },
  {
    "id": 3,
    "image_url": "https://example.com/image3.jpg",
    "description": "This is the third image description."
  }
]

# API endpoint to return images and text
@app.route('/', methods=['GET'])
def get_images():
  return jsonify(data)

if __name__ == '__main__':
  app.run(debug=True)
