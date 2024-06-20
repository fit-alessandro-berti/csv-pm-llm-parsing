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
                dataframe = csv_pm_llm_parsing.full_parse_csv_for_pm(full_path)
                dataframe.info()
                print(dataframe)
            except:
                traceback.print_exc()
                print("failed overall parsing for", full_path)


if __name__ == "__main__":
    execute_script()
