-- =====================================================
-- PLATINUMRX DATA ANALYST ASSIGNMENT - HOTEL MANAGEMENT SYSTEM
-- Advanced Analytical SQL Solutions (Phase 1)
-- =====================================================

-- QUESTION 1: Most Recently Booked Room
-- Business Goal: Real-time operational awareness for front desk preparation.
WITH recent_booking AS (
    SELECT 
        b.booking_id,
        u.first_name || ' ' || u.last_name AS guest_name,
        b.room_number,
        b.check_in_date,
        b.total_amount,
        b.created_at,
        ROW_NUMBER() OVER (ORDER BY b.created_at DESC) as recency_rank
    FROM bookings b
    JOIN users u ON b.user_id = u.user_id
)
SELECT * FROM recent_booking WHERE recency_rank = 1;

-- QUESTION 2: Total Revenue for November 2021
-- Business Goal: Financial reporting for the specific fiscal period.
SELECT 
    UPPER(TO_CHAR(b.check_in_date, 'Month YYYY')) as period,
    COUNT(DISTINCT b.booking_id) as total_reservations,
    SUM(bc.total_amount) as gross_revenue,
    ROUND(AVG(bc.total_amount), 2) as average_transaction_value
FROM bookings b
JOIN booking_commercials bc ON b.booking_id = bc.booking_id
WHERE b.check_in_date >= '2021-11-01' AND b.check_in_date <= '2021-11-30'
GROUP BY 1;

-- QUESTION 3: High-Value Bookings (Sum > $1000)
-- Business Goal: Identify VIP customers for high-touch service and retention.
SELECT 
    b.booking_id,
    u.first_name || ' ' || u.last_name as guest,
    u.membership_level,
    b.room_number,
    SUM(bc.total_amount) as total_bill,
    CASE 
        WHEN SUM(bc.total_amount) > 2000 THEN 'ULTRA-VIP'
        ELSE 'VIP'
    END as classification
FROM bookings b
JOIN users u ON b.user_id = u.user_id
JOIN booking_commercials bc ON b.booking_id = bc.booking_id
GROUP BY b.booking_id, guest, u.membership_level, b.room_number
HAVING SUM(bc.total_amount) > 1000
ORDER BY total_bill DESC;

-- QUESTION 4: Most and Least Ordered Items by Month
-- Business Goal: Inventory optimization and peak-load planning.
WITH monthly_item_metrics AS (
    SELECT 
        TO_CHAR(b.check_in_date, 'YYYY-MM') as month,
        i.item_name,
        SUM(bc.quantity) as vol_ordered,
        RANK() OVER (PARTITION BY TO_CHAR(b.check_in_date, 'YYYY-MM') ORDER BY SUM(bc.quantity) DESC) as top_rank,
        RANK() OVER (PARTITION BY TO_CHAR(b.check_in_date, 'YYYY-MM') ORDER BY SUM(bc.quantity) ASC) as bottom_rank
    FROM bookings b
    JOIN booking_commercials bc ON b.booking_id = bc.booking_id
    JOIN items i ON bc.item_id = i.item_id
    GROUP BY 1, 2
)
SELECT 
    month,
    MAX(CASE WHEN top_rank = 1 THEN item_name END) as most_popular,
    MAX(CASE WHEN bottom_rank = 1 THEN item_name END) as least_popular,
    MAX(CASE WHEN top_rank = 1 THEN vol_ordered END) as max_volume
FROM monthly_item_metrics
WHERE top_rank = 1 OR bottom_rank = 1
GROUP BY month
ORDER BY month;

-- QUESTION 5: Second Highest Booking Bill
-- Business Goal: Competitive benchmarking and outlier detection.
SELECT * FROM (
    SELECT 
        booking_id,
        total_amount,
        DENSE_RANK() OVER (ORDER BY total_amount DESC) as bill_rank
    FROM bookings
) ranked_bills
WHERE bill_rank = 2;

-- =====================================================
-- HIGH-END ANALYTICAL BONUS: Month-over-Month Revenue Growth
-- =====================================================
WITH monthly_rev AS (
    SELECT 
        DATE_TRUNC('month', check_in_date) as month,
        SUM(total_amount) as revenue
    FROM bookings
    GROUP BY 1
)
SELECT 
    TO_CHAR(month, 'YYYY-MM') as month,
    revenue as current_month_revenue,
    LAG(revenue) OVER (ORDER BY month) as prev_month_revenue,
    ROUND(((revenue - LAG(revenue) OVER (ORDER BY month)) / NULLIF(LAG(revenue) OVER (ORDER BY month), 0)) * 100, 2) as pct_growth
FROM monthly_rev;
