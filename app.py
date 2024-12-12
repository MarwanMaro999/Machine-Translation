from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load model and tokenizer
model_path = "model"  # Path to the model directory
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Get input text from request
        data = request.get_json()
        input_text = data.get("text", "")

        if not input_text.strip():
            return jsonify({"error": "Input text is empty"}), 400

        # Convert the input text to lowercase
        input_text = input_text.lower()

        # Tokenize and translate
        inputs = tokenizer.encode(input_text, return_tensors="pt")
        outputs = model.generate(inputs)
        translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return jsonify({"translation": translation})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
