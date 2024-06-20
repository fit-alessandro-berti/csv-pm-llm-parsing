import pandas as pd
import os
import csv_pm_llm_parsing
import traceback


def execute_script():
    path = "../testfiles/timest_format"

    files = os.listdir(path)

    for file in files:
        if file.endswith("csv"):
            full_path = os.path.join(path, file)

            try:
                dataframe = pd.read_csv(full_path)
                dataframe = csv_pm_llm_parsing.apply_timest_parser(dataframe, timest_column="time:timestamp", max_retry=1)
                dataframe.info()
                print(dataframe)
            except:
                traceback.print_exc()
                print("failed parsing for", file)


if __name__ == "__main__":
    execute_script()
