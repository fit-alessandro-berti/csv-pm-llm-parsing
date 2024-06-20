import pandas as pd
from csv_pm_llm_parsing import constants, meta
from typing import Optional


def apply_timest_parser(df: pd.DataFrame, timest_column: str = "time:timestamp", max_head_n: int = 10,
                        max_retry: int = constants.MAX_RETRY, openai_api_url: Optional[str] = None,
                        openai_api_key: Optional[str] = None,
                        openai_model: Optional[str] = None) -> pd.DataFrame:
    """
    Automatically detects the format of the timestamp in the specified column using LLMs.
    The Pandas dataframe's column is then parsed using the given format.

    Parameters
    ---------------
    df
        Pandas dataframe
    timest_column
        Column to which we aim to apply the automatic timestamp format detection
    max_head_n
        Number of top values that should be provided to the LLM
    max_retry
        Maximum number of retries upon failure
    openai_api_url
        API URL (like https://api.openai.com/v1 or http://127.0.0.1:11434/v1 )
    openai_api_key
        API key
    openai_model
        OpenAI model

    Returns
    ----------------
    df
        Pandas dataframe
    """
    from csv_pm_llm_parsing import timest_parser
    return timest_parser.apply_timest_parser(df, timest_column=timest_column, max_head_n=max_head_n,
                                             max_retry=max_retry, openai_api_url=openai_api_url,
                                             openai_api_key=openai_api_key, openai_model=openai_model)
