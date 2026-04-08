-- =====================================================
-- PLATINUMRX DATA ANALYST ASSIGNMENT - CLINIC MANAGEMENT SYSTEM
-- Professional Database Schema and High-Quality Seed Data
-- =====================================================

-- Drop existing tables for a clean, idempotent setup
DROP TABLE IF EXISTS expenses CASCADE;
DROP TABLE IF EXISTS clinic_sales CASCADE;

-- =====================================================
-- SCHEMA DEFINITIONS (Optimized for PostgreSQL/Supabase)
-- =====================================================

-- Clinic_Sales: Patient consultation and procedure revenue tracking
CREATE TABLE clinic_sales (
    sale_id SERIAL PRIMARY KEY,
    patient_id VARCHAR(20) NOT NULL,
    patient_name VARCHAR(100) NOT NULL,
    service_type VARCHAR(50) NOT NULL,
    doctor_name VARCHAR(100) NOT NULL,
    sales_channel VARCHAR(30) NOT NULL CHECK (sales_channel IN ('Walk-in', 'Online Booking', 'Phone Appointment', 'Referral')),
    amount DECIMAL(12,2) NOT NULL CHECK (amount >= 0),
    consultation_date DATE NOT NULL,
    payment_status VARCHAR(20) DEFAULT 'Paid' CHECK (payment_status IN ('Paid', 'Pending', 'Partially Paid', 'Cancelled')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Expenses: Clinic operational, administrative, and clinical costs
CREATE TABLE expenses (
    expense_id SERIAL PRIMARY KEY,
    expense_category VARCHAR(50) NOT NULL,
    expense_description VARCHAR(200) NOT NULL,
    amount DECIMAL(12,2) NOT NULL CHECK (amount >= 0),
    expense_date DATE NOT NULL,
    vendor_name VARCHAR(100),
    payment_method VARCHAR(30) DEFAULT 'Bank Transfer',
    approved_by VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- PROFESSIONAL SEED DATA (Exactly 20 Records per Table)
-- =====================================================

-- 1. Clinic Sales (20 Consultations)
INSERT INTO clinic_sales (patient_id, patient_name, service_type, doctor_name, sales_channel, amount, consultation_date, payment_status) VALUES
('P001', 'John Smith', 'General Consultation', 'Dr. Emily Johnson', 'Walk-in', 150.00, '2024-01-05', 'Paid'),
('P002', 'Mary Johnson', 'Specialist Consultation', 'Dr. Michael Chen', 'Online Booking', 250.00, '2024-01-06', 'Paid'),
('P003', 'Robert Davis', 'General Consultation', 'Dr. Sarah Williams', 'Phone Appointment', 150.00, '2024-01-08', 'Paid'),
('P004', 'Lisa Anderson', 'Dental Checkup', 'Dr. James Wilson', 'Walk-in', 200.00, '2024-01-10', 'Paid'),
('P005', 'William Brown', 'Specialist Consultation', 'Dr. Emily Johnson', 'Online Booking', 250.00, '2024-01-12', 'Paid'),
('P006', 'Patricia Miller', 'General Consultation', 'Dr. Michael Chen', 'Walk-in', 150.00, '2024-01-15', 'Paid'),
('P007', 'David Wilson', 'Pediatric Consultation', 'Dr. Sarah Williams', 'Phone Appointment', 180.00, '2024-01-18', 'Paid'),
('P008', 'Jennifer Moore', 'Dental Checkup', 'Dr. James Wilson', 'Online Booking', 200.00, '2024-01-20', 'Paid'),
('P009', 'Chris Taylor', 'Specialist Consultation', 'Dr. Emily Johnson', 'Walk-in', 250.00, '2024-01-22', 'Paid'),
('P010', 'Nancy Thomas', 'General Consultation', 'Dr. Michael Chen', 'Phone Appointment', 150.00, '2024-01-25', 'Paid'),
('P011', 'Daniel Jackson', 'Pediatric Consultation', 'Dr. Sarah Williams', 'Online Booking', 180.00, '2024-02-01', 'Paid'),
('P012', 'Betty White', 'Dental Checkup', 'Dr. James Wilson', 'Walk-in', 200.00, '2024-02-03', 'Paid'),
('P013', 'Paul Harris', 'Specialist Consultation', 'Dr. Emily Johnson', 'Phone Appointment', 250.00, '2024-02-05', 'Paid'),
('P014', 'Karen Martin', 'General Consultation', 'Dr. Michael Chen', 'Online Booking', 150.00, '2024-02-08', 'Paid'),
('P015', 'Steven Thompson', 'Pediatric Consultation', 'Dr. Sarah Williams', 'Walk-in', 180.00, '2024-02-10', 'Paid'),
('P016', 'Helen Garcia', 'Dental Checkup', 'Dr. James Wilson', 'Phone Appointment', 200.00, '2024-02-12', 'Paid'),
('P017', 'Thomas Martinez', 'Specialist Consultation', 'Dr. Emily Johnson', 'Online Booking', 250.00, '2024-02-15', 'Paid'),
('P018', 'Sandra Robinson', 'General Consultation', 'Dr. Michael Chen', 'Walk-in', 150.00, '2024-02-18', 'Paid'),
('P019', 'Jason Clark', 'Pediatric Consultation', 'Dr. Sarah Williams', 'Phone Appointment', 180.00, '2024-02-20', 'Paid'),
('P020', 'Linda Rodriguez', 'Dental Checkup', 'Dr. James Wilson', 'Online Booking', 200.00, '2024-02-22', 'Paid');

-- 2. Expenses (20 Operational Expenses)
INSERT INTO expenses (expense_category, expense_description, amount, expense_date, vendor_name, payment_method, approved_by) VALUES
('Staff Costs', 'Monthly Doctor Salaries - Jan', 12000.00, '2024-01-31', 'Direct Deposit', 'Bank Transfer', 'Admin'),
('Facility', 'Clinic Rent - Jan', 3500.00, '2024-01-31', 'Property Mgmt', 'Bank Transfer', 'Admin'),
('Utilities', 'Electricity and Water - Jan', 450.00, '2024-01-31', 'Utility Co', 'Bank Transfer', 'Admin'),
('Supplies', 'Surgical Gloves and Masks', 850.00, '2024-01-15', 'MedSupplies Inc', 'Credit Card', 'Dr. Chen'),
('Maintenance', 'Dental Chair Service', 1200.00, '2024-01-20', 'TechFix', 'Bank Transfer', 'Dr. Wilson'),
('Admin', 'Medical Software Subscription', 300.00, '2024-01-05', 'SaaS Corp', 'Credit Card', 'Admin'),
('Marketing', 'Local Health Awareness Ads', 800.00, '2024-01-25', 'Local Media', 'Credit Card', 'Admin'),
('Supplies', 'Vaccination Vials Batch A', 2200.00, '2024-02-15', 'PharmaDist', 'Bank Transfer', 'Dr. Johnson'),
('Staff Costs', 'Nurse Salaries - Jan', 8000.00, '2024-01-31', 'Direct Deposit', 'Bank Transfer', 'Admin'),
('Admin', 'Professional Indemnity Insurance', 2500.00, '2024-01-10', 'HealthGuard', 'Bank Transfer', 'Admin'),
('Supplies', 'Disposable Syringes', 250.00, '2024-02-10', 'MedSupplies Inc', 'Credit Card', 'Admin'),
('Facility', 'Clinic Rent - Feb', 3500.00, '2024-02-29', 'Property Mgmt', 'Bank Transfer', 'Admin'),
('Staff Costs', 'Monthly Doctor Salaries - Feb', 12000.00, '2024-02-29', 'Direct Deposit', 'Bank Transfer', 'Admin'),
('Utilities', 'Electricity and Water - Feb', 480.00, '2024-02-29', 'Utility Co', 'Bank Transfer', 'Admin'),
('Admin', 'Office Stationery and Forms', 180.00, '2024-02-25', 'OfficeDepot', 'Bank Transfer', 'Admin'),
('Maintenance', 'AC Unit Repair', 350.00, '2024-02-22', 'Cooling Experts', 'Credit Card', 'Admin'),
('Training', 'Basic Life Support Workshop', 1200.00, '2024-02-08', 'Red Cross', 'Bank Transfer', 'HR'),
('Legal', 'Contract Review Services', 750.00, '2024-02-20', 'Legal Partners', 'Bank Transfer', 'Admin'),
('Security', 'Monthly Security Patrol', 600.00, '2024-02-28', 'SecureGroup', 'Bank Transfer', 'Admin'),
('Admin', 'Bank Service Charges - Feb', 120.00, '2024-02-28', 'Global Bank', 'Direct Debit', 'Admin');

-- =====================================================
-- PERFORMANCE OPTIMIZATION (Indexing)
-- =====================================================
CREATE INDEX idx_clinic_sales_service ON clinic_sales(service_type);
CREATE INDEX idx_clinic_sales_consultation ON clinic_sales(consultation_date);
CREATE INDEX idx_expenses_category_date ON expenses(expense_category, expense_date);

-- =====================================================
-- VALIDATION SUMMARY
-- =====================================================
SELECT 
    'Verification' as phase,
    (SELECT COUNT(*) FROM clinic_sales) as sales_count,
    (SELECT COUNT(*) FROM expenses) as expenses_count,
    (SELECT SUM(amount) FROM clinic_sales) as total_revenue,
    (SELECT SUM(amount) FROM expenses) as total_spend;
