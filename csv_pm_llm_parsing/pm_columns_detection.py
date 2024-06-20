import pandas as pd
from csv_pm_llm_parsing import constants, util
from typing import Optional, Dict, Any, Union
import io, traceback, time


def detect_caseid_activity_timestamp(df: pd.DataFrame, max_retry: int = constants.MAX_RETRY,
                                     openai_api_url: Optional[str] = None,
                                     openai_api_key: Optional[str] = None,
                                     openai_model: Optional[str] = None, return_suggestions: bool = False) -> Union[
    pd.DataFrame, Dict[str, str]]:
    buf = io.StringIO()
    df.info(buf=buf)
    s = buf.getvalue()
    prompt = "Given the dataframe with the following columns:\n\n"
    prompt += s
    prompt += "\n\nCan you suggest some columns for the case identifier, activity, and completion timestamp?\n"
    prompt += "Please produce a JSON containing as keys: 'caseid', 'activity', 'timestamp'"

    suggested = False
    for i in range(max_retry):
        try:
            suggestions = util.get_json(util.openai_inquiry(prompt.encode('utf-8', errors='ignore').decode('utf-8'),
                                                            openai_api_url=openai_api_url,
                                                            openai_api_key=openai_api_key,
                                                            openai_model=openai_model))
            df[suggestions['caseid']]
            df[suggestions['activity']]
            df[suggestions['timestamp']]
            suggested = True
            df['case:concept:name'] = df[suggestions['caseid']]
            df['concept:name'] = df[suggestions['activity']]
            df['time:timestamp'] = df[suggestions['timestamp']]
        except Exception as e:
            traceback.print_exc()
            prompt += "\n\nI am getting the following error: " + str(e)
            time.sleep(constants.SLEEP_TIME)

    if not suggested:
        raise Exception("failed process mining column detection")

    return df
