-- 01. Top 15 oldest companies
SELECT company, country, industry, founded_year
FROM companies
ORDER BY founded_year ASC
LIMIT 15;

-- 02. Number of 200+ year old companies by country
SELECT country, COUNT(*) AS old_companies
FROM companies
WHERE founded_year <= YEAR(CURDATE()) - 200
GROUP BY country
ORDER BY old_companies DESC;

-- 03. Number of 200+ year old companies by industry
SELECT industry, COUNT(*) AS total_companies
FROM companies
WHERE founded_year <= YEAR(CURDATE()) - 200
GROUP BY industry
ORDER BY total_companies DESC;

-- 04. Oldest company in each country
SELECT c1.country, c1.company, c1.founded_year
FROM companies c1
JOIN (
    SELECT country, MIN(founded_year) AS oldest_year
    FROM companies
    GROUP BY country
) c2
ON c1.country = c2.country AND c1.founded_year = c2.oldest_year
ORDER BY c1.founded_year ASC;

-- 05. Companies founded by century
SELECT 
    (founded_year DIV 100) + 1 AS century, 
    COUNT(*) AS total_companies
FROM companies
GROUP BY century
ORDER BY century;
