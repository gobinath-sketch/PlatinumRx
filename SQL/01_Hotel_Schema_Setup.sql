-- =====================================================
-- PLATINUMRX DATA ANALYST ASSIGNMENT - HOTEL MANAGEMENT SYSTEM
-- Professional Database Schema and High-Quality Seed Data
-- =====================================================

-- Drop existing tables for a clean, idempotent setup
DROP TABLE IF EXISTS booking_commercials CASCADE;
DROP TABLE IF EXISTS bookings CASCADE;
DROP TABLE IF EXISTS items CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- =====================================================
-- SCHEMA DEFINITIONS (Optimized for PostgreSQL/Supabase)
-- =====================================================

-- Users: Core guest profile storage
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    membership_level VARCHAR(20) DEFAULT 'Standard' CHECK (membership_level IN ('Standard', 'Silver', 'Gold', 'Platinum')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Items: Catalog of hotel services, room types, and amenities
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    rate DECIMAL(12,2) NOT NULL CHECK (rate >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Bookings: Master reservation records
CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    room_number VARCHAR(10) NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    total_amount DECIMAL(12,2) NOT NULL DEFAULT 0,
    status VARCHAR(20) DEFAULT 'Confirmed' CHECK (status IN ('Pending', 'Confirmed', 'Completed', 'Cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (check_out_date >= check_in_date)
);

-- Booking_Commercials: Granular transactional records for each booking (Room charges + Extras)
CREATE TABLE booking_commercials (
    commercial_id SERIAL PRIMARY KEY,
    booking_id INTEGER REFERENCES bookings(booking_id) ON DELETE CASCADE,
    item_id INTEGER REFERENCES items(item_id) ON DELETE SET NULL,
    quantity INTEGER NOT NULL DEFAULT 1 CHECK (quantity > 0),
    rate DECIMAL(12,2) NOT NULL CHECK (rate >= 0),
    total_amount DECIMAL(12,2) GENERATED ALWAYS AS (quantity * rate) STORED,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- PROFESSIONAL SEED DATA (Exactly 20 Records per Core Entity)
-- =====================================================

-- 1. Users (20 Guests)
INSERT INTO users (first_name, last_name, email, phone, membership_level) VALUES
('James', 'Anderson', 'james.a@example.com', '555-0101', 'Platinum'),
('Sarah', 'Williams', 'sarah.w@example.com', '555-0102', 'Gold'),
('Michael', 'Brown', 'michael.b@example.com', '555-0103', 'Silver'),
('Emma', 'Davis', 'emma.d@example.com', '555-0104', 'Gold'),
('Robert', 'Miller', 'robert.m@example.com', '555-0105', 'Standard'),
('Lisa', 'Wilson', 'lisa.w@example.com', '555-0106', 'Platinum'),
('David', 'Moore', 'david.m@example.com', '555-0107', 'Silver'),
('Jennifer', 'Taylor', 'jennifer.t@example.com', '555-0108', 'Gold'),
('William', 'Anderson', 'william.a@example.com', '555-0109', 'Standard'),
('Maria', 'Thomas', 'maria.t@example.com', '555-0110', 'Silver'),
('Chris', 'Jackson', 'chris.j@example.com', '555-0111', 'Gold'),
('Patricia', 'White', 'patricia.w@example.com', '555-0112', 'Platinum'),
('Daniel', 'Harris', 'daniel.h@example.com', '555-0113', 'Standard'),
('Nancy', 'Martin', 'nancy.m@example.com', '555-0114', 'Silver'),
('Thomas', 'Thompson', 'thomas.t@example.com', '555-0115', 'Gold'),
('Betty', 'Garcia', 'betty.g@example.com', '555-0116', 'Standard'),
('Paul', 'Martinez', 'paul.m@example.com', '555-0117', 'Platinum'),
('Karen', 'Robinson', 'karen.r@example.com', '555-0118', 'Silver'),
('Steven', 'Clark', 'steven.c@example.com', '555-0119', 'Gold'),
('Helen', 'Rodriguez', 'helen.r@example.com', '555-0120', 'Standard');

-- 2. Items (20 Service Catalog Entries)
INSERT INTO items (item_name, category, rate) VALUES
('Deluxe King Room', 'Accommodation', 250.00),
('Junior Suite', 'Accommodation', 450.00),
('Standard Twin Room', 'Accommodation', 150.00),
('Executive Suite', 'Accommodation', 350.00),
('Presidential Suite', 'Accommodation', 800.00),
('Continental Breakfast', 'Dining', 25.00),
('Room Service Dinner', 'Dining', 45.00),
('Full Spa Package', 'Wellness', 120.00),
('Gym Day Pass', 'Wellness', 20.00),
('VIP Airport Transfer', 'Transport', 75.00),
('Guided City Tour', 'Tourism', 85.00),
('Premium Laundry', 'Service', 35.00),
('Business Center Duo', 'Service', 50.00),
('Board Room (4h)', 'Service', 200.00),
('High-Speed Wi-Fi', 'Utility', 15.00),
('Mini-Bar Re-stock', 'Dining', 60.00),
('Express Checkout', 'Service', 40.00),
('Pet Stay Cleaning', 'Service', 55.00),
('Kids Activity Club', 'Entertainment', 30.00),
('Private Beach Cabana', 'Recreation', 100.00);

-- 3. Bookings (20 Reservations across different time periods)
INSERT INTO bookings (user_id, room_number, check_in_date, check_out_date, total_amount, status) VALUES
(1, '101', '2021-11-01', '2021-11-05', 1000.00, 'Completed'),
(2, '202', '2021-11-10', '2021-11-12', 450.00, 'Completed'),
(3, '305', '2021-11-15', '2021-11-18', 450.00, 'Completed'),
(4, '401', '2021-12-01', '2021-12-10', 3500.00, 'Completed'),
(5, '102', '2022-01-05', '2022-01-07', 300.00, 'Completed'),
(6, '501', '2022-02-14', '2022-02-16', 1600.00, 'Completed'),
(7, '203', '2022-03-20', '2022-03-25', 750.00, 'Completed'),
(8, '404', '2022-04-10', '2022-04-15', 1750.00, 'Completed'),
(9, '105', '2022-05-01', '2022-05-03', 300.00, 'Completed'),
(10, '302', '2022-06-12', '2022-06-15', 540.00, 'Completed'),
(11, '201', '2022-07-04', '2022-07-10', 2100.00, 'Completed'),
(12, '502', '2022-08-20', '2022-08-22', 1600.00, 'Completed'),
(13, '108', '2022-09-15', '2022-09-18', 450.00, 'Completed'),
(14, '402', '2022-10-31', '2022-11-03', 1050.00, 'Completed'),
(15, '303', '2022-11-15', '2022-11-17', 900.00, 'Completed'),
(16, '107', '2022-12-24', '2022-12-28', 600.00, 'Completed'),
(17, '205', '2023-01-10', '2023-01-15', 1250.00, 'Completed'),
(18, '406', '2023-02-20', '2023-02-23', 1050.00, 'Completed'),
(19, '308', '2023-03-15', '2023-03-18', 450.00, 'Completed'),
(20, '104', '2024-04-01', '2024-04-05', 600.00, 'Confirmed');

-- 4. Booking Commercials (At least one per booking, showing high-end analytical data)
INSERT INTO booking_commercials (booking_id, item_id, quantity, rate) VALUES
(1, 1, 4, 250.00), (1, 6, 2, 25.00), (1, 10, 1, 75.00),
(2, 2, 2, 225.00), (2, 7, 1, 45.00),
(3, 3, 3, 150.00),
(4, 4, 9, 350.00), (4, 15, 1, 15.00), (4, 20, 2, 100.00),
(5, 3, 2, 150.00),
(6, 5, 2, 800.00), (6, 8, 1, 120.00),
(7, 3, 5, 150.00),
(8, 4, 5, 350.00), (8, 9, 2, 20.00),
(9, 3, 2, 150.00),
(10, 7, 3, 180.00),
(11, 4, 6, 350.00),
(12, 5, 2, 800.00),
(13, 3, 3, 150.00),
(14, 4, 3, 350.00),
(15, 2, 2, 450.00),
(16, 3, 4, 150.00),
(17, 1, 5, 250.00),
(18, 4, 3, 350.00),
(19, 3, 3, 150.00),
(20, 3, 4, 150.00);

-- =====================================================
-- PERFORMANCE OPTIMIZATION (Indexing)
-- =====================================================
CREATE INDEX idx_users_membership ON users(membership_level);
CREATE INDEX idx_bookings_date_range ON bookings(check_in_date, check_out_date);
CREATE INDEX idx_commercials_composite ON booking_commercials(booking_id, item_id);

-- =====================================================
-- VALIDATION SUMMARY
-- =====================================================
SELECT 
    'Verification' as phase,
    (SELECT COUNT(*) FROM users) as users_count,
    (SELECT COUNT(*) FROM items) as items_count,
    (SELECT COUNT(*) FROM bookings) as bookings_count,
    (SELECT COUNT(*) FROM booking_commercials) as ledger_count;
