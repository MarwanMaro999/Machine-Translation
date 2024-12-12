# Model and Tokenizer

You can access the model and tokenizer folder [here](https://drive.google.com/drive/folders/18KjDOYI2WByY3FuZ9zO9Pycz2IL3YueP?usp=sharing).

## How to Load the Model

To load the model and tokenizer, use the following code:

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Specify the directory where the model is stored
model_path = "./model_directory"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

print("Model and tokenizer loaded successfully!")
```
