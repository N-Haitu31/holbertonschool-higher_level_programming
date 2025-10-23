-- script that lists all records with a score >= 10
--  display both the score and the name
-- ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
