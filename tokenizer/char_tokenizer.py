from collections import Counter

class CharTokenizer:
    def __init__(self):
        self.char2idx={}
        self.idx2char={}
        self.vocab_size=0
        
        self.PAD="<PAD>"
        self.SOS="<SOS>"
        self.EOS="<EOS>"
        self.UNK="<UNK>"
        
    def build_vocab(self,texts):
        counter=Counter()
        
        for text in texts:
            for ch in text:
                counter[ch]+=1
        vocab=[self.PAD,self.SOS,self.EOS,self.UNK]+sorted(counter.keys())
        self.char2idx={ch:i for i,ch in enumerate(vocab)}
        self.idx2char={i:ch for ch,i in self.char2idx.items()}
        self.vocab_size = len(vocab)

    def encode(self, text):
        ids = [self.char2idx[self.SOS]]
        for ch in text:
            ids.append(self.char2idx.get(ch, self.char2idx[self.UNK]))
        ids.append(self.char2idx[self.EOS])
        return ids

    def decode(self, ids):
        chars = []
        for i in ids:
            ch = self.idx2char.get(i, "")
            if ch not in {self.PAD, self.SOS, self.EOS}:
                chars.append(ch)
        return "".join(chars)