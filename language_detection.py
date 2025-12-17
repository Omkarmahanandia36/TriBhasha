def detect_language(text: str) -> str:
    
    if not text or text.strip() == "":
        return "unknown"

    counts = {
        "english": 0,
        "hindi": 0,
        "odia": 0
    }

    for ch in text:
        # Odia Unicode block
        if '\u0B00' <= ch <= '\u0B7F':
            counts["odia"] += 1

        # Devanagari (Hindi) Unicode block
        elif '\u0900' <= ch <= '\u097F':
            counts["hindi"] += 1

        # Basic Latin letters (English)
        elif ('a' <= ch.lower() <= 'z'):
            counts["english"] += 1

    detected_language = max(counts, key=lambda x: counts[x])

    if counts[detected_language] == 0:
        return "unknown"

    return detected_language


if __name__ == "__main__":
    samples = [
        "I am fine",
        "मैं ठीक हूँ",
        "ମୁଁ ଭଲ ଅଛି",
        "Hello मैं fine"
    ]

    for text in samples:
        print(f"Text: {text}")
        print("Detected:", detect_language(text))
        print("-" * 30)
