from tokenizer.char_tokenizer import CharTokenizer
from pathlib import Path

DATA_DIR = Path("Dataset/Processed")

HI_EN_FILE = DATA_DIR/"hi_en.txt"
EN_OR_FILE = DATA_DIR/"en_or.txt"

def load_text():
    texts=[]
    for file_path in [HI_EN_FILE,EN_OR_FILE]:
        with open(file_path,encoding="utf-8") as f:
            for line in f:
                src,trg=line.split("|||")
                texts.append(src.strip())
                texts.append(trg.strip())
    return texts
def tokenize_dataset(file_path,tokenizer,max_len=120):
    encoded_pairs=[]
    
    with open(file_path, encoding="utf-8") as f:
        for line in f :
            src,trg=line.split("|||")
            
            src_ids = tokenizer.encode(src.strip())
            trg_ids = tokenizer.encode(trg.strip())
            
            if len(src_ids) <= max_len and len(trg_ids) <= max_len:
                encoded_pairs.append((src_ids, trg_ids))

    return encoded_pairs

if __name__ == "__main__":
    print("Loading texts...")
    texts = load_text()

    print("Building vocabulary...")
    tokenizer = CharTokenizer()
    tokenizer.build_vocab(texts)

    print("Vocabulary size:", tokenizer.vocab_size)

    print("Tokenizing HI → EN...")
    hi_en_data = tokenize_dataset(HI_EN_FILE, tokenizer)

    print("Tokenizing EN → OR...")
    en_or_data = tokenize_dataset(EN_OR_FILE, tokenizer)

    print("Sample HI → EN pair:")
    print(hi_en_data[0])

    print("Decoded back:")
    print(
        tokenizer.decode(hi_en_data[0][0]),
        "|||",
        tokenizer.decode(hi_en_data[0][1])
    )
    print("Done.")
