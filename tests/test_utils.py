import pandas as pd
from src.utils import save_to_csv, load_json, load_excel
import json

# Test for save_to_csv function
def test_save_to_csv(tmpdir):
    # Create a simple dataframe
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    file_path = tmpdir.join("test.csv")
    
    # Call save_to_csv
    save_to_csv(df, str(file_path), False)

    # Check if the file was written correctly
    written_df = pd.read_csv(file_path)
    pd.testing.assert_frame_equal(df, written_df)

# Test for load_json function
def test_load_json(tmpdir):
    json_data = {"key": "value"}
    file_path = tmpdir.join("test.json")

    # Write mock JSON file
    with open(file_path, "w") as f:
        json.dump(json_data, f)

    # Test load_json function
    result = load_json(str(file_path))
    assert result == json_data

# Test for load_excel function
def test_load_excel(tmpdir):
    excel_data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    file_path = tmpdir.join("test.xlsx")

    # Save mock Excel file
    excel_data.to_excel(file_path, index=False)

    # Test load_excel function
    result = load_excel(str(file_path))
    pd.testing.assert_frame_equal(excel_data, result)
