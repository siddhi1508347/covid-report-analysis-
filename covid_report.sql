CREATE DATABASE pandemic;
USE pandemic;

CREATE TABLE covid_india (
    state VARCHAR(50),
    total_cases INT,
    total_deaths INT,
    fatality_rate DECIMAL(5,2),
    cases_per_million DECIMAL(10,2),
    vaccination_v DECIMAL(5,2),
    positivity_rate DECIMAL(5,2)
);

INSERT INTO covid_india (state, total_cases, total_deaths, fatality_rate, cases_per_million, vaccination_v, positivity_rate)
VALUES
("Kerala", 599892, 8005, 1.33, 17961.0, 66.54, 44.71),
("Gujarat", 584486, 7919, 1.35, 9677.0, 66.54, 44.45),
("Delhi", 478739, 6229, 1.3, 28496.0, 66.54, 39.13),
("Karnataka", 392615, 5159, 1.31, 6426.0, 66.54, 35.06),
("West Bengal", 389116, 5195, 1.34, 4262.0, 66.54, 35.07),
("Tamil Nadu", 329705, 4250, 1.29, 4573.0, 66.54, 30.49),
("Andhra Pradesh", 324079, 4197, 1.3, 6534.0, 66.54, 30.68),
("Rajasthan", 249882, 3208, 1.28, 3648.0, 66.54, 24.49),
("Uttar Pradesh", 236958, 3045, 1.29, 1186.0, 66.54, 23.7);

-- 1. Top states by total cases
SELECT state, total_cases, total_deaths, fatality_rate
FROM covid_india
ORDER BY total_cases DESC;

-- 2. States ranked by cases per million (normalized)
SELECT state, cases_per_million
FROM covid_india
ORDER BY cases_per_million DESC;

-- 3. Highest positivity rate (possible under-testing indicator)
SELECT state, positivity_rate
FROM covid_india
ORDER BY positivity_rate DESC;

-- 4. Overall totals across all states
SELECT SUM(total_cases) AS total_cases_all,
       SUM(total_deaths) AS total_deaths_all,
       ROUND(SUM(total_deaths) * 100.0 / SUM(total_cases), 2) AS overall_fatality_rate
FROM covid_india;

-- 5. States above average fatality rate
SELECT state, fatality_rate
FROM covid_india
WHERE fatality_rate > (SELECT AVG(fatality_rate) FROM covid_india)
ORDER BY fatality_rate DESC;
