# csv-pm-llm-parsing

LLM-based CSV parsing for Process Mining purposes.
It is compatible with advanced LLMs exposing the OpenAI's API.

## How to install

**pip install -U csv_pm_llm_parsing**

## How to set up the LLM connection

Please provide the *openai_api_url*, *openai_api_key*, and *openai_model* as in the examples below.

Alternatively, they could be set up in the system environment variables **OPENAI_API_URL**, **OPENAI_API_KEY**, and **OPENAI_MODEL**.

Examples settings:
* OpenAI's GPT-4O: *openai_api_url='https://api.openai.com/v1'*, *openai_api_key='sk'*, *openai_model='gpt-4o'*
* Locally run (small) LLM (https://ollama.com/library/qwen2:72b-instruct-q6_K): *openai_api_url='http://127.0.0.1:11434/v1*, *openai_api_key='sk'*, *openai_model='qwen2:72b-instruct-q6_K'*
* DeepInfra (Qwen/Qwen2-72B-Instruct): *openai_api_url='https://api.deepinfra.com/v1/openai/'*, *openai_api_key='adssad'*, *openai_model='Qwen/Qwen2-72B-Instruct'*

## Modules

### Separator and Quotechar detection (using LLMs)

**Example code**:

```python
import csv_pm_llm_parsing  

csv_path = "testfiles/sep_detection/01_comma_doublequote.csv"  
format = csv_pm_llm_parsing.detect_sep_and_quote(csv_path, input_encoding="utf-8", openai_api_url="https://api.openai.com/v1", openai_api_key="sk-", openai_model="gpt-4o", return_detected_sep=True)  
print(format)  
```

### Case ID, Activity, and Timestamp columns detection (using LLMs)

**Example code**:

```python
import pandas as pd  
import csv_pm_llm_parsing  

csv_path = "testfiles/cid_acti_timest/01.csv"  
dataframe = pd.read_csv(csv_path)  
main_columns = csv_pm_llm_parsing.detect_caseid_activity_timestamp(dataframe, openai_api_url="https://api.openai.com/v1", openai_api_key="sk-", openai_model="gpt-4o", return_suggestions=True)  
print(main_columns)  
```

### Timestamp Format detection (using LLMs)

**Example code**:

```python
import pandas as pd  
import csv_pm_llm_parsing  

csv_path = "testfiles/timest_format/05_rfc1123.csv"  
dataframe = pd.read_csv(csv_path)  
timest_column = "time:timestamp"  
timest_format = csv_pm_llm_parsing.detect_timest_format(dataframe, timest_column=timest_column, openai_api_url="https://api.openai.com/v1", openai_api_key="sk-", openai_model="gpt-4o", return_timest_format=True)  
print(timest_format)  
dataframe[timest_column] = pd.to_datetime(dataframe[timest_column], format=timest_format)  
dataframe.info()  
```

## OVERALL CSV PARSING (executes all the modules)

**Example code**:

```python
import csv_pm_llm_parsing  

csv_path = "testfiles/overall/01.csv"  
dataframe = csv_pm_llm_parsing.full_parse_csv_for_pm(csv_path, openai_api_url="https://api.openai.com/v1", openai_api_key="sk-", openai_model="gpt-4o")  
dataframe.info()  
print(dataframe)  
```