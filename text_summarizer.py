from transformers import pipeline

def summarize_text(text, max_length=1000, min_length=30, model_name="facebook/bart-large-cnn"):
    """
    Summarize the input text using a pretrained transformer model.

    Args:
        text (str): The text to summarize.
        max_length (int): Maximum length of the summary.
        min_length (int): Minimum length of the summary.
        model_name (str): The pretrained model to use for summarization.

    Returns:
        str: The summarized text.
    """
    summarizer = pipeline("summarization", model=model_name)
    input_length = len(text.split())
    # Adjust max_length if input is shorter than max_length
    if input_length < max_length:
        max_length = input_length
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    sample_text = """
    This Agreement is made and entered into as of the date last written below by and between the parties.
    The parties agree to the following terms and conditions, which shall govern their relationship.
    Any disputes arising under this Agreement shall be resolved through arbitration in accordance with the rules.
    """
    print("Original Legal Text:")
    print(sample_text)
    print("\nSummary:")
    try:
        legal_model = "facebook/bart-large-cnn"  # Replace with a legal-specific model if available
        print(summarize_text(sample_text, model_name=legal_model))
    except Exception as e:
        print(f"Error during summarization: {e}")
