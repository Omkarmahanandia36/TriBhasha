import csv
import re
from pathlib import Path


RAW_DIR = Path("Dataset/Raw")
OUT_DIR = Path("Dataset/Processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

MAX_LEN = 100
MAX_ROWS = 100000  # <-- IMPORTANT: limit big CSV for now


# -------- CLEANING --------
def clean_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    text = text.replace("\u200c", "")
    text = text.replace("\u200b", "")
    return text


def is_valid(src: str, tgt: str) -> bool:
    if not src or not tgt:
        return False
    if len(src) > MAX_LEN or len(tgt) > MAX_LEN:
        return False
    return True


# -------- EN → OR (TXT) --------
def process_en_or_txt():
    input_file = RAW_DIR / "english_odia.txt"
    output_file = OUT_DIR / "en_or.txt"

    kept, dropped = 0, 0

    with open(input_file, encoding="utf-8") as fin, \
         open(output_file, "w", encoding="utf-8") as fout:

        for line in fin:
            if "||" not in line:
                dropped += 1
                continue

            src, tgt = line.split("||", 1)
            src = clean_text(src)
            tgt = clean_text(tgt)

            if is_valid(src, tgt):
                fout.write(f"{src} ||| {tgt}\n")
                kept += 1
            else:
                dropped += 1

    print(f"[EN→OR TXT] kept={kept}, dropped={dropped}")


# -------- HI → EN (CSV) --------
def process_hi_en_csv():
    input_file = RAW_DIR / "hindi_english_parallel.csv"
    output_file = OUT_DIR / "hi_en.txt"

    kept, dropped = 0, 0

    with open(input_file, encoding="utf-8") as fin, \
         open(output_file, "w", encoding="utf-8") as fout:

        reader = csv.reader(fin)
        next(reader, None)  # skip header

        for idx, row in enumerate(reader):
            if idx >= MAX_ROWS:
                print(f"Stopped after {MAX_ROWS} rows")
                break

            if idx % 5000 == 0 and idx > 0:
                print(f"Processed {idx} rows...")

            if len(row) < 2:
                dropped += 1
                continue

            hindi = clean_text(row[0])
            english = clean_text(row[1])

            if is_valid(hindi, english):
                fout.write(f"{hindi} ||| {english}\n")
                kept += 1
            else:
                dropped += 1

    print(f"[HI→EN CSV] kept={kept}, dropped={dropped}")


# -------- MAIN --------
if __name__ == "__main__":
    process_en_or_txt()
    process_hi_en_csv()
