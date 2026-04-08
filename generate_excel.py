import pandas as pd
import numpy as np
import datetime
import os

# =========================================================
# SPREADSHEET PROFICIENCY - PROFESSIONAL EXCEL GENERATOR
# =========================================================

def generate_professional_excel():
    ticket_csv = 'Spreadsheets/Ticket_Analysis_Data.csv'
    feedback_csv = 'Spreadsheets/Feedbacks_Data.csv'
    output_xlsx = 'Spreadsheets/Ticket_Analysis.xlsx'

    if not os.path.exists(ticket_csv) or not os.path.exists(feedback_csv):
        print("CSV files not found in Spreadsheets/ directory.")
        return

    # 1. Process Ticket Data
    df_ticket = pd.read_csv(ticket_csv)
    df_ticket['created_at'] = pd.to_datetime(df_ticket['created_at'])
    df_ticket['closed_at'] = pd.to_datetime(df_ticket['closed_at'])
    
    # Logic: Ticket solved on Same Day
    df_ticket['Solved Same Day'] = df_ticket.apply(
        lambda row: 'Yes' if row['created_at'].date() == row['closed_at'].date() else 'No', 
        axis=1
    )
    
    # Logic: Ticket solved in Same Hour
    df_ticket['Solved Same Hour'] = df_ticket.apply(
        lambda row: 'Yes' if (row['closed_at'] - row['created_at']).total_seconds() < 3600 else 'No',
        axis=1
    )

    # 2. Process Feedback Data (VLOOKUP / XLOOKUP Logic)
    df_feedback = pd.read_csv(feedback_csv)
    
    # Extract metadata from ticket to populate feedback (The "VLOOKUP" equivalent)
    lookup_df = df_ticket[['cms_id', 'outlet_name', 'assigned_to', 'category']]
    df_feedback = df_feedback.merge(lookup_df, on='cms_id', how='left')

    # 3. Create Dashboard Data
    df_dashboard = df_ticket.groupby('outlet_name').agg({
        'cms_id': 'count',
        'Solved Same Day': lambda x: (x == 'Yes').sum()
    }).rename(columns={'cms_id': 'Total Tickets', 'Solved Same Day': 'Same Day Resolution'})
    df_dashboard['Resolution Rate (%)'] = (df_dashboard['Same Day Resolution'] / df_dashboard['Total Tickets'] * 100).round(2)

    # 4. Save to Excel with Professional Styling
    with pd.ExcelWriter(output_xlsx, engine='xlsxwriter') as writer:
        df_ticket.to_excel(writer, sheet_name='ticket', index=False)
        df_feedback.to_excel(writer, sheet_name='feedbacks', index=False)
        df_dashboard.to_excel(writer, sheet_name='Dashboard', index=True)

        workbook = writer.book
        
        # Formats
        header_format = workbook.add_format({
            'bold': True, 'text_wrap': True, 'valign': 'top',
            'fg_color': '#1e293b', 'font_color': '#f8fafc', 'border': 1
        })
        
        # Apply style to all sheets
        for sheet_name in ['ticket', 'feedbacks', 'Dashboard']:
            worksheet = writer.sheets[sheet_name]
            df = df_ticket if sheet_name == 'ticket' else (df_feedback if sheet_name == 'feedbacks' else df_dashboard)
            
            # Set columns for headers
            cols = df.columns.tolist()
            if sheet_name == 'Dashboard': 
                worksheet.write(0, 0, 'Outlet Name', header_format)
                start_col = 1
            else:
                start_col = 0
                
            for col_num, value in enumerate(cols):
                worksheet.write(0, col_num + start_col, value, header_format)
            
            # Adjust column width
            worksheet.set_column(0, 10, 20)

    print(f"Professional Excel generated successfully at: {output_xlsx}")

if __name__ == "__main__":
    generate_professional_excel()
