from typing import List, Tuple
from datetime import datetime
from pandas import DataFrame
import json

def q1_benchmark(file_path: str) -> List[Tuple[datetime.date, str]]:
    records = []
    with open(f"/app/data/{file_path}") as jfile:
        for line in jfile:
            records.append(json.loads(line))
    df = DataFrame.from_records(records)
    df["date"] = df["date"].str[:10]
    df["username"] = df["user"].apply(lambda x: x["username"])

    df_by_day = df.groupby(["date"])["date"].count().nlargest(10).reset_index(name="count")
    df_by_day_user = df.groupby(["date","username"]).size().sort_values(ascending=False).reset_index(name="count").drop_duplicates(subset="date")

    df_join = df_by_day.set_index("date").join(df_by_day_user[["date", "username"]].set_index("date"), on="date", how="left")

    results = list(zip(df_join["username"].index, df_join["username"]))
    results_cast = [(datetime.strptime(x[0], '%Y-%m-%d').date(), x[1]) for x in results]
    return results_cast