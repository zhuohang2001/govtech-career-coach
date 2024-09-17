import pytest
import pandas as pd
from src.extract_data import extract_restaurant_details, extract_event_data

# Mock data for testing
mock_json_data = [
    {
        "restaurants": [
            {
                "restaurant": {
                    "id": "1",
                    "name": "Test Restaurant",
                    "location": {"country_id": 1, "city": "Test City"},
                    "user_rating": {"votes": "100", "aggregate_rating": "4.5"},
                    "cuisines": "Italian"
                }
            }
        ]
    }
]

mock_country_code = pd.DataFrame({
    'Country Code': [1],
    'Country': ['Test Country']
})

# Test for extract_restaurant_details function
def test_extract_restaurant_details(monkeypatch):
    """
    Test that the extract_restaurant_details function correctly processes
    restaurant data and matches it with the country codes from the Excel file.
    """

    # Mock the response of requests.get and pd.read_excel
    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return mock_json_data
        return MockResponse()

    def mock_read_excel(*args, **kwargs):
        return mock_country_code

    monkeypatch.setattr('requests.get', mock_get)
    monkeypatch.setattr('pandas.read_excel', mock_read_excel)

    # Call the function
    df = extract_restaurant_details('mock_url', 'mock_excel')

    # Check if the dataframe is correct
    assert df.shape == (1, 7)
    assert df['Restaurant Name'].iloc[0] == "Test Restaurant"
    assert df['Country'].iloc[0] == "Test Country"
