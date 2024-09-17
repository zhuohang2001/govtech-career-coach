import requests
import pandas as pd

def translate_rating_text(rating_text):
    """
    Translation dictionary from the original languages to English
    below in dict (line 15) are the possible values of text ratings based on the data provided using the code chunk here:
    lst = []
    for r in restaurant_data:
        for rest in r["restaurants"]:
            restaurant = rest["restaurant"]
            if "user_rating" in restaurant:
                lst.append(restaurant["user_rating"]["rating_text"])
    set(lst)
    """

    translations = {
        'Bardzo dobrze': 'Very Good',
        'Bueno': 'Good',
        'Eccellente': 'Excellent',
        'Excelente': 'Excellent',
        'Skvělá volba': 'Excellent',
        'Skvělé': 'Excellent',
        'Terbaik': 'Excellent',
        'Velmi dobré': 'Very Good',
        'Muito Bom': 'Very Good',
        'Muy Bueno': 'Very Good',
        'Poor': 'Poor',
        'Good': 'Good',
        'Average': 'Average',
        'Excellent': 'Excellent',
        'Not rated': 'Not rated',
    }

    # Return the English translation if exists, otherwise return the original text
    return translations.get(rating_text, rating_text)

def analyze_ratings(json_url):
    """
    Analyze restaurant ratings from the provided JSON URL.
    
    Args:
        json_url (str): URL of the JSON data containing restaurant information.
    
    Returns:
        pd.DataFrame: A DataFrame with rating thresholds (min, max, average).
    """

    rating_data = {
        'Excellent': [],
        'Very Good': [],
        'Good': [],
        'Average': [],
        'Poor': []
    }

    response = requests.get(json_url)
    restaurant_data = response.json()

    # Collect aggregate ratings based on translated rating texts
    for r in restaurant_data:
        for rest in r["restaurants"]:
            restaurant = rest["restaurant"]
            if "user_rating" in restaurant:
                rating_text = translate_rating_text(restaurant["user_rating"]["rating_text"])
                aggregate_rating = float(restaurant["user_rating"]["aggregate_rating"])
                
                # Only consider relevant rating texts
                if rating_text in rating_data:
                    rating_data[rating_text].append(aggregate_rating)

    # Calculate the thresholds for each category
    thresholds = {}
    for rating_text, ratings in rating_data.items():
        if ratings:
            thresholds[rating_text] = [min(ratings), max(ratings), sum(ratings) / len(ratings)]
        else:
            thresholds[rating_text] = [None, None, None]

    df = pd.DataFrame(thresholds, index=['min', 'max', 'average'])
    return df