from typing import List, Dict

class Solution:
    def tokenize_numbers(self, numbers: List[int], vocab: Dict[str, int]) -> List[List[str]]:
        # Tokenize each number using greedy left-to-right longest match.
        # Return a list of token lists showing how each number gets split.
        pass

        return [self.tokenize(str(num), vocab) for num in numbers]

    def count_tokens(self, text: str, vocab: Dict[str, int]) -> int:
        # Count how many tokens the text uses with greedy tokenization.
        # Use greedy left-to-right longest match.
        pass

        return len(self.tokenize(text, vocab))

    def fertility_score(self, text: str, vocab: Dict[str, int]) -> float:
        # Compute tokens-per-word ratio (fertility).
        # Higher = more expensive and less efficient.
        # Round to 4 decimal places.
        pass

        word_count = len(text.split())

        if word_count == 0:
            return 0.0

        token_count = self.count_tokens(text, vocab)

        return round(token_count / word_count, 4)

    def tokenize(self, text: str, vocab: Dict[str, int]) -> List[str]:
        tokens = []
        i = 0
        max_len = max(map(len, vocab), default=1)

        while i < len(text):
            for j in range(min(len(text), i + max_len), i, -1):
                token = text[i:j]

                if token in vocab:
                    tokens.append(token)
                    i = j
                    break
            else:
                tokens.append(text[i])
                i += 1

        return tokens






