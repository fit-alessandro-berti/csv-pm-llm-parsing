import pandas as pd
from csv_pm_llm_parsing import constants, util
import traceback
import time


def apply_timest_parser(df: pd.DataFrame, timest_column: str = "time:timestamp", max_head_n: int = 10,
                        max_retry: int = constants.MAX_RETRY) -> pd.DataFrame:
    head_values = list(df[timest_column].head(min(len(df), max_head_n)))

    prompt = "Given the following list of timestamps: " + str(head_values)
    prompt += "\n\nCan you propose the timestamp format that I should use as parameter for Pandas timestamp parsing?"
    prompt += "\n\nPlease include the proposed format in a JSON, like: {\"format\": PROPOSEDFORMAT}"

    parsed = False
    for i in range(max_retry):
        try:
            proposed_format = util.get_json(util.openai_inquiry(prompt))["format"]
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
