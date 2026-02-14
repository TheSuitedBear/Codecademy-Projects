-- Due to the way these projects are handled, reading them after the fact will be confusing --
-- Simply put, each new line seperated by at least one space was a new step/part of the challenge --
-- That's why their is numerous statements that say almost the same thing with one difference --

SELECT * FROM startups;

SELECT COUNT(*) FROM startups;

SELECT SUM(valuation) FROM startups;

SELECT MAX(raised) FROM startups
WHERE stage = 'Seed';

SELECT MIN(founded) FROM startups;


SELECT AVG(valuation) FROM startups;

SELECT category, AVG(valuation) FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation), 2)
FROM startups GROUP BY category;

SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY category
ORDER BY valuation DESC;


SELECT category, COUNT(*) FROM startups
GROUP BY category;

SELECT category, COUNT(*) FROM startups
GROUP BY category
HAVING COUNT(*) > 3;


SELECT location, AVG(employees) FROM startups
GROUP BY location;

SELECT location, AVG(employees) FROM startups
GROUP BY location
HAVING AVG(employees) > 500;