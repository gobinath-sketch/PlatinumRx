# Google Sheets Analysis Guide - Ticket and Feedback System

## Setup Instructions

### 1. Create Google Sheets File
1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet named "Ticket Analysis"
3. Create two sheets: "ticket" and "feedbacks"

### 2. Import Data
- **ticket sheet**: Import `Ticket_Analysis_Data.csv`
- **feedbacks sheet**: Import `Feedbacks_Data.csv`

## Question 1: VLOOKUP to Populate Ticket Created Date

### Goal
Bring the `created_at` date from the `ticket` sheet into the `feedbacks` sheet using `cms_id` as the key.

### Solution Steps

#### Method 1: VLOOKUP Formula
In the `feedbacks` sheet, add a new column called "Ticket_Created_Date" (Column H):

```excel
=VLOOKUP(B2, ticket!A:F, 3, FALSE)
```

**Formula Breakdown:**
- `B2`: The `cms_id` in the current row
- `ticket!A:F`: The lookup range in the ticket sheet (columns A to F)
- `3`: The column number containing `created_at` (3rd column in the range)
- `FALSE`: Exact match requirement

#### Method 2: INDEX-MATCH (More Flexible)
```excel
=INDEX(ticket!C:C, MATCH(B2, ticket!A:A, 0))
```

**Formula Breakdown:**
- `INDEX(ticket!C:C)`: Returns value from Column C (created_at)
- `MATCH(B2, ticket!A:A, 0)`: Finds the row number where cms_id matches

#### Method 3: QUERY Function (Google Sheets Specific)
```excel
=QUERY(ticket!A:F, "SELECT C WHERE A = " & B2, 0)
```

### Apply to All Rows
1. Enter the formula in cell H2
2. Drag the fill handle down to apply to all rows
3. Format the column as Date/Time

## Question 2: Time Analysis - Same Day and Same Hour Resolution

### Goal
Count tickets created and closed on the same day and same hour for each outlet.

### Solution Steps

#### Step 1: Add Helper Columns to ticket Sheet

**Column I: Same_Day_Flag**
```excel
=IF(INT(A2)=INT(D2), "Yes", "No")
```

**Formula Explanation:**
- `INT(A2)`: Extracts date part from created_at
- `INT(D2)`: Extracts date part from closed_at
- Compares dates to determine if same day

**Column J: Same_Hour_Flag**
```excel
=IF(AND(INT(A2)=INT(D2), HOUR(A2)=HOUR(D2)), "Yes", "No")
```

**Formula Explanation:**
- `HOUR(A2)`: Extracts hour from created_at
- `HOUR(D2)`: Extracts hour from closed_at
- Checks both same day AND same hour

#### Step 2: Create Analysis Dashboard

**Create a new sheet called "Dashboard"**

**Same Day Resolution Analysis:**
```excel
=QUERY(ticket!A:J, 
"SELECT B, COUNT(A), SUM(CASE WHEN I = 'Yes' THEN 1 ELSE 0 END) 
WHERE B IS NOT NULL 
GROUP BY B 
LABEL B 'Outlet', COUNT(A) 'Total Tickets', SUM(CASE WHEN I = 'Yes' THEN 1 ELSE 0 END) 'Same Day Resolved'", 0)
```

**Same Hour Resolution Analysis:**
```excel
=QUERY(ticket!A:J, 
"SELECT B, COUNT(A), SUM(CASE WHEN J = 'Yes' THEN 1 ELSE 0 END) 
WHERE B IS NOT NULL 
GROUP BY B 
LABEL B 'Outlet', COUNT(A) 'Total Tickets', SUM(CASE WHEN J = 'Yes' THEN 1 ELSE 0 END) 'Same Hour Resolved'", 0)
```

#### Step 3: Calculate Resolution Rates

**Same Day Resolution Rate:**
```excel
=ARRAYFORMULA(
  IF(B2:B="", "", 
    C2:C / D2:D
  )
)
```

**Same Hour Resolution Rate:**
```excel
=ARRAYFORMULA(
  IF(B2:B="", "", 
    E2:E / D2:D
  )
)
```

#### Step 4: Visual Dashboard with Charts

**Create the following charts:**

1. **Bar Chart**: Total Tickets by Outlet
2. **Stacked Bar Chart**: Same Day vs Different Day Resolution
3. **Pie Chart**: Resolution Rate Distribution
4. **Line Chart**: Resolution Trends Over Time

### Advanced Analysis Formulas

**Average Resolution Time by Outlet:**
```excel
=QUERY(ticket!A:J, 
"SELECT B, 
 AVG(D2-A2) as Avg_Resolution_Time,
 COUNT(A) as Total_Tickets
WHERE B IS NOT NULL 
GROUP BY B 
ORDER BY Avg_Resolution_Time ASC", 0)
```

**Peak Hours Analysis:**
```excel
=QUERY(ticket!A:J, 
"SELECT HOUR(A2) as Hour, 
 COUNT(A) as Tickets_Created,
 SUM(CASE WHEN I = 'Yes' THEN 1 ELSE 0 END) as Same_Day_Resolved
GROUP BY HOUR(A2) 
ORDER BY Hour", 0)
```

**Performance Metrics Dashboard:**
```excel
=LET(
  total_tickets, COUNTA(ticket!A:A),
  same_day_resolved, COUNTIF(ticket!I:I, "Yes"),
  same_hour_resolved, COUNTIF(ticket!J:J, "Yes"),
  
  "Total Tickets: " & total_tickets & "
" & 
  "Same Day Resolution: " & TEXT(same_day_resolved/total_tickets, "0.0%") & "
" &
  "Same Hour Resolution: " & TEXT(same_hour_resolved/total_tickets, "0.0%")
)
```

## Additional Analysis Options

### 1. Pivot Table Analysis
1. Select all data in ticket sheet
2. Insert → Pivot Table
3. Rows: outlet_name
4. Values: COUNT of cms_id, SUM of Same_Day_Flag, SUM of Same_Hour_Flag

### 2. Conditional Formatting
- Highlight "Yes" in green for same day resolution
- Highlight "No" in red for delayed resolution
- Color scale based on resolution time

### 3. Data Validation
- Create dropdown for outlet selection
- Dynamic filtering based on date ranges

## Final Dashboard Layout

### Sheet 1: ticket
- Original data with helper columns
- Conditional formatting applied

### Sheet 2: feedbacks
- Original data with VLOOKUP results
- Customer satisfaction analysis

### Sheet 3: Dashboard
- Summary statistics
- Charts and visualizations
- Performance metrics

### Sheet 4: Analysis
- Detailed breakdowns
- Trend analysis
- Comparative metrics

## Tips for Professional Presentation

1. **Use consistent formatting** throughout all sheets
2. **Add data validation** to prevent errors
3. **Include headers and descriptions** for clarity
4. **Use named ranges** for easier formula management
5. **Protect cells** with formulas to prevent accidental changes
6. **Add documentation** in a separate sheet for formula explanations

## Export Options

- **PDF**: For professional reports
- **Excel**: For compatibility with other systems
- **CSV**: For data import into other tools
- **Web**: For sharing interactive dashboards
