-- The idea of this project was to analyze different trends within
-- a site called Hacker News

-- First bit is to just get an idea of the top stories on the site
SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

-- Finding the total score (likes) of all the stories on the site
SELECT SUM(score) FROM hacker_news;

-- Identifying Users who have more than 200 score total and what their score is
SELECT user, SUM(score) FROM hacker_news
GROUP BY user HAVING SUM(score) > 200
ORDER BY 2 DESC;

-- Finding what percentage of the total score on the site is owned by the top users, with the answer being 22%
SELECT (517 + 309 + 304 + 282) / 6366.0;

-- Identifying users who posted a Rickroll and how many times they did
SELECT user, COUNT(*) FROM hacker_news
WHERE url LIKE 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
GROUP BY user
ORDER BY COUNT(*) DESC;

-- Groups stories by if they link to Github, Medium, NYTimes or something else
SELECT CASE
  WHEN url LIKE '%github.com%' THEN 'Github'
  WHEN url LIKE '%medium.com%' THEN 'Medium'
  WHEN url LIKE '%nytimes.com%' THEN 'NYTimes'
  ELSE 'Other'
 END AS 'Source',
 COUNT(*)
FROM hacker_news
GROUP BY 1;

-- Looking into how times are displayed (when posts are made)
SELECT timestamp FROM hacker_news
LIMIT 10;

-- Lists different times in groups
SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

-- A query that gets the hours of 'Timestamp', the average score for each hour, and how many stories have been made each hour
SELECT strftime('%H', timestamp) AS 'Hour',
  ROUND(AVG(score), 1) AS 'Score',
  COUNT(*) AS 'Total'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;