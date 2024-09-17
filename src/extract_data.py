import pandas as pd
import requests
import json

def extract_restaurant_details(json_url, excel_file):
    response = requests.get(json_url)
    restaurant_data = response.json()  # Parse the JSON data from the URL
    
    country_codes = pd.read_excel(excel_file)  # Load country codes from local file

    restaurant_details = []
    for entry in restaurant_data:
        for restaurant in entry['restaurants']:
            country_code = restaurant['restaurant']['location']['country_id']
            if country_code in country_codes['Country Code'].values:
                restaurant_details.append({
                    'Restaurant Id': restaurant['restaurant']['id'],
                    'Restaurant Name': restaurant['restaurant']['name'],
                    'Country': country_codes[country_codes['Country Code'] == country_code]['Country'].values[0],
                    'City': restaurant['restaurant']['location']['city'],
                    'User Rating Votes': restaurant['restaurant']['user_rating']['votes'],
                    'User Aggregate Rating': float(restaurant['restaurant']['user_rating']['aggregate_rating']),
                    'Cuisines': restaurant['restaurant']['cuisines']
                })

    return pd.DataFrame(restaurant_details)

# Function to extract event data for April 2019 from URL
def extract_event_data(json_url):
    response = requests.get(json_url)
    restaurant_data = response.json()  # Parse the JSON data from the URL

    event_details = []
    for entry in restaurant_data:
        for rest in entry['restaurants']:
            restaurant = rest["restaurant"]
            if "zomato_events" in restaurant:
                for evt in restaurant["zomato_events"]:
                    event = evt["event"]
                    start_date = pd.to_datetime(event['start_date'])
                    end_date = pd.to_datetime(event['end_date'])
                    photo_url = event["photos"][0]["photo"]["url"] if event.get("photos") else "No Photo"
                    if (start_date <= pd.Timestamp('2019-04-30')) and (end_date >= pd.Timestamp('2019-04-01')):
                        event_details.append({
                            'Event Id': event['event_id'],
                            'Restaurant Id': restaurant["R"]["res_id"],
                            'Restaurant Name': restaurant['name'],
                            'Photo URL': photo_url,
                            'Event Title': event['title'],
                            'Event Start Date': event['start_date'],
                            'Event End Date': event['end_date']
                        })

    return pd.DataFrame(event_details)