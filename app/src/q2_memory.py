from emoji import EMOJI_DATA
from typing import List, Tuple
import json

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    with open(f"/app/data/{file_path}") as jfile:
        records = [json.loads(line)["content"] for line in jfile]

    emoji_list = EMOJI_DATA.keys()
    emoji_count = {}
    for record in records:
        for char in record:
            if char in emoji_list:
                current_count = emoji_count.get(char, 0)
                emoji_count[char] = current_count + 1
    emoji_found_sorted = sorted(list(emoji_count.items()), key=lambda x: x[1], reverse=True)
    
    return emoji_found_sorted[:10]