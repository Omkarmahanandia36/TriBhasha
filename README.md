# TriBhasa

Tribhasa is a from-scratch multilingual translation system designed to work seamlessly with PDF documents. The core idea is simple: **select text in a PDF and instantly see its translation**, without choosing languages manually.

This project is built for deep learning fundamentals, not shortcuts. All major components (language detection, tokenization, and translation models) are implemented from scratch.

---

## 🎯 Project Goal

To build an API-driven system that:
- Automatically detects the language of selected text from a PDF
- Translates based on predefined rules
- Returns translations in a clean, structured format
- Can be integrated with a PDF viewer or browser extension

---

## 🌍 Supported Languages (v1)

- **English** (`en`)
- **Hindi** (`hi`)
- **Odia** (`or`)

No additional languages are supported in version 1.

---

## 🔁 Translation Rules (Locked Behavior)

The system follows **automatic routing** based on detected language:

| Detected Language | Translation Output |
|------------------|-------------------|
| Odia | English |
| Hindi | English |
| English | Hindi + Odia |

The user never selects source or target languages manually.

---

## 📥 Input Specification

### Source
- Text selected from a **PDF file**

### Constraints
- Minimum length: 1 word
- Maximum length: 150 characters (v1 limit)

### API Input Format
```json
{
  "text": "<selected_text>"
}
```

---

## 🧠 Language Detection

- Language detection is automatic
- Implemented using **Unicode character ranges**
- No external language detection libraries are used

Detection output (internal):
```
english | hindi | odia
```

---

## 📤 Output Specification

### Case 1: Hindi or Odia Input
```json
{
  "source_language": "hindi",
  "translations": {
    "english": "I am fine"
  }
}
```

### Case 2: English Input
```json
{
  "source_language": "english",
  "translations": {
    "hindi": "मैं ठीक हूँ",
    "odia": "ମୁଁ ଭଲ ଅଛି"
  }
}
```

---

## ⚠️ Error Handling

- Empty text → error response
- Unsupported script → error response
- Mixed-language text → dominant script is chosen

Example error:
```json
{
  "error": "Unsupported language detected"
}
```

---

## 🚫 Non-Goals (v1)

BhashaLens v1 does **not** aim to:
- Translate entire PDFs at once
- Handle scanned/image-only PDFs
- Guarantee perfect grammar or fluency
- Compete with commercial translation tools

---

## 🧱 Planned Architecture (High Level)

```
PDF Text Selection
        ↓
Language Detection
        ↓
Routing Logic
        ↓
From-scratch Translation Models
        ↓
FastAPI Backend
        ↓
Tooltip / Overlay UI


