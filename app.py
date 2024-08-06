from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample translation dictionary for French
TRANSLATION_DICT = {
    "hello": "bonjour",
    "goodbye": "au revoir",
    "please": "s'il vous plait",
    "thank you": "merci",
    "yes": "oui",
    "no": "non"
}

@app.route('/translate', methods=['POST'])
def translate_text():
    # Retrieve JSON data from request
    data = request.json

    # Validate input
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input. No text provided!'}), 400

    # Extract text
    text = data['text'].lower()  # Convert to lowercase for consistent dictionary lookup

    # Translate text using the dictionary
    translated_text = TRANSLATION_DICT.get(text, "Translation not found")

    # Return a simple response
    return jsonify({
        'status': 'success',
        'original_text': text,
        'translated_text': translated_text
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
