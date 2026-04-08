# 💎 PlatinumRx Data Analyst Portfolio Project

## 🚀 Overview
Welcome to the **PlatinumRx Real-Time Business Intelligence** ecosystem. This project transforms a standard data analyst assignment into a production-grade, real-time system spanning Database Management, Spreadsheet Engineering, and Python Scripting.

> [!IMPORTANT]
> This system is built for **visual excellence** and **real-time performance**. It replaces all mock data with a live connection to a **Supabase (PostgreSQL)** database.

---

## 🛠️ Technical Ecosystem

### 1. 🏨 Hotel Management Intelligence (SQL)
- **Real-Time Schema:** Optimized PostgreSQL schema with 20+ high-quality seed records.
- **Advanced BI:** Complex analytical solutions including:
    - Month-over-Month Revenue Growth
    - Detailed Occupancy & Activity Metrics
    - VIP Guest Identification via Multi-Table Joins
- **Files:** `SQL/01_Hotel_Schema_Setup.sql`, `SQL/02_Hotel_Queries.sql`

### 2. 🏥 Clinic Operations Analytics (SQL)
- **Revenue Tracking:** Granular consultation and procedure logging.
- **Financial Health:** Automated Profit & Loss (P&L) analysis with expense category breakdowns.
- **Files:** `SQL/03_Clinic_Schema_Setup.sql`, `SQL/04_Clinic_Queries.sql`

### 3. 📊 Interactive Real-Time Dashboard (Streamlit)
- **Live BI:** Professional dashboard connecting directly to Supabase.
- **Data Entry:** Real-time forms to insert new bookings and sales directly into the production database.
- **Visualizations:** Immersive Plotly charts representing key business metrics.
- **Run Locally:** `streamlit run real_time_dashboard.py`

### 4. 📈 Spreadsheet Proficiency (Excel Automation)
- **Automated Engineering:** High-end Python script (`generate_excel.py`) that produces the `Ticket_Analysis.xlsx` file.
- **Logic Implemented:**
    - `XLOOKUP` style data mapping.
    - "Same Day" and "Same Hour" resolution logic.
    - Automated BI Dashboard worksheet.

### 5. 🐍 Python Utility Excellence
- **Time Converter:** Converts minutes to human-readable format with robust error handling.
- **Duplicate Remover:** Implements multiple algorithmic approaches for string manipulation.
- **Files:** `Python/01_Time_Converter.py`, `Python/02_Remove_Duplicates.py`

---

## 🚦 Getting Started

### Prerequisites
- Python 3.10+
- Internet connection (for Supabase real-time sync)

### Setup & Installation
1. Install dependencies:
   ```bash
   pip install streamlit pandas plotly psycopg2-binary xlsxwriter
   ```
2. Initialize the Database (Supabase):
   ```bash
   python db_setup.py
   ```
3. Generate the Analysis Excel:
   ```bash
   python generate_excel.py
   ```
4. Launch the Dashboard:
   ```bash
   streamlit run real_time_dashboard.py
   ```

---

## 🔍 Proof of Work
Refer to the [walkthrough.md](file:///C:/Users/gobin/.gemini/antigravity/brain/dd409078-a978-444b-9ffd-63bdf423fbc9/walkthrough.md) for a detailed technical tour and visual confirmation of the real-time capabilities.

---
**Developed with ❤️ and Precision for PlatinumRx.**
