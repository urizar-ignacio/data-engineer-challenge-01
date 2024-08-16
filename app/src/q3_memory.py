from typing import List, Tuple
import json
import re

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    with open(f"/app/data/{file_path}") as jfile:
        records = [json.loads(line)["content"] for line in jfile if '@' in line]

    mention_counter = {}
    for record in records:
        mentions = [mention.group() for mention in re.finditer(r"@([a-zA-Z0-9_]){4,15}\b", record)]
        for mention in mentions:
            current_count = mention_counter.get(mention, 0)
            mention_counter[mention] = current_count + 1

    mention_counter_sorted = sorted(list(mention_counter.items()), key=lambda x: x[1], reverse=True)
    
    return mention_counter_sorted[:10]
