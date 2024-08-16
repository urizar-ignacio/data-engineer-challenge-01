from emoji import EMOJI_DATA
from itertools import groupby
from typing import List, Tuple
import json

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    with open(f"/app/data/{file_path}") as jfile:
        records = [json.loads(line)["content"] for line in jfile]

    emoji_found = []
    emoji_list = EMOJI_DATA.keys()
    for record in records:
        emoji_found = emoji_found + [char for char in record if char in emoji_list]
    emoji_found_sorted = sorted(emoji_found)
    del emoji_found
    emoji_count = [(k, len(list(g))) for k, g in groupby(emoji_found_sorted, lambda x: x)]
    
    return sorted(emoji_count, key=lambda x: x[1], reverse=True)[:10]