import re
import string
from typing import Dict, List, Tuple
from cyb_python.utils import chunks


class Text:
    text: str

    def __init__(self, path: str) -> None:
        with open(path) as fin:
            self.text = fin.read()

    def chunk_freq(self, f: int) -> List[Tuple[str, int]]:
        freq_dict: Dict[str, int] = {}

        for chunk in chunks(self.text, f):
            freq_dict[chunk] = freq_dict.get(chunk, 0) + 1

        items = list(freq_dict.items())
        items.sort(key=lambda x: x[1], reverse=True)
        # freqs = sorted(freq_dict.values(), reverse=True)
        # return freqs
        return items

    def positions(self, clip: str) -> List[int]:
        return [m.start() for m in re.finditer(clip, self.text)]

    @staticmethod
    def freq(text: str) -> List[Tuple[str, int]]:
        """
        Get the letter frequency in `text` in descending order
        """
        freqs = {
            alpha: 0 for alpha in string.ascii_uppercase
        }
        for char in text.upper():
            if char in freqs:
                freqs[char] += 1
        return sorted(list(freqs.items()), key=lambda it: it[1], reverse=True)