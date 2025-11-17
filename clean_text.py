def clean_text(text):
    return "".join(ch for ch in text.upper() if ch.isalpha())

#delete non alphabet symbols from text