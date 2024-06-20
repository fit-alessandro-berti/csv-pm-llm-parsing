import os
import csv_pm_llm_parsing
import traceback
import pandas as pd


def execute_script():
    path = "../testfiles/cid_acti_timest"

    files = os.listdir(path)

    for file in files:
        if file.endswith("csv"):
            full_path = os.path.join(path, file)

            try:
                dataframe = csv_pm_llm_parsing.detect_caseid_activity_timestamp(pd.read_csv(full_path, sep=',', quotechar='\"', encoding="utf-8"))
                dataframe.info()
                print(dataframe)
            except:
                traceback.print_exc()
                print("failed column detection for", full_path)


if __name__ == "__main__":
    execute_script()
