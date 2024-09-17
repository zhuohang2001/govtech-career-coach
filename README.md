# Data Engineer Take-home Assignment

## Requirements
- Python 3.7+
- Pandas
- Requests

## Setup
1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Place the provided `Country-Code.xlsx` file in the project directory.

3. Run the main script:
    ```bash
    python main.py
    ```

## Explanation
The project is organized into three main steps:
1. Fetch restaurant details from the provided URL and save them to `restaurant_details.csv`.
2. Extract event data for April 2019 and save it to `restaurant_events.csv`.
3. Analyze the user ratings and save the updated data to `restaurant_details_with_ratings.csv`.
