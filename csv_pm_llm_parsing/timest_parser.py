import pandas as pd
from csv_pm_llm_parsing import constants, util
import traceback
import time
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
    df[timest_column] = df[timest_column].astype(str).apply(lambda x: x.strip())
    head_values = list(df[timest_column].head(min(len(df), max_head_n)))

    prompt = "Given the following list of timestamps: " + str(head_values)
    prompt += "\n\nCan you propose the timestamp format that I should use as parameter for Pandas timestamp parsing?"
    prompt += "\n\nPlease include the proposed format in a JSON, like: {\"format\": PROPOSEDFORMAT}"

    parsed = False
    for i in range(max_retry):
        try:
            proposed_format = util.get_json(
                util.openai_inquiry(prompt.encode('utf-8', errors='ignore').decode('utf-8'), openai_api_url=openai_api_url, openai_api_key=openai_api_key,
                                    openai_model=openai_model))["format"]
            df[timest_column] = pd.to_datetime(df[timest_column], format=proposed_format)
            parsed = True
            break
        except Exception as e:
            traceback.print_exc()
            prompt += "\n\nI am getting the following error: " + str(e)
            time.sleep(constants.SLEEP_TIME)

    if not parsed:
        raise Exception("failed parsing of the timestamp column: " + timest_column)

    return df
