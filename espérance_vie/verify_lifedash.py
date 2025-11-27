import streamlit as st
import pandas as pd
# Mock streamlit to avoid errors during import if necessary, 
# but for now let's just try to import the function.
# Streamlit commands might warn or fail if not run via `streamlit run`, 
# but we just want to test load_data.

try:
    from lifedash import load_data
    
    print("Attempting to load data...")
    df = load_data()
    
    if not df.empty:
        print("Data loaded successfully!")
        print("Columns:", df.columns.tolist())
        print("Shape:", df.shape)
        
        expected_columns = ["Country", "Year", "LifeExpectancy"]
        if all(col in df.columns for col in expected_columns):
            print("Verification PASSED: All expected columns are present.")
        else:
            print(f"Verification FAILED: Missing columns. Expected {expected_columns}, got {df.columns.tolist()}")
            
        # Verify content of Country column for expected values
        countries = df['Country'].unique()
        print("Sample Countries:", countries[:5])
        
    else:
        print("Verification FAILED: DataFrame is empty.")

except Exception as e:
    print(f"Verification FAILED with error: {e}")
