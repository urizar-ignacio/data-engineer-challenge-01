from typing import List, Tuple
from datetime import datetime
from itertools import groupby
from json import loads


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    records = []
    with open(f"/app/data/{file_path}") as jfile:
        for line in jfile:
            jline = loads(line)
            records.append({"date": jline["date"][:10], "username": jline["user"]["username"]})
    
    ordered_by_date_records = sorted(records, key=lambda x: x["date"])
    count_by_date = [(k, len(list(g))) for k, g in (groupby(ordered_by_date_records, lambda x: x["date"]))]
    top_count_by_day = sorted(count_by_date, key=lambda x: x[1], reverse=True)[:10]

    ordered_by_date_username_records = sorted(records, key=lambda x: (x["date"], x["username"]))
    count_by_date_and_user = [(k, len(list(g))) for k, g in (groupby(ordered_by_date_username_records, lambda x: (x["date"],x["username"])))]

    results = []
    for top_date in top_count_by_day:
        filter_group = filter(lambda x: x[0][0] == top_date[0], count_by_date_and_user)
        username = max(filter_group, key=lambda x: x[1])[0][1]
        results.append((datetime.strptime(top_date[0], '%Y-%m-%d').date(), username))

    del ordered_by_date_records
    del count_by_date
    del top_count_by_day
    del ordered_by_date_username_records
    del count_by_date_and_user
    return results