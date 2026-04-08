-- =====================================================
-- PLATINUMRX DATA ANALYST ASSIGNMENT - CLINIC MANAGEMENT SYSTEM
-- Advanced Analytical SQL Solutions (Phase 1)
-- =====================================================

-- QUESTION 1: Revenue by Sales Channel
-- Business Goal: Optimize CAC (Customer Acquisition Cost) by identifying top channels.
SELECT 
    sales_channel,
    COUNT(*) as volume,
    SUM(amount) as revenue,
    ROUND(SUM(amount) * 100.0 / (SELECT SUM(amount) FROM clinic_sales), 2) as revenue_share_pct
FROM clinic_sales
GROUP BY 1
ORDER BY revenue DESC;

-- QUESTION 2: Top Performing Doctors by Revenue
-- Business Goal: Workforce optimization and incentive planning.
SELECT 
    doctor_name,
    COUNT(*) as patient_load,
    SUM(amount) as revenue_generated,
    ROUND(AVG(amount), 2) as avg_consult_value,
    DENSE_RANK() OVER (ORDER BY SUM(amount) DESC) as performance_rank
FROM clinic_sales
GROUP BY 1;

-- QUESTION 3: Monthly Profit and Loss (P&L) Analysis
-- Business Goal: Core financial health tracking.
WITH monthly_rev AS (
    SELECT DATE_TRUNC('month', consultation_date) as month, SUM(amount) as rev
    FROM clinic_sales GROUP BY 1
),
monthly_exp AS (
    SELECT DATE_TRUNC('month', expense_date) as month, SUM(amount) as exp
    FROM expenses GROUP BY 1
)
SELECT 
    TO_CHAR(COALESCE(r.month, e.month), 'YYYY-MM') as month,
    COALESCE(r.rev, 0) as total_revenue,
    COALESCE(e.exp, 0) as total_expenses,
    COALESCE(r.rev, 0) - COALESCE(e.exp, 0) as net_profit,
    ROUND((COALESCE(r.rev, 0) - COALESCE(e.exp, 0)) * 100.0 / NULLIF(r.rev, 0), 2) as profit_margin_pct
FROM monthly_rev r
FULL OUTER JOIN monthly_exp e ON r.month = e.month
ORDER BY 1;

-- QUESTION 4: Service Type Performance
-- Business Goal: Strategic service-line expansion analysis.
SELECT 
    service_type,
    COUNT(*) as volume,
    SUM(amount) as revenue,
    ROUND(AVG(amount), 2) as unit_price,
    RANK() OVER (ORDER BY SUM(amount) DESC) as revenue_rank
FROM clinic_sales
GROUP BY 1;

-- QUESTION 5: Patient Volume Trends (Peak Days/Hours)
-- Business Goal: Operational scheduling and staff shift optimization.
SELECT 
    TO_CHAR(consultation_date, 'Day') as day_of_week,
    COUNT(*) as visit_volume,
    SUM(amount) as daily_revenue
FROM clinic_sales
GROUP BY 1, EXTRACT(DOW FROM consultation_date)
ORDER BY EXTRACT(DOW FROM consultation_date);

-- =====================================================
-- HIGH-END ANALYTICAL BONUS: Expense Breakdown by Category
-- =====================================================
SELECT 
    expense_category,
    SUM(amount) as category_total,
    ROUND(SUM(amount) * 100.0 / (SELECT SUM(amount) FROM expenses), 2) as expense_share_pct
FROM expenses
GROUP BY 1
ORDER BY category_total DESC;
