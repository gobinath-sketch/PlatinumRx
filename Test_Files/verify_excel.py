import pandas as pd
import os

xlsx_path = 'Spreadsheets/Ticket_Analysis.xlsx'

def verify_excel():
    if not os.path.exists(xlsx_path):
        print(f"File not found: {xlsx_path}")
        return

    print(f"--- Verifying {xlsx_path} ---")
    
    # Check sheets
    xl = pd.ExcelFile(xlsx_path)
    print(f"Sheets found: {xl.sheet_names}")
    
    # Verify 'ticket' sheet logic
    df_ticket = pd.read_excel(xlsx_path, sheet_name='ticket')
    print(f"Ticket Sheet Sample:\n{df_ticket[['cms_id', 'Solved Same Day', 'Solved Same Hour']].head()}")
    
    # Verify 'feedbacks' sheet mapping
    df_feed = pd.read_excel(xlsx_path, sheet_name='feedbacks')
    print(f"Feedback Sheet Sample (Checking VLOOKUP logic):\n{df_feed[['feedback_id', 'outlet_name', 'assigned_to']].head()}")
    
    # Verify 'Dashboard' sheet
    df_dash = pd.read_excel(xlsx_path, sheet_name='Dashboard')
    print(f"Dashboard Sheet Summary:\n{df_dash}")

if __name__ == "__main__":
    verify_excel()
