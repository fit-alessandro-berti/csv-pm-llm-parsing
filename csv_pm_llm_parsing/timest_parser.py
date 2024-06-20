import pandas as pd


def apply_timest_parser(df: pd.DataFrame, timest_column: str = "time:timestamp", max_head_n: int = 10) -> pd.DataFrame:
    head_values = list(df[timest_column].head(min(len(df), max_head_n)))
    print(head_values)
