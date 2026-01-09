import analyse_pmet
import os
import sys
import traceback

try:
    # Use existing file
    file_path = "Recette_2.xlsx"
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        # Try to find any xlsx
        files = [f for f in os.listdir('.') if f.endswith('.xlsx') and not f.startswith('~$')]
        if files:
            file_path = files[0]
            print(f"Using found file: {file_path}")
        else:
            print("No Excel file found for testing.")
            sys.exit(1)
            
    output_dir = os.getcwd()
    print(f"--- START DEBUG TEST on {file_path} ---")
    
    # Simulate the call exactly as in pmet_app.py
    result = analyse_pmet.analyze_file(file_path, output_dir)
    
    print("\n--- RETURN VALUES ---")
    print(f"Type: {type(result)}")
    if isinstance(result, tuple):
        print(f"Length: {len(result)}")
        print(f"Values: {result}")
    else:
        print(f"Value: {result}")
        
    stats, graph_dir, excel_path, rich_excel_path = result
    print("\n--- UNPACKING SUCCESSFUL ---")
    
except Exception:
    print("\n--- ERROR CAUGHT ---")
    traceback.print_exc()
