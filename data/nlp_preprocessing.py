import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        sentences = positive + negative
        words = sorted(set(word for sentence in sentences for word in sentence.split()))
        vocab = {word: 1 + i for i, word in enumerate(words)}

        # 2. Encode each sentence by replacing words with their IDs
        encoded = [
            torch.tensor([vocab[word] for word in sentence.split()], dtype=torch.float32)
            for sentence in sentences
        ]

        # 3. Combine positive + negative into one list of tensors
        tensors = encoded

        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        result = nn.utils.rnn.pad_sequence(tensors, batch_first=True, padding_value=0)

        return result
        pass
