import pandas as pd
import os
import csv_pm_llm_parsing
import traceback


def execute_script():
    path = "../testfiles/sep_detection"

    files = os.listdir(path)

    for file in files:
        if file.endswith("csv"):
            full_path = os.path.join(path, file)

            try:
                dataframe = csv_pm_llm_parsing.detect_sep_and_load(full_path, input_encoding="utf-8")
                dataframe.info()
                print(dataframe)
            except:
                traceback.print_exc()
                print("failed detection for", full_path)


if __name__ == "__main__":
    execute_script()
