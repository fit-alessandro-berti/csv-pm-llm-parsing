import pandas as pd
from csv_pm_llm_parsing import constants, meta


def apply_timest_parser(df: pd.DataFrame, timest_column: str = "time:timestamp", max_head_n: int = 10) -> pd.DataFrame:
    from csv_pm_llm_parsing import timest_parser
    return timest_parser.apply_timest_parser(df, timest_column=timest_column, max_head_n=max_head_n)
