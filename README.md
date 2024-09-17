# Data Engineer Take-home Assignment

## Requirements
- Python 3.7+
- Pandas
- Requests
- Pytest (for running tests)

## Setup

1. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Place the provided `Country-Code.xlsx` file** in the project directory.

3. **Run the main script:**
    ```bash
    python src/main.py
    ```

## Explanation

The project is organized into three main steps:

1. **Fetch restaurant details** from the provided URL and save them to `restaurant_details.csv`.
2. **Extract event data** for April 2019 and save it to `restaurant_events.csv`.
3. **Analyze the user ratings** and save the updated data to `restaurant_details_with_ratings.csv`.

## Running the Tests

The project includes unit tests to verify that the data extraction, analysis, and utility functions work as expected. The tests are located in the `tests/` directory.

1. **Run the tests** using `pytest`:

    ```bash
    pytest
    ```

2. **Run a specific test file**:

    If you'd like to run tests for a specific file, you can specify the test file:

    ```bash
    pytest tests/test_extract_data.py
    ```

3. **View detailed output**:

    To get detailed output from the tests, use the `-v` flag:

    ```bash
    pytest -v
    ```

## Directory Structure

project_root/
│
├── src/                             # Your source code
│   ├── extract_data.py              # Contains extraction functions
│   ├── main.py                      # Main entry point for the program
│   ├── utils.py                     # Utility functions (e.g., saving/loading)
│   ├── analyze_ratings.py           # Rating analysis logic
│
├── tests/                           # Directory for all test files
│   ├── __init__.py                  # Makes it a package (can be empty)
│   ├── test_extract_data.py         # Unit tests for extract_data.py
│   ├── test_utils.py                # Unit tests for utils.py
│   ├── test_analyze_ratings.py      # Unit tests for analyze_ratings.py
│
├── Country-Code.xlsx                # Excel file for country codes
├── requirements.txt                 # Dependencies (like pytest, pandas, requests)
└── README.md                        # Project documentation


## Notes
- Ensure that you have the `Country-Code.xlsx` file in place before running the main script.
- Make sure your environment meets the requirements listed in `requirements.txt`.
