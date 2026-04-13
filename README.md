<div align="center">

# PlatinumRx — Real-Time Business Intelligence Ecosystem

### A Production-Grade Data Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://supabase.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live_Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![Excel](https://img.shields.io/badge/Excel-Automated-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://microsoft.com/excel)

> **Live-connected, visually immersive, zero-hardcoded-data BI platform spanning SQL, Python, Spreadsheet Engineering, and Real-Time Dashboarding.**

</div>

---
live stramlit ui pushed link access thorugh here -->>     https://platinumrx-qb5sa7hbadxtim78y6kpwg.streamlit.app

##  Table of Contents

- [ Project Overview](#-project-overview)
- [ System Architecture](#️-system-architecture)
- [ Quick Start](#-quick-start)
- [ Database Module (SQL)](#️-database-module-sql)
  - [ Hotel Management System](#-hotel-management-system)
  - [ Clinic Management System](#-clinic-management-system)
- [ Real-Time BI Dashboard](#-real-time-bi-dashboard)
- [ Spreadsheet Automation (Excel)](#-spreadsheet-automation-excel)
- [ Python Utility Scripts](#-python-utility-scripts)
- [ System Audit & Testing](#-system-audit--testing)
- [ Project Structure](#-project-structure)
- [ Visual Proof](#️-visual-proof)
- [ Security](#-security)

---

##  Project Overview

**PlatinumRx** is a full-spectrum data analytics portfolio project. It transforms a standard business analyst assignment into a **production-ready, enterprise-grade BI ecosystem** with the following capabilities:

| Capability | Technology | Status |
|---|---|---|
| Live Database Backend | Supabase (PostgreSQL) |  Connected |
| Advanced SQL Analytics | 10 Analytical Queries (Part A + B) |  Implemented |
| Real-Time BI Dashboard | Streamlit + Plotly |  Live |
| Spreadsheet Automation | Python → Excel (openpyxl/xlsxwriter) |  Automated |
| Python Utility Scripting | Custom OOP Classes |  Verified |
| Live Data Entry | Real-time DB INSERT via Dashboard |  Functional |
| End-to-End Audit | Automated Test Suite |  Passing |

---

##  System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     PlatinumRx Ecosystem                    │
└───────────────────────────┬─────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐  ┌────────────────┐  ┌────────────────────┐
│  SQL Layer    │  │  Python Layer  │  │  Streamlit Layer   │
│               │  │                │  │                    │
│ Hotel Schema  │  │ 01_Time_Conv.  │  │  Hotel Analytics   │
│ Clinic Schema │  │ 02_Remove_Dup. │  │  Clinic Analytics  │
│ 10 SQL Queries│  │ generate_excel │  │  Data Entry Forms  │
└───────┬───────┘  └────────┬───────┘  └─────────┬──────────┘
        │                   │                     │
        └───────────────────▼─────────────────────┘
                            │
                ┌───────────▼───────────┐
                │   Supabase (PostgreSQL)│
                │   Live Database Backend│
                └───────────────────────┘
```

---

##  Quick Start

### Prerequisites

- Python 3.13+
- Internet connection (for Supabase live sync)

### Installation

```bash
# Step 1: Clone the repository
git clone https://github.com/gobinath-sketch/PlatinumRx.git
cd PlatinumRx

# Step 2: Install all dependencies
py -m pip install streamlit pandas plotly psycopg2-binary openpyxl xlsxwriter python-dotenv

# Step 3: Initialize Database (Seeds all tables with professional data)
py db_setup.py

# Step 4: Generate Excel Spreadsheet
py generate_excel.py

# Step 5: Launch the Live Dashboard
streamlit run real_time_dashboard.py
```

> **Dashboard available at:** `http://localhost:8501`

---

##  Database Module (SQL)

The database layer consists of two fully independent management systems deployed on Supabase (PostgreSQL).

---

###  Hotel Management System

**Schema Files:** `SQL/01_Hotel_Schema_Setup.sql`

#### Table Schema

```
┌──────────────────────────────────────────────────────────┐
│                   HOTEL DATABASE SCHEMA                  │
├─────────────────────┬────────────────────────────────────┤
│       Table         │           Columns                  │
├─────────────────────┼────────────────────────────────────┤
│ users               │ user_id, first_name, last_name,    │
│                     │ email, phone, membership_level,    │
│                     │ created_at                         │
├─────────────────────┼────────────────────────────────────┤
│ items               │ item_id, item_name, category,      │
│                     │ rate, is_active, created_at        │
├─────────────────────┼────────────────────────────────────┤
│ bookings            │ booking_id, user_id, room_number,  │
│  (FK: users)        │ check_in_date, check_out_date,     │
│                     │ total_amount, status, created_at   │
├─────────────────────┼────────────────────────────────────┤
│ booking_commercials │ commercial_id, booking_id,         │
│  (FK: bookings,     │ item_id, quantity, rate,           │
│       items)        │ total_amount (GENERATED), created_at│
└─────────────────────┴────────────────────────────────────┘
```

**Seed Data:** 20 Users | 20 Items | 20 Bookings | 25 Commercial Records

####  Hotel Analytics Queries — Part A (`SQL/02_Hotel_Queries.sql`)

| # | Business Question | SQL Technique |
|---|---|---|
| Q1 | Most recently booked room | `ROW_NUMBER()` Window Function |
| Q2 | Total revenue for November 2021 | `DATE` filtering + Multi-table `JOIN` |
| Q3 | High-value bookings (Sum > $1,000) | `HAVING` clause + `CASE` classification |
| Q4 | Most & least ordered items by month | `RANK()` with dual `PARTITION BY` |
| Q5 | Second highest booking bill | `DENSE_RANK()` Window Function |
| **BONUS** | Month-over-Month Revenue Growth | `LAG()` Window Function |

---

###  Clinic Management System

**Schema Files:** `SQL/03_Clinic_Schema_Setup.sql`

#### Table Schema

```
┌──────────────────────────────────────────────────────────┐
│                  CLINIC DATABASE SCHEMA                  │
├─────────────────────┬────────────────────────────────────┤
│       Table         │           Columns                  │
├─────────────────────┼────────────────────────────────────┤
│ clinics             │ clinic_id, clinic_name, city,      │
│                     │ state, address, phone              │
├─────────────────────┼────────────────────────────────────┤
│ doctors             │ doctor_id, first_name, last_name,  │
│  (FK: clinics)      │ specialization, clinic_id          │
├─────────────────────┼────────────────────────────────────┤
│ clinic_sales        │ oid, uid, cid, did, amount,        │
│  (FK: users,        │ consultation_date, sales_channel   │
│   clinics, doctors) │                                    │
├─────────────────────┼────────────────────────────────────┤
│ expenses            │ expense_id, cid, category, amount, │
│  (FK: clinics)      │ expense_date, description          │
└─────────────────────┴────────────────────────────────────┘
```

**Seed Data:** 5 Clinics | 10 Doctors | 25 Sales Records | 15 Expense Records

####  Clinic Analytics Queries — Part B (`SQL/04_Clinic_Queries.sql`)

| # | Business Question | SQL Technique |
|---|---|---|
| Q1 | Revenue by Sales Channel | `GROUP BY` + Revenue share % |
| Q2 | Top 10 Most Valuable Customers (2021) | `RANK()` + `JOIN` + Year filter |
| Q3 | Monthly P&L with Profitability Status | `FULL OUTER JOIN` + `CASE` logic |
| Q4 | Most Profitable Clinic per City | `RANK()` with `PARTITION BY city` |
| Q5 | Second Least Profitable Clinic per State | `RANK()` with `PARTITION BY state` |

---

##  Real-Time BI Dashboard

**File:** `real_time_dashboard.py`

The dashboard is a **4-page Streamlit application** with direct database connectivity.

### Pages & Functionality

```
Sidebar Navigation
├──  Home          — DB connectivity status & system overview
├──  Hotel Analytics — Live KPIs + Item popularity charts (Part A)
├──  Clinic Analytics — Monthly P&L trend lines (Part B)
└──  Data Entry    — Live INSERT forms for Hotel & Clinic data
```

### Data Entry Flow

```
User fills form
      │
      ▼
Input validation (date logic, min values)
      │
      ▼
psycopg2 executes INSERT INTO bookings/clinic_sales
      │
      ▼
Database commits record
      │
      ▼
Success message → Navigate back → Charts refresh with new data
```

### Running the Dashboard

```bash
streamlit run real_time_dashboard.py
# → Dashboard: http://localhost:8501
```

---

##  Spreadsheet Automation (Excel)

**File:** `generate_excel.py`
**Output:** `Spreadsheets/Ticket_Analysis.xlsx`

This script programmatically engineers a professional multi-worksheet Excel report from CSV data.

### Logic Implemented

| Feature | Implementation |
|---|---|
| Data Loading | Reads `Ticket_Analysis_Data.csv` and `Feedbacks_Data.csv` |
| `XLOOKUP` Simulation | Python dictionary mapping for O(1) lookups |
| **Same Day Resolution** | `IF(created_date = resolved_date, "Same Day", "Different Day")` |
| **Same Hour Resolution** | `IF(HOUR(created_time) = HOUR(resolved_time), "Same Hour", "Different Hour")` |
| Auto-Formatting | Column width adjustment, header styling |
| Dashboard Sheet | Summary KPI worksheet auto-generated |

```bash
# Run Excel generation
py generate_excel.py
# → Output: Spreadsheets/Ticket_Analysis.xlsx
```

---

##  Python Utility Scripts

### `Python/01_Time_Converter.py` — TimeConverter Class

Converts raw minutes into a clean, human-readable duration string.

```bash
# Usage Examples
py Python/01_Time_Converter.py convert 130   # → "2 hrs 10 mins"
py Python/01_Time_Converter.py test           # → Run full test suite
py Python/01_Time_Converter.py interactive    # → Interactive mode
```

**Core Algorithm:**
```python
hours   = minutes // 60
mins    = minutes % 60
result  = f"{hours} hrs {mins} mins"
```

---

### `Python/02_Remove_Duplicates.py` — DuplicateRemover Class

Removes duplicate characters from strings using multiple algorithmic approaches.

```bash
# Usage Examples
py Python/02_Remove_Duplicates.py remove programming          # → "progamin"
py Python/02_Remove_Duplicates.py remove 'HelloHELLO' case_insensitive  # → "Hello"
py Python/02_Remove_Duplicates.py test                        # → Run full test suite
py Python/02_Remove_Duplicates.py interactive                 # → Interactive mode
```

**Supported Methods:**
| Method | Description |
|---|---|
| `case_sensitive` | Default — preserves first occurrence, removes duplicates |
| `case_insensitive` | Treats uppercase and lowercase as duplicates |
| `preserve_order` | Maintains original character ordering |

---

##  System Audit & Testing

A dedicated automated audit script validates **all four modules** simultaneously.

```bash
py Test_Files/comprehensive_audit.py
```

### Audit Output

```
============================================================
 PLATINUMRX END-TO-END SYSTEM AUDIT 
============================================================

[1/4] Auditing Database Connectivity...
 Hotel System: Verified. Total Revenue = $19,045.00
 Clinic System: Verified. Total Consultations = 25
 Users Table: Verified. Current Count = 22

[2/4] Auditing Python Utilities...
 Time Converter: Verified. 130 min -> '2 hrs 10 mins'
 Duplicate Remover: Verified. 'programming' -> 'progamin'

[3/4] Auditing Spreadsheet Generation...
 Excel Generation: Verified. Created Spreadsheets/Ticket_Analysis.xlsx

[4/4] Auditing Codebase Integrity...
 SQL Syntax: Audited.
 Real-Time Dashboard Logic: Audited.
 Error Handling: Audited.

============================================================
 AUDIT COMPLETE: ALL SYSTEMS NOMINAL 
============================================================
```

---

##  Project Structure

```
PlatinumRx/
│
├──  README.md                        ← You are here
├──  .env                             ← Credentials (git-ignored)
├──  .gitignore                       ← Security manifest
│
├──  SQL/
│   ├── 01_Hotel_Schema_Setup.sql       ← Hotel tables + 20 seed records
│   ├── 02_Hotel_Queries.sql            ← 5 Hotel analytical queries (Part A)
│   ├── 03_Clinic_Schema_Setup.sql      ← Clinic tables + seed data
│   └── 04_Clinic_Queries.sql           ← 5 Clinic analytical queries (Part B)
│
├──  Python/
│   ├── 01_Time_Converter.py            ← Minutes-to-hours converter class
│   └── 02_Remove_Duplicates.py         ← String duplicate remover class
│
├──  Spreadsheets/
│   ├── Feedbacks_Data.csv              ← Source data (feedback)
│   ├── Ticket_Analysis_Data.csv        ← Source data (tickets)
│   └── Ticket_Analysis.xlsx            ← AUTO-GENERATED professional report
│
├──  Reports/
│   ├── COMPREHENSIVE_TEST_REPORT.md    ← Full test results
│   ├── Google_Sheets_Analysis_Guide.md ← Spreadsheet methodology guide
│   ├── Supabase_Setup_Guide.md         ← DB connection guide
│   └── TEST_REPORT.md                  ← Summary test report
│
├──  images/
│   ├── web_screenshots/                ← Dashboard visual proof
│   │   ├── home.png
│   │   ├── hotel_analytics.png
│   │   ├── clinic.png
│   │   └── data_entry.png
│   └── terminal_screenshots/           ← Audit & script execution proof
│       ├── Screenshot 2026-04-08 211223.png
│       ├── Screenshot 2026-04-08 211247.png
│       └── Screenshot 2026-04-08 211326.png
│
├──  Screen_Records/
│   └── Full_System_Walkthrough.webp    ← End-to-end live demo recording
│
├──  Test_Files/
│   └── comprehensive_audit.py          ← Automated 4-module audit script
│
├──  real_time_dashboard.py           ← Streamlit BI dashboard (main app)
├──   db_setup.py                     ← Database initializer
└──  generate_excel.py                ← Excel automation engine
```

---

##  Visual Proof

All screenshots are stored in the `images/` directory for submission evidence.

| Evidence Type | Location |
|---|---|
| Web Dashboard — Home | `images/web_screenshots/home.png` |
| Web Dashboard — Hotel | `images/web_screenshots/hotel_analytics.png` |
| Web Dashboard — Clinic | `images/web_screenshots/clinic.png` |
| Web Dashboard — Data Entry | `images/web_screenshots/data_entry.png` |
| Terminal — Full System Audit | `images/terminal_screenshots/Screenshot 2026-04-08 211223.png` |
| Terminal — Excel Generation | `images/terminal_screenshots/Screenshot 2026-04-08 211247.png` |
| Terminal — Python Utilities | `images/terminal_screenshots/Screenshot 2026-04-08 211326.png` |
| 🎥 Full System Video | `Screen_Records/Full_System_Walkthrough.webp` |

---

##  Security

| Item | Status |
|---|---|
| Database credentials | Stored in `.env` (never committed) |
| `.gitignore` | Configured to exclude `.env` and cache files |
| Connection pooling | Uses Supabase Transaction Pooler (port 6543) |

---

<div align="center">

PlatinumRx Data Analyst Portfolio — Production-Grade, Real-Time, Zero Compromise.

</div>
