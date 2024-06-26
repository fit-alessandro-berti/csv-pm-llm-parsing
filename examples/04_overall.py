import os
import csv_pm_llm_parsing
import traceback


DEBUG = True

def execute_script():
    path = "../testfiles/overall"

    files = os.listdir(path)

    for file in files:
        if file.endswith("csv"):
            full_path = os.path.join(path, file)
            print(full_path)

            try:
                dataframe = csv_pm_llm_parsing.full_parse_csv_for_pm(full_path, debug=DEBUG)
                dataframe.info()
                print(dataframe)
            except:
                traceback.print_exc()
                print("failed overall parsing for", full_path)


if __name__ == "__main__":
    execute_script()
