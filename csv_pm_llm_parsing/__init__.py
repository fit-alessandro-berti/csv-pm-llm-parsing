import pandas as pd
from csv_pm_llm_parsing import constants, meta
from typing import Optional, Union, Dict


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
        Pandas dataframe (with the timestamp column parsed)
    """
    from csv_pm_llm_parsing import timest_parser
    return timest_parser.apply_timest_parser(df, timest_column=timest_column, max_head_n=max_head_n,
                                             max_retry=max_retry, openai_api_url=openai_api_url,
                                             openai_api_key=openai_api_key, openai_model=openai_model)


def detect_sep_and_load(file_path: str, input_encoding: str = "utf-8", read_bytes: int = 2048,
                        max_retry: int = constants.MAX_RETRY, openai_api_url: Optional[str] = None,
                        openai_api_key: Optional[str] = None,
                        openai_model: Optional[str] = None) -> pd.DataFrame:
    """
    Detects the separator and quotechar in the provided file using LLMs.

    Parameters
    ----------------
    file_path
        Path to the file
    input_encoding
        Encoding of the file (default: utf-8)
    read_bytes
        Number of bytes that should be initially considered
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
    from csv_pm_llm_parsing import sep_detection
    return sep_detection.detect_sep_and_load(file_path, input_encoding=input_encoding, read_bytes=read_bytes,
                                             max_retry=max_retry, openai_api_url=openai_api_url,
                                             openai_api_key=openai_api_key, openai_model=openai_model)


def detect_caseid_activity_timestamp(df: pd.DataFrame, max_retry: int = constants.MAX_RETRY,
                                     openai_api_url: Optional[str] = None,
                                     openai_api_key: Optional[str] = None,
                                     openai_model: Optional[str] = None, return_suggestions: bool = False) -> Union[
    pd.DataFrame, Dict[str, str]]:
    """
    Detects automatically the columns to use as case identifier, activity, and timestamp in the provided dataframe.

    Parameters
    -----------------
    df
        Pandas dataframe
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
        Pandas dataframe with standard column names (i.e., in pm4py, 'case:concept:name' for the case ID, 'concept:name' for the activity, and 'time:timestamp' for the timestamp).
    """
    from csv_pm_llm_parsing import pm_columns_detection
    return pm_columns_detection.detect_caseid_activity_timestamp(df, max_retry=max_retry, openai_api_url=openai_api_url,
                                                                 openai_api_key=openai_api_key,
                                                                 openai_model=openai_model,
                                                                 return_suggestions=return_suggestions)
