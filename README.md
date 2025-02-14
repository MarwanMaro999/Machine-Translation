# 📖 Machine Translation (English to Arabic)

This project demonstrates how to use **Hugging Face** libraries to apply the **Helsinki-NLP `opus-mt-en-ar`** model for English-to-Arabic translation. It includes:
- Loading the **CoVoST2 EN-AR dataset**
- Setting up the **model and tokenizer**
- **Translating text** using a pre-trained model
- **Evaluating results** with BLEU scores

---

## Features

### Model and Tokenizer Setup
- **Load Pre-trained Model**: Load the Helsinki-NLP `opus-mt-en-ar` model.
- **Initialize Tokenizer**: Set up the tokenizer for text processing.

### Text Translation
- **Tokenize Input Text**: Prepare the input text for translation.
- **Generate Translations**: Use the model to translate the text.
- **Decode Output**: Convert the model's output to readable text.

### Evaluation
- **Compute BLEU Scores**: Compare model translations with reference translations to measure quality.

### Demonstration
- **Example Translations**: Showcase the model's capabilities with example sentences.
- **Advantages**: Highlight the benefits of using a pre-trained model.

---

## Getting Started

### Prerequisites
- Python 3.x
- Hugging Face Transformers library
- Datasets library

### Installation
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/ManwanMaro999/Machine-Translation.git
    cd Machine-Translation
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
