-- First-Case OR Delay Analysis Queries
-- Compatible with Epic, Cerner (adjust table/column names as needed)

-- Query 1: Daily First-Case Delay Summary
-- Purpose: Track average delays by day with breakdown
SELECT 
    DATE(scheduled_start) as surgery_date,
    COUNT(*) as total_first_cases,
    AVG(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as avg_delay_minutes,
    SUM(CASE WHEN TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) <= 5 THEN 1 ELSE 0 END) as on_time_starts,
    SUM(CASE WHEN TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) > 30 THEN 1 ELSE 0 END) as severe_delays,
    ROUND(100.0 * SUM(CASE WHEN TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) <= 5 THEN 1 ELSE 0 END) / COUNT(*), 1) as on_time_rate
FROM or_cases
WHERE 
    case_sequence = 1  -- First case of the day
    AND scheduled_start >= CURRENT_DATE - INTERVAL 30 DAY
    AND case_status = 'COMPLETED'
GROUP BY DATE(scheduled_start)
ORDER BY surgery_date DESC;

-- Query 2: Delay Root Cause Analysis
-- Purpose: Identify primary delay reasons
SELECT 
    delay_reason,
    COUNT(*) as frequency,
    AVG(delay_minutes) as avg_delay_when_occurs,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) as percent_of_delays
FROM (
    SELECT 
        case_id,
        TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) as delay_minutes,
        CASE 
            WHEN equipment_ready_time > scheduled_start THEN 'Equipment Not Ready'
            WHEN staff_ready_time > scheduled_start THEN 'Staff Not Ready'
            WHEN patient_ready_time > scheduled_start THEN 'Patient Not Ready'
            WHEN anesthesia_ready_time > scheduled_start THEN 'Anesthesia Delay'
            WHEN surgeon_arrival_time > scheduled_start THEN 'Surgeon Late'
            ELSE 'Other/Unknown'
        END as delay_reason
    FROM or_cases
    WHERE case_sequence = 1
        AND TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) > 5
        AND scheduled_start >= CURRENT_DATE - INTERVAL 30 DAY
) delay_analysis
GROUP BY delay_reason
ORDER BY frequency DESC;

-- Query 3: Day of Week Pattern Analysis
-- Purpose: Identify weekly patterns
SELECT 
    DAYNAME(scheduled_start) as day_of_week,
    DAYOFWEEK(scheduled_start) as day_number,
    COUNT(*) as total_cases,
    AVG(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as avg_delay,
    STDDEV(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as delay_stddev,
    MIN(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as min_delay,
    MAX(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as max_delay
FROM or_cases
WHERE 
    case_sequence = 1
    AND scheduled_start >= CURRENT_DATE - INTERVAL 90 DAY
    AND case_status = 'COMPLETED'
GROUP BY DAYNAME(scheduled_start), DAYOFWEEK(scheduled_start)
ORDER BY day_number;

-- Query 4: OR Room Performance Comparison
-- Purpose: Identify best/worst performing rooms
SELECT 
    or_room,
    COUNT(*) as total_first_cases,
    AVG(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as avg_delay,
    ROUND(100.0 * SUM(CASE WHEN TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) <= 5 THEN 1 ELSE 0 END) / COUNT(*), 1) as on_time_rate,
    SUM(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as total_delay_minutes
FROM or_cases
WHERE 
    case_sequence = 1
    AND scheduled_start >= CURRENT_DATE - INTERVAL 30 DAY
    AND case_status = 'COMPLETED'
GROUP BY or_room
HAVING COUNT(*) >= 10  -- Minimum sample size
ORDER BY avg_delay DESC;

-- Query 5: Surgeon On-Time Performance
-- Purpose: Identify surgeon-specific patterns (use diplomatically)
SELECT 
    surgeon_id,
    surgeon_name,
    COUNT(*) as total_first_cases,
    AVG(TIMESTAMPDIFF(MINUTE, scheduled_start, surgeon_arrival_time)) as avg_arrival_vs_scheduled,
    ROUND(100.0 * SUM(CASE WHEN surgeon_arrival_time <= scheduled_start THEN 1 ELSE 0 END) / COUNT(*), 1) as on_time_arrival_rate,
    AVG(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as avg_case_delay
FROM or_cases
WHERE 
    case_sequence = 1
    AND scheduled_start >= CURRENT_DATE - INTERVAL 30 DAY
    AND case_status = 'COMPLETED'
GROUP BY surgeon_id, surgeon_name
HAVING COUNT(*) >= 5  -- Minimum sample size
ORDER BY avg_arrival_vs_scheduled DESC;

-- Query 6: Financial Impact Calculator
-- Purpose: Calculate revenue loss from delays
SELECT 
    DATE_FORMAT(scheduled_start, '%Y-%m') as month,
    SUM(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as total_delay_minutes,
    ROUND(SUM(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) / 60.0, 1) as total_delay_hours,
    COUNT(*) as delayed_cases,
    -- Assumptions: $100/minute OR time, $50/minute overtime
    ROUND(SUM(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) * 100, 0) as lost_or_revenue,
    ROUND(SUM(CASE WHEN TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) > 30 THEN (TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) - 30) * 50 ELSE 0 END), 0) as overtime_costs,
    ROUND(SUM(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) * 100 + 
          SUM(CASE WHEN TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) > 30 THEN (TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) - 30) * 50 ELSE 0 END), 0) as total_financial_impact
FROM or_cases
WHERE 
    case_sequence = 1
    AND TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start) > 5
    AND scheduled_start >= CURRENT_DATE - INTERVAL 180 DAY
    AND case_status = 'COMPLETED'
GROUP BY DATE_FORMAT(scheduled_start, '%Y-%m')
ORDER BY month DESC;

-- Query 7: Predictive Delay Risk Factors
-- Purpose: Identify cases at high risk for delays
SELECT 
    CASE 
        WHEN DAYOFWEEK(scheduled_start) = 2 THEN 'High Risk - Monday'
        WHEN procedure_duration_estimate > 240 THEN 'High Risk - Long Case'
        WHEN equipment_complexity = 'HIGH' THEN 'High Risk - Complex Equipment'
        WHEN patient_age > 75 THEN 'Medium Risk - Elderly Patient'
        WHEN add_on_case = 'Y' THEN 'Medium Risk - Add-on'
        ELSE 'Low Risk'
    END as risk_category,
    COUNT(*) as case_count,
    AVG(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as avg_delay,
    STDDEV(TIMESTAMPDIFF(MINUTE, scheduled_start, actual_start)) as delay_variability
FROM or_cases
WHERE 
    case_sequence = 1
    AND scheduled_start >= CURRENT_DATE - INTERVAL 90 DAY
    AND case_status = 'COMPLETED'
GROUP BY risk_category
ORDER BY avg_delay DESC;