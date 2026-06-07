-- Q1: Total survivors
SELECT COUNT(*) AS survivors
FROM titanic
WHERE survived = 1;

-- Q2: Total non-survivors
SELECT COUNT(*) AS not_survived
FROM titanic
WHERE survived = 0;

-- Q3: Average passenger age
SELECT AVG(age) AS average_age
FROM titanic;

-- Q4: Average fare
SELECT AVG(fare) AS average_fare
FROM titanic;

-- Q5: Gender-wise passenger count
SELECT sex, COUNT(*) AS passenger_count
FROM titanic
GROUP BY sex;

-- Q6: Survival rate by passenger class
SELECT pclass,
       AVG(survived) * 100 AS survival_rate
FROM titanic
GROUP BY pclass
ORDER BY survival_rate DESC;

-- Q7: Average fare by passenger class
SELECT pclass,
       AVG(fare) AS average_fare
FROM titanic
GROUP BY pclass
ORDER BY average_fare DESC;