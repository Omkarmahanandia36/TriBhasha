from pathlib import Path
from tokenizer.char_tokenizer import CharTokenizer

DATA_FILE=Path("Dataset/processed/hi_en.txt")
MAX_SEQ_LEN=40

def load_pairs():
    pairs=[]
    with open(DATA_FILE,encoding="utf-8") as f :
        for line in f :
            src,trg=line.split("|||")
            pairs.append((src.strip(),trg.strip()))
    return pairs


def pad_sequence(seq,max_len,pad_id):
    if len(seq)<max_len:
        seq=seq+[pad_id]*(max_len-len(seq))
    else:
        seq=seq[:max_len]
    return seq
if __name__=="__main__":
    print("loading data ...")
    pairs=load_pairs()
    
    print("bulidng tokenizer...")
    tokenizer=CharTokenizer()
    texts=[s for s,t in pairs] +[t for s,t in pairs]
    
    tokenizer.build_vocab(texts)
    print("Vocab size:", tokenizer.vocab_size)
    encoder_inputs = []
    decoder_inputs = []
    decoder_targets = []

    for src, tgt in pairs:
        enc = tokenizer.encode(src)
        dec = tokenizer.encode(tgt)

        dec_in = dec[:-1]   # remove <EOS>
        dec_out = dec[1:]   # remove <SOS>

        enc = pad_sequence(enc, MAX_SEQ_LEN, tokenizer.char2idx[tokenizer.PAD])
        dec_in = pad_sequence(dec_in, MAX_SEQ_LEN, tokenizer.char2idx[tokenizer.PAD])
        dec_out = pad_sequence(dec_out, MAX_SEQ_LEN, tokenizer.char2idx[tokenizer.PAD])

        encoder_inputs.append(enc)
        decoder_inputs.append(dec_in)
        decoder_targets.append(dec_out)

    print("Samples:")
    print("ENC:", encoder_inputs[0])
    print("DEC_IN:", decoder_inputs[0])
    print("DEC_OUT:", decoder_targets[0])