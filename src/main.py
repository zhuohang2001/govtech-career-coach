from extract_data import extract_restaurant_details, extract_event_data
from analyze_ratings import analyze_ratings
from utils import save_to_csv

def main():
    """
    Main script to extract, analyze, and save restaurant data and events.
    """

    # Define URL and file paths
    restaurant_json_url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"
    country_excel_file = "../data/Country-Code.xlsx"
    
    # Question 1: Extract restaurant data and save to CSV
    # 1. Extract the following fields from restaurant_data.json and store them in a CSV file named restaurant_details.csv. 
    # Only include restaurants with a matching Country Code found in Country-Code.xlsx

    restaurant_df = extract_restaurant_details(restaurant_json_url, country_excel_file)
    save_to_csv(restaurant_df, '../output/restaurant_details.csv', False)
    
    # Question 2: Extract event data for April 2019 and save to CSV
    # 2. Extract details of restaurants that had events in April 2019 from restaurant_data.json and store them in a CSV file named restaurant_events.csv:

    event_df = extract_event_data(restaurant_json_url)
    save_to_csv(event_df, '../output/restaurant_events.csv', False)

    # Question 3: Analyze ratings threshold and update CSV
    # 3. Analyse the restaurant data JSON file to determine the threshold for different rating texts based on the aggregate rating. Consider the following rating texts:
    analyzed_df = analyze_ratings(restaurant_json_url)
    save_to_csv(analyzed_df, '../output/restaurant_details_with_ratings.csv', True)


if __name__ == "__main__":
    main()
