-- Overall success rate
SELECT
    COUNT(*) AS total_launches,
    ROUND(100.0 * SUM(is_success) / COUNT(*), 2) AS success_rate_pct
FROM space_launches;

-- Top 10 companies
SELECT company, COUNT(*) AS launches,
       ROUND(100.0 * SUM(is_success) / COUNT(*), 1) AS success_rate_pct
FROM space_launches
GROUP BY company
ORDER BY launches DESC
LIMIT 10;

-- Launches per year
SELECT year, COUNT(*) AS launches
FROM space_launches
WHERE year IS NOT NULL
GROUP BY year
ORDER BY year;