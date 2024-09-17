import pytest
import pandas as pd
from src.analyze_ratings import translate_rating_text, analyze_ratings

# Mock data for testing
mock_json_data = [
    {
        "restaurants": [
            {
                "restaurant": {
                    "id": "1",
                    "name": "Test Restaurant",
                    "location": {"country_id": 1, "city": "Test City"},
                    "user_rating": {"votes": "100", "aggregate_rating": "4.5", "rating_text": "Excelente"}
                }
            },
            {
                "restaurant": {
                    "id": "2",
                    "name": "Test Restaurant 2",
                    "location": {"country_id": 1, "city": "Test City 2"},
                    "user_rating": {"votes": "50", "aggregate_rating": "3.8", "rating_text": "Bueno"}
                }
            }
        ]
    }
]

# Test for translate_rating_text function
def test_translate_rating_text():
    assert translate_rating_text("Bardzo dobrze") == "Very Good"
    assert translate_rating_text("Bueno") == "Good"
    assert translate_rating_text("Skvělé") == "Excellent"
    assert translate_rating_text("Unknown text") == "Unknown text"  # Should return as-is

# Test for analyze_ratings function
def test_analyze_ratings(monkeypatch):
    # Mock the response of requests.get
    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return mock_json_data
        return MockResponse()

    monkeypatch.setattr('requests.get', mock_get)

    # Call the function
    df = analyze_ratings('mock_url')

    # Check if the DataFrame is structured as expected
    print(df, "df")
    assert df.shape == (3, 5)
    assert 'Excellent' in df.columns  # Ensure the "Excellent" category is present
    assert 'Good' in df.columns      # Ensure the "Good" category is present
    
    # Check if the values are correct
    assert df['Excellent']['min'] == 4.5
    assert df['Good']['min'] == 3.8
    assert df['Good']['average'] == 3.8