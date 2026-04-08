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

-- QUESTION 2: Top 10 Most Valuable Customers (By Revenue)
-- Requirement: Find top 10 most valuable customers for a given year (2021).
SELECT 
    u.first_name || ' ' || u.last_name as customer_name,
    COUNT(s.oid) as total_visits,
    SUM(s.amount) as total_spend,
    RANK() OVER (ORDER BY SUM(s.amount) DESC) as value_rank
FROM clinic_sales s
JOIN users u ON s.uid = u.user_id
WHERE EXTRACT(YEAR FROM s.consultation_date) = 2021
GROUP BY 1
LIMIT 10;

-- QUESTION 3: Monthly P&L and Profitability Status
-- Requirement: Find month wise revenue, expense, profit, status (profitable / not-profitable) for a given year (2021).
WITH monthly_rev AS (
    SELECT DATE_TRUNC('month', consultation_date) as month, SUM(amount) as rev
    FROM clinic_sales WHERE EXTRACT(YEAR FROM consultation_date) = 2021 GROUP BY 1
),
monthly_exp AS (
    SELECT DATE_TRUNC('month', expense_date) as month, SUM(amount) as exp
    FROM expenses WHERE EXTRACT(YEAR FROM expense_date) = 2021 GROUP BY 1
)
SELECT 
    TO_CHAR(COALESCE(r.month, e.month), 'YYYY-MM') as month,
    COALESCE(r.rev, 0) as total_revenue,
    COALESCE(e.exp, 0) as total_expenses,
    COALESCE(r.rev, 0) - COALESCE(e.exp, 0) as net_profit,
    CASE 
        WHEN (COALESCE(r.rev, 0) - COALESCE(e.exp, 0)) > 0 THEN 'Profitable'
        ELSE 'Not-Profitable'
    END as status
FROM monthly_rev r
FULL OUTER JOIN monthly_exp e ON r.month = e.month
ORDER BY 1;

-- QUESTION 4: Most Profitable Clinic per City
-- Requirement: For each city find the most profitable clinic for a given month.
WITH clinic_profit AS (
    SELECT 
        c.city,
        c.clinic_name,
        SUM(s.amount) - COALESCE((SELECT SUM(amount) FROM expenses e WHERE e.cid = c.clinic_id), 0) as profit
    FROM clinics c
    JOIN clinic_sales s ON c.clinic_id = s.cid
    GROUP BY 1, 2, c.clinic_id
)
SELECT city, clinic_name, profit
FROM (
    SELECT city, clinic_name, profit,
    RANK() OVER (PARTITION BY city ORDER BY profit DESC) as city_rank
    FROM clinic_profit
) ranked
WHERE city_rank = 1;

-- QUESTION 5: Second Least Profitable Clinic per State
-- Requirement: For each state find the second least profitable clinic for a given month.
WITH state_profit AS (
    SELECT 
        c.state,
        c.clinic_name,
        SUM(s.amount) - COALESCE((SELECT SUM(amount) FROM expenses e WHERE e.cid = c.clinic_id), 0) as profit
    FROM clinics c
    JOIN clinic_sales s ON c.clinic_id = s.cid
    GROUP BY 1, 2, c.clinic_id
)
SELECT state, clinic_name, profit
FROM (
    SELECT state, clinic_name, profit,
    RANK() OVER (PARTITION BY state ORDER BY profit ASC) as state_rank
    FROM state_profit
) ranked
WHERE state_rank = 2;
