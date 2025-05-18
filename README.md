# Text Summarizer

This is a simple text summarization project in Python using the Hugging Face Transformers library.

## Requirements

- Python 3.6+
- Install dependencies with:
  ```
  pip install -r requirements.txt
  ```

## Usage

Run the `text_summarizer.py` script to see a sample text summarized:

```
python text_summarizer.py
```

You can modify the `sample_text` variable in the script to summarize your own text.

To use a legal domain-specific model for summarization, update the `model_name` parameter in the `summarize_text` function call within the script. For example, replace the model name with a legal-specific pretrained model from Hugging Face if available.

## Notes

- This project uses the `facebook/bart-large-cnn` pretrained model for general summarization by default.
- Legal document summarization can be performed by specifying a legal domain-specific model.
- Make sure you have a working internet connection the first time you run the script to download the model.
