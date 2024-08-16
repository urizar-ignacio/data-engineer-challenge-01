from typing import List, Tuple
from emoji import EMOJI_DATA
from threading import Thread
from collections import Counter
import json

def count_emojis(record_list, emoji_list, results):
    emoji_count = {}
    for record in record_list:
        for char in record:
            if char in emoji_list:
                current_count = emoji_count.get(char, 0)
                emoji_count[char] = current_count + 1

    results.append(emoji_count)
    return emoji_count

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    records = []
    with open(f"/app/data/{file_path}") as jfile:
        for line in jfile:
            jline = json.loads(line)
            records.append(jline["content"])

    emoji_list = set(EMOJI_DATA.keys())
    threads = []
    results = []

    chunk_size = 10000
    for i in range((len(records)//chunk_size)+1):
        task = Thread(target=count_emojis, kwargs={"record_list":records[i*chunk_size:(i+1)*chunk_size], "emoji_list": emoji_list, "results":results})
        threads.append(task)
        task.start()
    
    for task in threads:
            task.join()

    c = Counter()
    for count in results:
        c.update(count)
    
    return sorted(list(dict(c).items()), key=lambda x: x[1], reverse=True)[:10]