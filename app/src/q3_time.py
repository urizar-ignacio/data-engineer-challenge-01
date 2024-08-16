from typing import List, Tuple
from threading import Thread
from collections import Counter
import json
import re

def count_mentions(record_list, results):
    mention_counter = {}
    for record in record_list:
        mentions = [mention.group() for mention in re.finditer(r"@([a-zA-Z0-9_]){4,15}\b", record)]
        for mention in mentions:
            current_count = mention_counter.get(mention, 0)
            mention_counter[mention] = current_count + 1

    results.append(mention_counter)
    return True

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    records = []
    with open(f"/app/data/{file_path}") as jfile:
        records = [json.loads(line)["content"] for line in jfile if '@' in line]

    threads = []
    results = []

    chunk_size = 10000
    for i in range((len(records)//chunk_size)+1):
        task = Thread(target=count_mentions, kwargs={"record_list":records[i*chunk_size:(i+1)*chunk_size], "results":results})
        threads.append(task)
        task.start()
    
    for task in threads:
            task.join()

    c = Counter()
    for count in results:
        c.update(count)
    
    return sorted(list(dict(c).items()), key=lambda x: x[1], reverse=True)[:10]